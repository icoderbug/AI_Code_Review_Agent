from agents.risk_agent import calculate_risk_score

review = """
Code contains:
- Hardcoded password
- SQL injection vulnerability
- Nested loops
- Unused variables
"""

score = calculate_risk_score(review)

print("Risk Score:", score)