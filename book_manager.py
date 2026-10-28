from storage import load_books, save_books
from utils import get_text, get_positive_integer


def generate_book_id(books):
    highest = 0

    for book in books:
        book_id = book.get("book_id", "")

        if book_id.startswith("BK"):
            try:
                highest = max(highest, int(book_id[2:]))
            except ValueError:
                continue

    return f"BK{highest + 1:04d}"


def add_book():
    books = load_books()

    print("\n--- Add Book ---")

    title = get_text("Book title: ")
    author = get_text("Author name: ")
    quantity = get_positive_integer("Number of copies: ")

    book = {
        "book_id": generate_book_id(books),
        "title": title,
        "author": author,
        "quantity": quantity,
        "available": quantity
    }

    books.append(book)
    save_books(books)

    print("Book added successfully.")
    print(f"Book ID: {book['book_id']}")


def display_book(book):
    print("-" * 40)
    print(f"Book ID   : {book['book_id']}")
    print(f"Title     : {book['title']}")
    print(f"Author    : {book['author']}")
    print(f"Total     : {book['quantity']}")
    print(f"Available : {book['available']}")
    print("-" * 40)


def list_books():
    books = load_books()

    print("\n--- Book Collection ---")

    if not books:
        print("No books have been added.")
        return

    for book in books:
        display_book(book)

    print(f"Total book titles: {len(books)}")


def search_books():
    books = load_books()

    keyword = input(
        "Search by book ID, title, or author: "
    ).strip().lower()

    if not keyword:
        print("Enter a search term.")
        return

    results = [
        book for book in books
        if keyword in book.get("book_id", "").lower()
        or keyword in book.get("title", "").lower()
        or keyword in book.get("author", "").lower()
    ]

    if not results:
        print("No matching books found.")
        return

    for book in results:
        display_book(book)


def find_book(books, book_id):
    for book in books:
        if book.get("book_id", "").upper() == book_id.upper():
            return book

    return None
