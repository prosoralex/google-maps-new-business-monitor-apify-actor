# Google Maps New Business Monitor – New Local Leads — Apify Actor usage guide

[![Run on Apify](https://img.shields.io/badge/Apify-Run%20this%20Actor-24C1E0)](https://apify.com/leadsbrary/google-maps-new-business-monitor?fpr=aupara)
[![Try Apify free](https://img.shields.io/badge/Apify-Try%20it%20free-24C1E0)](https://console.apify.com/sign-up?fpr=aupara)

Monitor Google Maps for new businesses: schedule per category and city, get only newly listed places with name, address, phone, website, rating and coordinates. Export JSON, CSV, Excel. From $1.00 per 1,000 results.

> **This repository does not contain the Actor's source code.** The Actor is closed-source and
> runs on Apify's infrastructure. This repo is documentation plus ready-to-run client examples
> (curl, Python, JavaScript) that call the hosted Actor with **your own** Apify API token.

**Run it on Apify →** [https://apify.com/leadsbrary/google-maps-new-business-monitor?fpr=aupara](https://apify.com/leadsbrary/google-maps-new-business-monitor?fpr=aupara)

## What it does

Monitor Google Maps for new businesses: schedule per category and city, get only newly listed places with name, address, phone, website, rating and coordinates. Export JSON, CSV, Excel. From $1.00 per 1,000 results.

## Use cases

- Daily or weekly scheduled run per category + city that outputs only newly appeared listings (new-lead alert feed)
- Franchise / competitor territory watch: be notified when a competitor brand opens a new location in an area
- Feed a CRM, Google Sheet, Slack or Zapier/Make webhook with fresh local leads before competitors reach them
- Commercial real-estate scouting: track openings in a neighborhood as a market-activity signal


## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `searchQueries` | array | yes | Business categories or keywords to monitor, as you would type them in Google Maps (e.g. coffee shop, dentist). |
| `locations` | array | yes | Cities, neighborhoods or postal areas. Each query is searched in each location. |
| `monitorId` | string | no | Name of the monitor whose seen-place history is reused between runs (letters, digits, dashes). Use a different ID per independent watch list. |
| `outputMode` | string | no | new_only = only places not seen in earlier runs of this monitor. all = every scanned place, with changeType/isNew flags. |
| `emitBaseline` | boolean | no | On the first run of a monitor (no history yet) output all found places as changeType=BASELINE. If off, the first run only records history and outputs nothing. |
| `maxPlacesPerSearch` | integer | no | Maximum places scanned per query + location (Google returns 20 per page, about 120 at most). |
| `maxResults` | integer | no | Stop after this many delivered results (also protects your spending). |
| `language` | string | no | Language code for names and categories returned by Google (e.g. en, de, fr). |
| `countryCode` | string | no | Two-letter country code (e.g. us, gb, de) used as Google's regional setting. Leave empty to detect it from the first results. |
| `historyRetentionDays` | integer | no | Place IDs not seen again for this many days are dropped from the monitor history (only IDs and dates are stored). |
| `resetHistory` | boolean | no | Clear this monitor's history before the run (this run becomes a new baseline). |
| `proxyConfiguration` | object | no | Apify datacenter proxy is used by default. |

The full input form (with defaults and validation) is on the [Actor page](https://apify.com/leadsbrary/google-maps-new-business-monitor?fpr=aupara).


## Output (sample item)

Sample trimmed for readability (long texts and lists are shortened) — a real run returns the complete data.

```json
{
  "placeId": "ChIJ1S_Bov20RIYRe7MiR8tYawY",
  "name": "Jo's Coffee – South Congress",
  "changeType": "BASELINE",
  "isNew": false,
  "firstSeenAt": "2026-10-03T14:48:18.652Z",
  "category": "Coffee shop",
  "categories": [
    "Coffee shop",
    "Cafe"
  ],
  "address": "1300 S Congress Ave, Austin, TX 78704",
  "city": "Austin",
  "postalCode": "78704",
  "countryCode": "US",
  "latitude": 30.2510458,
  "longitude": -97.7493717,
  "phone": "+15128522300",
  "website": "https://www.joscoffee.com/south-congress-jos",
  "rating": 4.4,
  "reviewsCount": null,
  "priceLevel": null,
  "businessStatus": null,
  "googleMapsUrl": "https://www.google.com/maps/place/?q=place_id:ChIJ1S_Bov20RIYRe7MiR8tYawY",
  "searchQuery": "coffee shop",
  "location": "Austin, TX, USA",
  "monitorId": "smoke-example",
  "scrapedAt": "2026-10-03T14:48:18.652Z"
}
```

## Pricing

Pay only for results: about **$1.50 per 1,000 results** on the Apify Free plan, down to **$1.00 per 1,000** on paid Apify plans.

Apify platform usage (compute) is billed by Apify on top of the per-result price — about **$0.02 per 1,000 results** in our measured test runs (estimate, varies with input). Tip: keep only the output formats and options you need to reduce it.

Prices can change — the [Actor page](https://apify.com/leadsbrary/google-maps-new-business-monitor?fpr=aupara) always shows the current pricing.

## Quick start

You need an Apify account and an API token (Apify Console → **Settings → API & Integrations**).
Never commit your token: export it as the `APIFY_TOKEN` environment variable.

### cURL

```bash
curl -X POST "https://api.apify.com/v2/acts/leadsbrary~google-maps-new-business-monitor/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
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
```

### Python (`apify-client`)

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "searchQueries": [
        "coffee shop"
    ],
    "locations": [
        "Austin, TX, USA"
    ],
    "monitorId": "austin-coffee",
    "outputMode": "new_only",
    "emitBaseline": True,
    "maxPlacesPerSearch": 20,
    "maxResults": 3,
    "language": "en",
    "historyRetentionDays": 90,
    "resetHistory": False,
    "proxyConfiguration": {
        "useApifyProxy": True
    }
}

run = client.actor("leadsbrary/google-maps-new-business-monitor").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### JavaScript (`apify-client`)

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

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
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

Runnable versions live in [`examples/`](./examples).

## Troubleshooting

- **401 / "User was not found or authentication token is not valid"** — check that `APIFY_TOKEN` is set and copied completely.
- **The run finished but the dataset is empty** — widen your search input or check the run log on the Apify Console.
- **Run stops early** — you may have reached the maximum cost per run you set in Apify; raise it in the run options.
- **Need something else?** Open an issue in this repository or use the Issues tab on the Actor page.

## Don't have an Apify account yet?

[Sign up here](https://console.apify.com/sign-up?fpr=aupara) — new accounts get $5 of free platform usage every month, enough to try most Actors without paying upfront.
Browse the full [Apify Store](https://apify.com/store?fpr=aupara) or [all Actors from this developer](https://apify.com/leadsbrary?fpr=aupara).

## Links

- Actor page: [https://apify.com/leadsbrary/google-maps-new-business-monitor?fpr=aupara](https://apify.com/leadsbrary/google-maps-new-business-monitor?fpr=aupara)
- All Actors from this developer: [https://apify.com/leadsbrary?fpr=aupara](https://apify.com/leadsbrary?fpr=aupara)
- Apify API reference: [https://docs.apify.com/api/v2](https://docs.apify.com/api/v2)

## Keywords

google maps new business monitor, new business scraper, google maps change alert, new business leads, newly opened businesses, local lead monitor, google maps scraper, google maps monitoring, new restaurant openings, franchise territory monitoring, local business leads, google places new listings, new store openings data

#GoogleMaps #LeadGeneration #NewBusiness #LocalLeads #BusinessMonitoring #WebScraping #Apify #SalesProspecting #RealEstate #Franchise

## License

The example code in this repository is released under the MIT License — see [LICENSE](./LICENSE).
It does not cover the Actor itself, which remains closed-source and is operated by its developer on Apify.
