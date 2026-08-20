# Book Reading Tracker

## Problem Statement
Tracking reading progress manually can be inconvenient and makes it difficult to see overall reading progress.

## Objective
To build a simple Python-based reading tracker that stores book information in SQLite and allows users to update and monitor their reading progress.

## Features
*   Add new books 
*   Store book title, date, total pages, pages read, and rating
*   Update reading progress
*   Automatically calculate reading percentage
*   Automatically determine reading status
*   Display a dashboard with all books
*   Track completed and currently reading books
    

## Technologies Used
*   Python
*   SQLite
*   DB Browser for SQLite

## Installation / Setup
1.  Install Python 3.
2.  Install DB Browser for SQLite (optional, for viewing the database).
3.  Clone or download the project.
4.  Make sure books.db is in the project directory.
5.  No additional Python libraries are required.

## How to Run
Run the following command from the project directory:

   ```python main.py```

Follow the menu options to add books, update reading progress, and view the dashboard.

## Project Structure

```text
Book_Tracker/
├── main.py       # Main Python application
├── books.db      # SQLite database
└── README.md     # Project documentation
```

## Testing
The project was tested by:
*   Adding multiple books
*   Updating pages read
*   Checking progress calculations 
*   Checking automatic Reading/Completed status
*   Verifying data in SQLite using DB Browser
    

## Limitations
*   Only one reading progress value is stored for each book.
*   Book titles must be entered consistently when updating progress. 
*   Input validation is currently basic.

## Future Improvements
*   Add a graphical/web interface using HTML and CSS
*   Add search and filtering
*   Add book deletion and editing
*   Improve input validation and error handling
