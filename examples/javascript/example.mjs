// Run the "Google Maps New Business Monitor – New Local Leads" Apify Actor and print its results.
// Setup: npm install  &&  export APIFY_TOKEN=your_apify_token  &&  node example.mjs
// This repository only documents the Actor; its source code runs on Apify's infrastructure.
import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_TOKEN;
if (!token) {
    console.error('Set the APIFY_TOKEN environment variable first (Apify Console > Settings > API & Integrations).');
    process.exit(1);
}

const client = new ApifyClient({ token });

const runInput = {
  "searchQueries": [
    "coffee shop"
  ],
  "locations": [
    "Austin, TX, USA"
  ],
  "monitorId": "austin-coffee",
  "outputMode": "new_only",
  "emitBaseline": true,
  "maxPlacesPerSearch": 20,
  "maxResults": 3,
  "language": "en",
  "historyRetentionDays": 90,
  "resetHistory": false,
  "proxyConfiguration": {
    "useApifyProxy": true
  }
};

const run = await client.actor('leadsbrary/google-maps-new-business-monitor').call(runInput);
console.log(`Run finished with status: ${run.status}`);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));
