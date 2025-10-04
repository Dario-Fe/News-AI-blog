export default async (req, context) => {
  const authHeader = req.headers.get('authorization');

  // Get credentials from environment variables
  const user = Deno.env.get('STATS_USER');
  const pass = Deno.env.get('STATS_PASSWORD');

  // If the credentials are not set in the Netlify dashboard, deny access.
  if (!user || !pass) {
    console.error('STATS_USER or STATS_PASSWORD environment variables not set.');
    return new Response('Authentication is not configured on the server.', { status: 500 });
  }

  // Encode the expected credentials to match the browser's format
  const expectedAuth = 'Basic ' + btoa(`${user}:${pass}`);

  // If the browser's credentials don't match, prompt for them
  if (authHeader !== expectedAuth) {
    return new Response('Unauthorized', {
      status: 401,
      headers: {
        'WWW-Authenticate': 'Basic realm="Restricted Area"',
      },
    });
  }

  // If authentication is successful, proceed to the requested page
  return context.next();
};