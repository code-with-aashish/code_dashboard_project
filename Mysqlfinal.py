import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime, timedelta

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1122Qwerty@",
    database="LibraryDB"
)
cursor = db.cursor()

# Main window setup
root = tk.Tk()
root.title("Library Management System")

# Function to clear the Treeview and set specific columns for each table
def configure_treeview(columns, headers):
    tree["columns"] = columns
    for col, header in zip(columns, headers):
        tree.heading(col, text=header)
        tree.column(col, anchor="center")

# Function to add a new book
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    genre = genre_entry.get()
    isbn = isbn_entry.get()
    copies = int(copies_entry.get())
    
    if title and author and isbn:
        try:
            cursor.execute("INSERT INTO Books (Title, Author, Genre, ISBN, CopiesAvailable) VALUES (%s, %s, %s, %s, %s)",
                           (title, author, genre, isbn, copies))
            db.commit()
            messagebox.showinfo("Success", "Book added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Warning", "Please fill all required fields.")

# Function to add a new member
def add_member():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    
    if name and email:
        try:
            cursor.execute("INSERT INTO Members (Name, Email, Phone) VALUES (%s, %s, %s)", (name, email, phone))
            db.commit()
            messagebox.showinfo("Success", "Member added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Warning", "Please fill all required fields.")

# Function to issue a book
def issue_book():
    book_id = int(book_id_entry.get())
    member_id = int(member_id_entry.get())
    due_date = datetime.now() + timedelta(days=14)  # 2-week due period

    try:
        # Check availability
        cursor.execute("SELECT CopiesAvailable FROM Books WHERE BookID = %s", (book_id,))
        result = cursor.fetchone()
        
        if result and result[0] > 0:
            # Update transactions and book availability
            cursor.execute("INSERT INTO Transactions (BookID, MemberID, DueDate) VALUES (%s, %s, %s)",
                           (book_id, member_id, due_date))
            cursor.execute("UPDATE Books SET CopiesAvailable = CopiesAvailable - 1 WHERE BookID = %s", (book_id,))
            db.commit()
            messagebox.showinfo("Success", "Book issued successfully!")
        else:
            messagebox.showwarning("Unavailable", "Book is not available.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to return a book
def return_book():
    transaction_id = int(transaction_id_entry.get())

    try:
        # Update return date and book availability
        cursor.execute("UPDATE Transactions SET ReturnDate = %s WHERE TransactionID = %s",
                       (datetime.now(), transaction_id))
        cursor.execute("""
            UPDATE Books 
            JOIN Transactions ON Books.BookID = Transactions.BookID 
            SET CopiesAvailable = CopiesAvailable + 1 
            WHERE Transactions.TransactionID = %s
        """, (transaction_id,))
        db.commit()
        messagebox.showinfo("Success", "Book returned successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to display books
def show_books():
    for row in tree.get_children():
        tree.delete(row)
    configure_treeview(columns=("BookID", "Title", "Author", "Genre", "ISBN", "CopiesAvailable"),
                       headers=("Book ID", "Title", "Author", "Genre", "ISBN", "Copies Available"))
    cursor.execute("SELECT * FROM Books")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)

# Function to display members
def show_members():
    for row in tree.get_children():
        tree.delete(row)
    configure_treeview(columns=("MemberID", "Name", "Email", "Phone", "MembershipDate"),
                       headers=("Member ID", "Name", "Email", "Phone", "Membership Date"))
    cursor.execute("SELECT * FROM Members")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)

# Function to display transactions
def show_transactions():
    for row in tree.get_children():
        tree.delete(row)
    configure_treeview(columns=("TransactionID", "BookID", "MemberID", "IssueDate", "DueDate", "ReturnDate"),
                       headers=("Transaction ID", "Book ID", "Member ID", "Issue Date", "Due Date", "Return Date"))
    cursor.execute("SELECT * FROM Transactions")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)

# GUI Elements
# Labels and entries for adding books
tk.Label(root, text="Title").grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Author").grid(row=1, column=0)
author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1)

tk.Label(root, text="Genre").grid(row=2, column=0)
genre_entry = tk.Entry(root)
genre_entry.grid(row=2, column=1)

tk.Label(root, text="ISBN").grid(row=3, column=0)
isbn_entry = tk.Entry(root)
isbn_entry.grid(row=3, column=1)

tk.Label(root, text="Copies Available").grid(row=4, column=0)
copies_entry = tk.Entry(root)
copies_entry.grid(row=4, column=1)

add_book_btn = tk.Button(root, text="Add Book", command=add_book)
add_book_btn.grid(row=5, column=1)

# Labels and entries for adding members
tk.Label(root, text="Member Name").grid(row=6, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=6, column=1)

tk.Label(root, text="Email").grid(row=7, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=7, column=1)

tk.Label(root, text="Phone").grid(row=8, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=8, column=1)

add_member_btn = tk.Button(root, text="Add Member", command=add_member)
add_member_btn.grid(row=9, column=1)

# Labels and entries for issuing books
tk.Label(root, text="Book ID").grid(row=10, column=0)
book_id_entry = tk.Entry(root)
book_id_entry.grid(row=10, column=1)

tk.Label(root, text="Member ID").grid(row=11, column=0)
member_id_entry = tk.Entry(root)
member_id_entry.grid(row=11, column=1)

issue_book_btn = tk.Button(root, text="Issue Book", command=issue_book)
issue_book_btn.grid(row=12, column=1)

# Labels and entries for returning books
tk.Label(root, text="Transaction ID").grid(row=13, column=0)
transaction_id_entry = tk.Entry(root)
transaction_id_entry.grid(row=13, column=1)

return_book_btn = tk.Button(root, text="Return Book", command=return_book)
return_book_btn.grid(row=14, column=1)

# Display buttons
show_books_btn = tk.Button(root, text="Show Books", command=show_books)
show_books_btn.grid(row=15, column=0)

show_members_btn = tk.Button(root, text="Show Members", command=show_members)
show_members_btn.grid(row=15, column=1)

show_transactions_btn = tk.Button(root, text="Show Transactions", command=show_transactions)
show_transactions_btn.grid(row=15, column=2)

# Treeview for displaying records
tree = ttk.Treeview(root, show="headings")
tree.grid(row=16, column=0, columnspan=3, sticky="nsew")

# Run the main loop
root.mainloop()

# Close database connection on exit
db.close()
