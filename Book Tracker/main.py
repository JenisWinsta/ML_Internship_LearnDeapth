import sqlite3
#database things
connection = sqlite3.connect("books.db")
cursor = connection.cursor()

def add_book():

    print("\n--- Add Book ---")
    title = input("Book title: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()
    total_pages = int(input("Total pages: "))
    rating = int(input("Rating (1-5): "))

    cursor.execute("""
        INSERT INTO books
        (title, date, total_pages, pages_read, rating)
        VALUES (?, ?, ?, ?, ?)
    """, (title, date, total_pages, 0, rating))

    connection.commit()

    print("\nBook added successfully!")

#---------------------------------------------
def update_progress():

    print("\n--- Update Reading Progress ---")
    title = input("Book title: ").strip()
    cursor.execute("""
        SELECT id, total_pages, pages_read
        FROM books
        WHERE title = ?
    """, (title,))

    book = cursor.fetchone()
    if not book:
        print("\nBook not found.")
        return

    book_id, total_pages, current_pages = book

    print(f"\nCurrent progress: {current_pages}/{total_pages}")

    new_pages = int(input("How many pages have you read now? "))

    if new_pages < current_pages:
        print("You cannot reduce your pages read.")
        return

    if new_pages > total_pages:
        print(f"You cannot exceed {total_pages} pages.")
        return

    cursor.execute("""
        UPDATE books
        SET pages_read = ?
        WHERE id = ?
    """, (new_pages, book_id))

    connection.commit()

    progress = new_pages / total_pages * 100

    if new_pages >= total_pages:
        status = "Completed"
    else:
        status = "Reading"

    print("\nReading progress updated!")
    print(f"Pages: {new_pages}/{total_pages}")
    print(f"Progress: {progress:.0f}%")
    print(f"Status: {status}")

# -----------------------------

def dashboard():

    cursor.execute("""
        SELECT title, date, total_pages, pages_read, rating
        FROM books
    """)

    books = cursor.fetchall()

    if not books:
        print("\nNo books found.")
        return

    total_books = len(books)
    completed_books = 0
    reading_books = 0
    total_pages_read = 0

    print("\n" + "=" * 105)
    print("                                READING DASHBOARD")
    print("=" * 105)

    print(
        f"{'Book':<25}"
        f"{'Date':<15}"
        f"{'Pages':<12}"
        f"{'Progress':<12}"
        f"{'Status':<12}"
        f"{'Rating':<10}"
    )

    print("-" * 105)

    for title, date, total_pages, pages_read, rating in books:
        progress = pages_read / total_pages * 100
        if pages_read >= total_pages:
            status = "Completed"
            completed_books += 1
        else:
            status = "Reading"
            reading_books += 1

        total_pages_read += pages_read

        print(
            f"{title:<25}"
            f"{date:<15}"
            f"{str(pages_read) + '/' + str(total_pages):<12}"
            f"{progress:.0f}%{'':<10}"
            f"{status:<12}"
            f"{str(rating) + '/5':<10}"
        )

    print("-" * 105)

    print(f"Total Books:       {total_books}")
    print(f"Completed:         {completed_books}")
    print(f"Currently Reading: {reading_books}")
    print(f"Total Pages Read:  {total_pages_read}")

    print("=" * 105)



# Main Menu
while True:
    print("\n==============================")
    print("     BOOK READING TRACKER")
    print("==============================")

    print("1. Add Book")
    print("2. Update Reading Progress")
    print("3. Dashboard")
    print("4. Exit")

    choice = input("\nChoose: ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        update_progress()
    elif choice == "3":
        dashboard()
    elif choice == "4":
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid choice. Please choose 1-4.")

# Close database
connection.close()