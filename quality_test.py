from agents.quality_agent import calculate_quality_score


review = """
The code is well structured and readable.

Strengths:
- Proper function decomposition
- Meaningful variable names
- Good coding practices

Issues:
- Missing docstrings
- Could improve error handling

Overall the code quality is good.
"""

score = calculate_quality_score(review)

print("Quality Score:", score)