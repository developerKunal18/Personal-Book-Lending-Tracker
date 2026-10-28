from collections import Counter
from storage import load_books, load_lending_records
from utils import days_overdue


def lending_summary():
    books = load_books()
    records = load_lending_records()

    borrowed = [
        record for record in records
        if record.get("status") == "Borrowed"
    ]

    returned = [
        record for record in records
        if record.get("status") == "Returned"
    ]

    overdue = [
        record for record in borrowed
        if days_overdue(record["due_date"]) > 0
    ]

    print("\n========== LENDING SUMMARY ==========")
    print(f"Book titles             : {len(books)}")
    print(f"Total lending records   : {len(records)}")
    print(f"Currently borrowed      : {len(borrowed)}")
    print(f"Returned records        : {len(returned)}")
    print(f"Overdue books           : {len(overdue)}")
    print("=====================================")


def popular_books_report():
    records = load_lending_records()

    if not records:
        print("No lending history available.")
        return

    counts = Counter(
        record.get("book_title", "Unknown")
        for record in records
    )

    print("\n--- Most Borrowed Books ---")

    for title, count in counts.most_common():
        print(f"{title}: borrowed {count} time(s)")


def overdue_report():
    records = load_lending_records()

    overdue = [
        record for record in records
        if record.get("status") == "Borrowed"
        and days_overdue(record["due_date"]) > 0
    ]

    print("\n--- Overdue Lending Records ---")

    if not overdue:
        print("No overdue books.")
        return

    for record in overdue:
        print(
            f"{record['lending_id']} | "
            f"{record['book_title']} | "
            f"{record['borrower']} | "
            f"{days_overdue(record['due_date'])} day(s) overdue"
        )
