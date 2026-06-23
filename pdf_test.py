from pdf_generator import generate_pdf

path = generate_pdf(
    "sample.py",
    65,
    84,
    "Good code but has nested loops.",
    "Use dictionary lookups instead."
)

print(path)