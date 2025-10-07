# workflow_test.py
import requests

# =========================
# CONFIGURATION
# =========================

# Temporary webhook for testing (development mode)
dev_webhook = "http://localhost:5678/webhook-test/insurance-alert"

# Production webhook (after activating workflow in n8n)
prod_webhook = "http://localhost:5678/webhook/insurance-alert"

# Choose which URL to use
webhook_url = prod_webhook  # change to dev_webhook for testing

# =========================
# GENERATE SAMPLE CLAIMS
# =========================

claims = [
    {
        "claim_id": f"C{10000 + i}",
        "claim_amount": 500000 + i * 20000,  # random increasing amounts
        "fraud_score": 50 + i,               # fraud score 50-69
        "policy_expiry": "2025-11-06"
    }
    for i in range(20)
]

# =========================
# SEND CLAIMS TO WEBHOOK
# =========================

for claim in claims:
    try:
        response = requests.post(webhook_url, json=claim)
        if response.status_code == 200:
            print(f"Sent {claim['claim_id']} successfully.")
        else:
            print(f"Error sending {claim['claim_id']}: {response.status_code}")
    except Exception as e:
        print(f"Exception sending {claim['claim_id']}: {e}")

print("All claims processed.")
