from agents.optimization_agent import get_optimization_suggestions


sample_code = """
for i in range(1000):
    for j in range(1000):
        print(i, j)
"""


result = get_optimization_suggestions(sample_code)

print(result)