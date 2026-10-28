from storage import initialize_storage
from book_manager import add_book, list_books, search_books
from lending_manager import (
    lend_book,
    return_book,
    list_lending_records,
    list_borrowed_books,
    search_borrower
)
from report_manager import (
    lending_summary,
    popular_books_report,
    overdue_report
)
from utils import pause


def show_menu():
    print("\n" + "=" * 43)
    print("       PERSONAL BOOK LENDING TRACKER")
    print("=" * 43)
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Books")
    print("4. Lend a Book")
    print("5. Return a Book")
    print("6. View Lending History")
    print("7. View Currently Borrowed Books")
    print("8. Search Borrower History")
    print("9. Lending Summary")
    print("10. Most Borrowed Books")
    print("11. Overdue Report")
    print("0. Exit")
    print("=" * 43)


def main():
    initialize_storage()

    actions = {
        "1": add_book,
        "2": list_books,
        "3": search_books,
        "4": lend_book,
        "5": return_book,
        "6": list_lending_records,
        "7": list_borrowed_books,
        "8": search_borrower,
        "9": lending_summary,
        "10": popular_books_report,
        "11": overdue_report
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using Personal Book Lending Tracker!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (OSError, ValueError, KeyError, TypeError) as error:
                print(f"An error occurred: {error}")

            pause()
        else:
            print("Invalid choice. Please select a valid option.")
            pause()


if __name__ == "__main__":
    main()
