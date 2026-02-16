from datetime import datetime, timezone

def calculate_lead_score(phone=None, email=None, company_name=None, budget=None):
    score = 0
    if phone:
        score += 10
    if email:
        score += 10
    if company_name:
        score += 15
    if budget and budget > 1000:
        score += 20
    return score

def get_today():
    return datetime.now(timezone.utc).date()
