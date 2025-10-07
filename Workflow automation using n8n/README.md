![Screenshot 2025-10-07 180928](https://github.com/user-attachments/assets/3f89a361-a5ec-4940-9298-d0488fa7bc01)



# Insurance Workflow Automation Project

## Overview
This project automates insurance workflows using **n8n**, **Gmail**, **Google Sheets**, and optional **Telegram notifications**.  
It is designed to handle the following tasks:

1. Trigger alert if a claim exceeds ₹5 lakh  
2. Auto-notify underwriter if fraud risk score > 80  
3. Send renewal reminder emails 30 days before policy expiry  
4. Log all claim data into Google Sheets  

All automation workflows are built using **free tools** and a local n8n Docker setup.

---

## Project Structure
![Screenshot 2025-10-07 181712](https://github.com/user-attachments/assets/1c98efaf-3d43-4689-aff4-f579a6e36dbe)


---

## Requirements

- Docker  
- n8n (local installation)  
- Python 3.x  
- Gmail account (for sending alerts)  
- Google Sheet (for logging claims)  
- Optional: Telegram bot for group notifications  

---

## Setup Instructions

### 1. Start n8n
~~~bash
docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
~~~
Open in browser: `http://localhost:5678`

### 2. Import Workflow
- Open n8n → ☰ → Import → select `insurance_workflow.json`  
- Click **Activate Workflow**  

### 3. Connect Gmail Node
- In Gmail Node → connect your Gmail account via OAuth  
- Use redirect URL:  
~~~text
http://localhost:5678/rest/oauth2-credential/callback
~~~

### 4. Configure Google Sheet Node
- Create a sheet with columns:  
~~~text
Claim ID, Claim Amount, Fraud Score, Policy Expiry, Timestamp
~~~
- Copy spreadsheet ID and paste in n8n node  

### 5. (Optional) Configure Telegram Node
- Create a bot using @BotFather → copy bot token  
- Add Telegram Node → set chat ID → connect  

---

## Test Workflow (Development Mode)

1. Use **temporary webhook** URL:  
~~~text
http://localhost:5678/webhook-test/insurance-alert
~~~

2. Run Python script to send sample claims:
~~~python
import requests

dev_webhook = "http://localhost:5678/webhook-test/insurance-alert"

claims = [
    {"claim_id": f"C{10000+i}", "claim_amount": 500000+i*1000, "fraud_score": 50+i, "policy_expiry": "2025-11-06"}
    for i in range(20)
]

for claim in claims:
    r = requests.post(dev_webhook, json=claim)
    print(f"Sent {claim['claim_id']}, status: {r.status_code}")
~~~

3. Verify alerts in Gmail, Google Sheet entries, optional Telegram messages.  

---

## Production Mode

1. **Activate workflow** in n8n → the webhook URL becomes **permanent**:  
~~~text
http://localhost:5678/webhook/insurance-alert
~~~

2. Update your Python script to use **production webhook**:
~~~python
import requests

prod_webhook = "http://localhost:5678/webhook/insurance-alert"

# Example 20 claims
claims = [
    {"claim_id": f"C{20000+i}", "claim_amount": 550000+i*2000, "fraud_score": 55+i, "policy_expiry": "2025-12-31"}
    for i in range(20)
]

for claim in claims:
    response = requests.post(prod_webhook, json=claim)
    if response.status_code == 200:
        print(f"Sent {claim['claim_id']} successfully")
    else:
        print(f"Error sending {claim['claim_id']}: {response.status_code}")
~~~

3. Now all incoming claims are **logged in Google Sheet**, **Gmail alerts triggered**, and **Telegram alerts sent** if configured.  

> ✅ **Tip:** Always test with dev URL first to avoid sending incorrect data in production.

---

## How to Use

- Send claim JSON payload to production webhook URL:
~~~json
{
    "claim_id": "C12345",
    "claim_amount": 650000,
    "fraud_score": 72,
    "policy_expiry": "2025-11-06"
}
~~~

Workflow automatically:
- Sends Gmail alerts if claim > ₹5L or fraud score > 80  
- Logs claim into Google Sheet  
- Optional: Sends Telegram alert  

---

## Task-wise Explanation

### Task 1: Webhook Setup
- Created webhook node in n8n to receive claim data  
- Temporary URL: `/webhook-test/insurance-alert`  
- Permanent URL (production): `/webhook/insurance-alert`

### Task 2: High Claim Alert
- IF Node checks `claim_amount > 500000`  
- Gmail Node sends alert to team  

### Task 3: Fraud Alert
- IF Node checks `fraud_score > 80`  
- Gmail Node sends alert to underwriter  

### Task 4: Logging to Google Sheet
- Sheet Columns: `Claim ID, Claim Amount, Fraud Score, Policy Expiry, Timestamp`  
- Google Sheet Node appends every claim automatically  

### Task 5: Renewal Reminder (Optional)
- Cron Node runs daily  
- IF Node checks `policy_expiry < 30 days`  
- Gmail Node sends reminder to customer  

### Task 6: Telegram Alerts (Optional)
- Telegram Node sends group alerts for urgent claims  
- Free and works for small teams  

### Task 7: Python Test Script
- Sends sample claims (20+) to webhook  
- Tests workflow automatically  

### Task 8: Production Mode
- Activate workflow → permanent webhook URL  
- Python script uses production URL to send live claims  
- Logs, Gmail, and Telegram alerts work automatically  

---

## References

- n8n Docs: [https://docs.n8n.io/](https://docs.n8n.io/)  
- Google Sheets API: [https://developers.google.com/sheets/api](https://developers.google.com/sheets/api)  
- Gmail OAuth: [https://developers.google.com/identity/protocols/oauth2](https://developers.google.com/identity/protocols/oauth2)
