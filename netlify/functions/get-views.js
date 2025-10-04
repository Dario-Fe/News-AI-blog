import { getStore } from '@netlify/blobs';

export default async () => {
  console.log("Function 'get-views' invoked for final diagnostics.");

  try {
    const store = getStore('page-views');
    console.log("Blob store 'page-views' accessed.");

    // --- FINAL DIAGNOSTIC STEP ---
    // The goal is to see the exact structure of what store.list() returns.
    const listResult = await store.list();
    
    // Log the raw result to the server logs. This is the most crucial part.
    console.log("RAW DIAGNOSTIC DATA from store.list():", JSON.stringify(listResult, null, 2));

    // Also return a success message to the browser console so we know the function ran.
    return new Response(JSON.stringify({
      diagnostic_message: "Function executed. Check Netlify server logs for 'RAW DIAGNOSTIC DATA'.",
      raw_result_type: typeof listResult,
      has_blobs_property: listResult.hasOwnProperty('blobs')
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
    });

  } catch (error) {
    console.error('CRITICAL ERROR during final diagnostics:', error);
    return new Response(JSON.stringify({ error: 'Internal Server Error during diagnostics', message: error.message }), { 
        status: 500,
        headers: { 'Content-Type': 'application/json' }
    });
  }
};