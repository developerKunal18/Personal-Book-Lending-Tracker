# Personal Book Lending Tracker

A simple Python application for maintaining a personal book collection and tracking books lent to friends, classmates, or colleagues.

## Features

- Add and search books
- Track book quantities and availability
- Lend books and record borrower details
- Record expected return dates
- Process book returns
- View borrowing history
- Search borrower history
- Identify overdue books
- Generate lending and popular-book reports
- Store records in JSON files

## Technologies Used

- Python 3
- JSON
- datetime
- collections

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Personal-Book-Lending-Tracker.git
```

Open the project folder:

```bash
cd Personal-Book-Lending-Tracker
```

Run the application:

```bash
python main.py
```

No external packages are required.

## Project Structure

```text
Personal-Book-Lending-Tracker/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── book_manager.py
├── lending_manager.py
├── report_manager.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    ├── books.json
    └── lending_records.json
```

## How to Use

1. Add a book to your collection.
2. Use the generated book ID to lend a copy.
3. Enter the borrower's name and optional phone number.
4. Record the lending ID.
5. Use the lending ID to process the return.
6. Review the overdue report and lending summary.

The default lending period is 14 days.

## Learning Outcomes

- Functions and modules
- Lists and dictionaries
- JSON file handling
- Date calculations
- Searching and filtering
- Counters and report generation
- Menu-driven application development

## Future Improvements

- Add a graphical user interface
- Integrate SQLite or MySQL
- Send return-date reminders
- Export lending history to CSV
- Add borrower contact management

## Author

Python Project Challenge 

## License

Free to use for educational and personal learning purposes.
