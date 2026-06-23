from config import model


def get_optimization_suggestions(code):

    prompt = f"""
You are a Senior Python Performance Engineer.

Analyze the following Python code and provide:

1. Time Complexity
2. Space Complexity
3. Performance Bottlenecks
4. Optimization Suggestions
5. Better Data Structures (if applicable)
6. Alternative Efficient Approach
7. Refactored Code (if needed)

Return the response in clean markdown format.

Code:
{code}
"""

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Optimization Agent Error: {str(e)}"