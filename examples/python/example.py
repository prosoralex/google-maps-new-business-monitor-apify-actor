"""
Run the "Google Maps New Business Monitor – New Local Leads" Apify Actor and print its results.

Setup:
    pip install -r requirements.txt
    export APIFY_TOKEN=your_apify_token   # Apify Console > Settings > API & Integrations

This repository only documents the Actor; its source code runs on Apify's infrastructure.
"""
import os
import sys

from apify_client import ApifyClient

ACTOR_ID = "leadsbrary/google-maps-new-business-monitor"

RUN_INPUT = {
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


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set the APIFY_TOKEN environment variable first (Apify Console > Settings > API & Integrations).")
    client = ApifyClient(token)
    print(f"Starting {ACTOR_ID} ...")
    run = client.actor(ACTOR_ID).call(run_input=RUN_INPUT)
    print(f"Run finished with status: {run['status']}")
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)


if __name__ == "__main__":
    main()
