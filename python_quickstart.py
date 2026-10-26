"""
SaaS Pricing Page, Plan Tiers & Competitor Feature Spy — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/saas-pricing-page-tier-feature-extractor ($0.80 / 1,000 pages)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~saas-pricing-page-tier-feature-extractor/run-sync-get-dataset-items"

payload = {
    "urls": [
        "https://linear.app/pricing",
        "https://supabase.com/pricing"
    ]
}

if __name__ == "__main__":
    print(f"Running SaaS Pricing Page, Plan Tiers & Competitor Feature Spy on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
