import sqlite3

# create a connection to the database
conn = sqlite3.connect('ebookstore.db')

# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE books (
        id INT,
        title TEXT,
        author TEXT,
        qty INTEGER
)""")

# populate the table with the current books. This is done by creating a list with tuples carrying book entries inside
current_books = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
                 (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling',40 ),
                 (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
                 (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
                 (3005, 'Alice in Wonderland', 'Lewis Carroll', 12),
]

# insert the info into multiple rows at once with this step
c.executemany("INSERT INTO books VALUES (?,?,?,?)", current_books)

while True:
    # present user with a menu
    menu = int(input("What would you like to do ?:\n1.Enter book \n2.Update book \n3.Delete book \n4.Search books  \n0.Exit\n"))

    if menu == 1:
        # ask user to for the book details:
        book_id = int(input("Please enter the book's id: "))
        book_title = input("Please enter the book's title: ")
        book_author = input("Please enter the book author's name: ").title()
        quantity = int(input("Please enter the quantity of the books: "))

        # the variables containing the variables with the user's input 
        book_entry = [(book_id), (book_title), (book_author), (quantity),]
        # enter the book's info to the database using INSERT command.
        query1 = c.execute("INSERT INTO books VALUES (?,?,?,?)", book_entry)

    elif menu == 2 :
        # user is provided with the option of updating the quantity as this value is most likely to change
        book_id = int(input("Enter the ID of the book you'd like to update: "))
        # to check if the book id exists in the table
        c.execute("SELECT *FROM books WHERE id = ?",[book_id])
        # returns a list of the results from the select statement above
        data = c.fetchall()
        # to access the id from the list of tuples that was returned, using a for loop and indexing was used at position 0 of the tuple 
        print(data)
        for i in data:
            print(i[0])
            if i[0] == book_id:
                print('Book ID match found. Proceeding to UPDATE',i[0])
                new_quant = int(input("Enter the new quantity of the books: "))
                # variables are stored as tuples to be used in the query statement
                updated = (new_quant,book_id)
                c.execute("UPDATE books SET qty = ? WHERE id = ? ",updated)
            else:
                print('Book ID not found')
                
        
    elif menu == 3:
        # user can delete the book by referencing the book ID
        book_id = int(input("Enter the ID of the book you'd like to delete: "))
        # to check if the id exists in the table
        c.execute("SELECT *FROM books WHERE id = ?",[book_id])
        # returns a list of the results from the select statement above
        data = c.fetchall()
        # to access the id from the list of tuples that was returned, using a for loop and indexing was used at position 0 of the tuple 
        print(data)
        for i in data:
            print(i[0])
            if i[0] == book_id:
                print('Book ID match found. Proceeding to delete',i[0])
                delete_query = c.execute("DELETE FROM books WHERE id =?",[book_id])
            else:
                print('Sorry book id not found.')

    elif menu == 4:
        # user is given an option to search using either id, title or author of the book:
        search_by = int(input("Would you like to search by 1.author, 2.title or 3.id?: "))
        if search_by == 1:
            author = input('Please enter the book author to begin your search: ').title()
            print(author)
            c.execute("SELECT *FROM books WHERE author = ?", [author])
            search_data = c.fetchall()
            print('Author found:', search_data)

        elif search_by == 2:
            book_title = input('Please enter the book title to begin your search: ')
            print(book_title)
            c.execute("SELECT *FROM books WHERE title = ?", [book_title])
            search_data = c.fetchall()
            print('Book title found:', search_data)

        elif search_by == 3:
            book_id = int(input("Enter the ID of the book you'd like to search for: "))
            # to check if the id exists in the table
            c.execute("SELECT *FROM books WHERE id = ?",[book_id])
            # returns a list of the results from the select statement above
            data = c.fetchall()
            # to access the id from the list of tuples that was returned, using a for loop and indexing was used at position 0 of the tuple 
            print(data)

    elif menu == 0:
        print('Goodbye!')
        exit()

    # commit changes
    conn.commit()
    