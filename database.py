import sqlite3

DB_NAME = "review_history.db"


def initialize_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        risk_score INTEGER,
        quality_score INTEGER,
        review TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_review(
        filename,
        risk_score,
        quality_score,
        review
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reviews
        (
            filename,
            risk_score,
            quality_score,
            review
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            filename,
            risk_score,
            quality_score,
            review
        )
    )

    conn.commit()
    conn.close()


def fetch_reviews():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM reviews
        ORDER BY id DESC
        """
    )

    reviews = cursor.fetchall()

    conn.close()

    return reviews