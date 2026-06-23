from config import model
import re


def calculate_risk_score(review_text):

    prompt = f"""
You are a software security auditor.

Analyze the following code review and assign a Risk Score from 0 to 100.

Risk Levels:
0-20   = Very Low Risk
21-40  = Low Risk
41-60  = Medium Risk
61-80  = High Risk
81-100 = Critical Risk

Return ONLY the numeric score.

Review:
{review_text}
"""

    try:

        response = model.generate_content(prompt)

        response_text = response.text.strip()

        # Extract first number from response
        numbers = re.findall(r'\d+', response_text)

        if numbers:

            score = int(numbers[0])

            # Keep score within range
            score = max(0, min(score, 100))

            return score

        return 50

    except Exception as e:

        print(f"Risk Agent Error: {e}")

        return 50