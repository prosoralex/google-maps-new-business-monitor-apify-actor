#!/usr/bin/env bash
# Run the "Google Maps New Business Monitor – New Local Leads" Apify Actor synchronously and print the dataset items.
# Usage: export APIFY_TOKEN=your_apify_token && ./run.sh
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN first (Apify Console > Settings > API & Integrations)}"

curl -sS -X POST "https://api.apify.com/v2/acts/leadsbrary~google-maps-new-business-monitor/run-sync-get-dataset-items" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
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
}
JSON
