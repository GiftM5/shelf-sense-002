DATABASE_FILE = "./database/books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        Database = db
        pass  # Ensure the file exists


def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # TODO: Append the book's title and author to the database file
    with open(DATABASE_FILE,"w") as Database:
        Database.write("To Kill a Mockingbird,Harper Lee")

    Database = str(Database)
    Database = Database.split()
    title = Database[0]
    author = Database[1]
    
     

        
print(add_book("To Kill a Mockingbird","Harper Lee"))


def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file

    with open(DATABASE_FILE,"r") as db:
        database = db.readlines

    database = str(database)
        
    lines = database.split(",")
    print(lines)


search_book("To Kill a Mockingbird")



def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries

