from config import model
from config import require_model


def review_code(code, language):

    prompt = f"""
You are a Senior Software Engineer.

Analyze the following {language} code.

Provide:

1. Code Summary
2. Bugs Found
3. Security Issues
4. Performance Issues
5. Code Smells
6. Best Practice Violations
7. Suggestions for Improvement

Return the answer in clean markdown.

Code:

{code}
"""

    try:
        model = require_model()
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Error during review: {str(e)}"