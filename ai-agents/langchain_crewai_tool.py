"""
SaaS Pricing Page, Plan Tiers & Competitor Feature Spy — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/saas-pricing-page-tier-feature-extractor ($0.80 / 1,000 pages)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~saas-pricing-page-tier-feature-extractor/run-sync-get-dataset-items"

def run_saas_pricing_page_tier_feature_extractor(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes SaaS Pricing Page, Plan Tiers & Competitor Feature Spy on Apify Cloud ($0.80/1k pages).
    Analyze any list of SaaS company domains or pricing URLs to extract plan names, monthly/annual pricing tiers, freemium/trial flags, enterprise contact-sales gating, and competitive pricing intelligence.
    """
    default_payload = {
    "urls": [
        "https://linear.app/pricing",
        "https://supabase.com/pricing"
    ]
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()
