import { getStore } from '@netlify/blobs';

// Contatore pageview per path.
//
// La versione precedente faceva un read-modify-write non atomico:
//
//   const current = await store.get(key) || { count: 0 };
//   current.count += 1;
//   await store.setJSON(key, current);
//
// Due problemi reali, entrambi visibili in produzione:
//
// 1. le letture sono "eventual" per default (aggiornamenti e delete si propagano
//    fino a 60 secondi), quindi due visite ravvicinate leggevano lo stesso valore
//    e la seconda scrittura cancellava la prima (incrementi persi nei picchi);
// 2. se la lettura tornava vuota il conteggio ripartiva da 1: il 26/09/2026 il
//    path "de" è passato da 217 a 1 e la dashboard ha registrato 53 visite in un
//    giorno in cui il contatore era già 200+ sopra il valore precedente.
//
// Qui l'incremento è: lettura con consistenza "strong" + scrittura condizionata
// sull'ETag (onlyIfMatch / onlyIfNew). La scrittura va a buon fine solo se
// nessun altro ha modificato il blob nel frattempo, altrimenti si riprova.
// Ogni visita persa dopo N tentativi viene annotata con un blob di perdita
// (chiave univoca, quindi mai in conflitto) che update-stats.mjs conta nel
// riepilogo: così l'anomalia è misurabile invece di essere invisibile.

const STORE_NAME = 'page-views';
const MAX_ATTEMPTS = 5;
const LOST_PREFIX = '__lost__/';

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function backoffMs(attempt) {
  return Math.min(50 * 2 ** (attempt - 1), 400) + Math.floor(Math.random() * 25);
}

async function recordLostWrite(store, attempts) {
  const now = new Date();
  const day = now.toISOString().slice(0, 10);
  const key = `${LOST_PREFIX}${day}/${now.getTime()}-${Math.random().toString(36).slice(2, 8)}`;
  try {
    await store.setJSON(key, { attempts, at: now.toISOString() });
  } catch (error) {
    console.error('Impossibile annotare la scrittura persa:', error);
  }
}

async function increment(store, key) {
  for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
    const current = await store.getWithMetadata(key, { type: 'json', consistency: 'strong' });

    // Blob assente: si crea solo se non esiste, così due richieste simultanee
    // non possono sovrascriversi.
    if (current === null) {
      const fresh = { count: 1, updatedAt: new Date().toISOString() };
      const { modified } = await store.setJSON(key, fresh, { onlyIfNew: true });
      if (modified) return { modified: true, attempts: attempt, count: fresh.count };
      await sleep(backoffMs(attempt));
      continue;
    }

    const stored = current.data;
    const valid = stored && typeof stored.count === 'number' && Number.isFinite(stored.count);
    if (!valid) {
      console.error(`Contatore illeggibile per "${key}", viene ricreato da zero:`, stored);
    }
    const count = valid ? stored.count : 0;
    const next = { count: count + 1, updatedAt: new Date().toISOString() };

    if (!current.etag) {
      // Senza ETag non è possibile una scrittura condizionata: meglio contare la
      // visita (last write wins) che perderla, ma lo segnaliamo perché è il caso
      // in cui due visite ravvicinate possono ancora sovrascriversi.
      console.error(`Nessun ETag per "${key}": scrittura non condizionata.`);
      await store.setJSON(key, next);
      return { modified: true, attempts: attempt, count: next.count, unconditional: true };
    }

    const { modified } = await store.setJSON(key, next, { onlyIfMatch: current.etag });
    if (modified) return { modified: true, attempts: attempt, count: next.count };

    await sleep(backoffMs(attempt));
  }

  return { modified: false, attempts: MAX_ATTEMPTS };
}

export default async (req) => {
  if (req.method !== 'POST') {
    return new Response('Method Not Allowed', { status: 405 });
  }

  try {
    const { path } = await req.json();

    if (!path || typeof path !== 'string' || !path.startsWith('/')) {
      return new Response('Invalid path', { status: 400 });
    }

    // The key for the blob store cannot start with a slash.
    const storeKey = path.slice(1);

    const store = getStore({ name: STORE_NAME, consistency: 'strong' });
    const result = await increment(store, storeKey);

    if (!result.modified) {
      // Il beacon non ritenta: la visita è persa, la annotiamo per poterla contare.
      await recordLostWrite(store, result.attempts);
      console.error(`Incremento non riuscito dopo ${result.attempts} tentativi per "${storeKey}".`);
    }

    return new Response(JSON.stringify({ success: true, modified: result.modified }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    console.error('Error in page-view function:', error);
    return new Response('Internal Server Error', { status: 500 });
  }
};
