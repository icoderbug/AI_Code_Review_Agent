from config import model
import re


def calculate_quality_score(review_text):

    prompt = f"""
You are a senior software engineer and code quality auditor.

Analyze the following code review and assign a Quality Score from 0 to 100.

Quality Levels:
0-20   = Poor
21-40  = Weak
41-60  = Average
61-80  = Good
81-100 = Excellent

Consider:
- Readability
- Maintainability
- Code Structure
- Naming Conventions
- Documentation
- Performance
- Security Practices

Return ONLY the numeric score.

Review:
{review_text}
"""

    try:

        response = model.generate_content(prompt)

        response_text = response.text.strip()

        numbers = re.findall(r"\d+", response_text)

        if numbers:

            score = int(numbers[0])

            score = max(0, min(score, 100))

            return score

        return 70

    except Exception as e:

        print(f"Quality Agent Error: {e}")

        return 70