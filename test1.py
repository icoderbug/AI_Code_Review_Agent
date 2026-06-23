from agents.code_review_agent import review_code

sample_code = """
a=10
b=20
print(a+b)
"""

print(review_code(sample_code))