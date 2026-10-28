from datetime import datetime, timedelta

from config import DATE_FORMAT, DEFAULT_LOAN_DAYS
from storage import (
    load_books,
    save_books,
    load_lending_records,
    save_lending_records
)
from book_manager import find_book
from utils import get_text, current_date, days_overdue


def generate_lending_id(records):
    highest = 0

    for record in records:
        record_id = record.get("lending_id", "")

        if record_id.startswith("LN"):
            try:
                highest = max(highest, int(record_id[2:]))
            except ValueError:
                continue

    return f"LN{highest + 1:04d}"


def lend_book():
    books = load_books()
    records = load_lending_records()

    book_id = input("Enter book ID: ").strip().upper()
    book = find_book(books, book_id)

    if not book:
        print("Book not found.")
        return

    if book["available"] <= 0:
        print("No copies are currently available.")
        return

    borrower = get_text("Borrower's name: ")
    phone = input("Borrower's phone (optional): ").strip()

    due_date = (
        datetime.strptime(current_date(), DATE_FORMAT)
        + timedelta(days=DEFAULT_LOAN_DAYS)
    ).strftime(DATE_FORMAT)

    record = {
        "lending_id": generate_lending_id(records),
        "book_id": book["book_id"],
        "book_title": book["title"],
        "borrower": borrower,
        "phone": phone,
        "borrow_date": current_date(),
        "due_date": due_date,
        "return_date": None,
        "status": "Borrowed"
    }

    book["available"] -= 1
    records.append(record)

    save_books(books)
    save_lending_records(records)

    print("Book lent successfully.")
    print(f"Lending ID: {record['lending_id']}")
    print(f"Return by: {due_date}")


def return_book():
    books = load_books()
    records = load_lending_records()

    lending_id = input("Enter lending ID: ").strip().upper()

    for record in records:
        if record.get("lending_id", "").upper() != lending_id:
            continue

        if record["status"] == "Returned":
            print("This book has already been returned.")
            return

        book = find_book(books, record["book_id"])

        if not book:
            print("The associated book record is missing.")
            return

        record["status"] = "Returned"
        record["return_date"] = current_date()
        book["available"] = min(
            book["quantity"],
            book["available"] + 1
        )

        save_books(books)
        save_lending_records(records)

        print("Book returned successfully.")
        print(f"Book: {record['book_title']}")
        print(f"Returned on: {record['return_date']}")
        return

    print("Lending record not found.")


def list_lending_records():
    records = load_lending_records()

    print("\n--- Lending History ---")

    if not records:
        print("No lending records found.")
        return

    for record in records:
        print("-" * 45)
        print(f"Lending ID : {record['lending_id']}")
        print(f"Book       : {record['book_title']}")
        print(f"Borrower   : {record['borrower']}")
        print(f"Borrow Date: {record['borrow_date']}")
        print(f"Due Date   : {record['due_date']}")
        print(f"Return Date: {record.get('return_date') or 'Not returned'}")
        print(f"Status     : {record['status']}")
        print("-" * 45)


def list_borrowed_books():
    records = load_lending_records()

    active = [
        record for record in records
        if record.get("status") == "Borrowed"
    ]

    print("\n--- Currently Borrowed Books ---")

    if not active:
        print("No books are currently borrowed.")
        return

    for record in active:
        overdue = days_overdue(record["due_date"])

        print(
            f"{record['lending_id']} | "
            f"{record['book_title']} | "
            f"{record['borrower']} | "
            f"Due: {record['due_date']} | "
            f"Overdue days: {overdue}"
        )


def search_borrower():
    records = load_lending_records()

    keyword = input("Enter borrower name: ").strip().lower()

    if not keyword:
        print("Enter a borrower name.")
        return

    results = [
        record for record in records
        if keyword in record.get("borrower", "").lower()
    ]

    if not results:
        print("No lending history found for this borrower.")
        return

    for record in results:
        print(
            f"{record['lending_id']} | "
            f"{record['book_title']} | "
            f"{record['borrow_date']} | "
            f"{record['status']}"
        )
