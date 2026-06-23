from database import *

initialize_database()

save_review(
    "sample.py",
    75,
    88,
    "Good code structure"
)

reviews = fetch_reviews()

for row in reviews:
    print(row)