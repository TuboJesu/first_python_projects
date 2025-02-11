
book_repository = [{
    "Title": "Sunday School Manual", 
    "Author": "RCCG", 
    "Year of Publication": 2024, 
    "ISBN": 1201508, 
    "Available": True },

    {
    "Title": "Bible Study Manual", 
    "Author": "RCCG", 
    "Year of Publication": 2025, 
    "ISBN": 1201497, 
    "Available": True }]

def add_book():

    book_details = {}

    book_title = input("Enter a book title : ")
    author = input("Enter the Author name: ")
    year_of_publication = int(input("Enter the year of publication: "))
    book_isbn = int(input("Enter the ISBN: "))

    book_details["Title"] = book_title
    book_details["Author"] = author
    book_details["Year of Publication"] = year_of_publication
    book_details["ISBN"] = book_isbn
    book_details["Available"] = True
    
    book_repository.append(book_details) 
    return "Book added sucessfully"


def view_books():
    for index, books in enumerate(book_repository, start=1):
        print(f" {index} -- {books}")
    
    return""


def update_book(isbn):

    def update_title(updated_title):
        book["Title"] = updated_title
    
    def update_author(updated_author):
        book["Author"] = updated_author
    
    def update_yop(updated_yop):
        book["Year of Publication"] = updated_yop
    
    def update_isbn(updated_isbn):
        book["ISBN"] = updated_isbn

    def update_all_details(all_updated_title, all_updated_author, all_updated_yop, all_updated_isbn):
        book["Title"] = all_updated_title
        book["Author"] = all_updated_author
        book["Year of Publication"] = all_updated_yop
        book["ISBN"] = all_updated_isbn

    for book in book_repository:
       if book["ISBN"] == isbn:
            
            print(f"current details: {book}")
            while True:

                print('''
                        
SELECT 1 to Update the title
SELECT 2 to Update the author
SELECT 3 to Update the year of publication
SELECT 4 to Update the ISBN
SELECT 5 to Update all
SELECT 6 to Quit
                        
''')
                update_selection = input("Select an operation from 1 - 6: ")

                if book["Available"] == False:
                    print(f"{book["Title"]} is not available")
                    break
                
                if update_selection == "6":
                    break

                if update_selection == "1":
                    new_title = input("Enter the book title : ")
                    update_title(new_title)

                elif update_selection == "2":
                    new_author = input("Enter the book author : ")
                    update_author(new_author)
                
                elif update_selection == "3":
                    new_yop = input("Enter the book Year of Publication : ")
                    update_yop(new_yop)
                
                elif update_selection == "4":
                    new_isbn = input("Enter the book ISBN : ")
                    update_isbn(new_isbn)
                
                elif update_selection == "5":
                    all_new_book_title = input("Enter a book title : ")
                    all_new_author = input("Enter the Author name: ")
                    all_new_yop = int(input("Enter the year of publication: "))
                    all_new_book_isbn = int(input("Enter the ISBN: "))
                    update_all_details(all_new_book_title, all_new_author, all_new_yop, all_new_book_isbn)

                else:
                    print("Only pick an option from 1 to 6.")
                
                return "Book Updated Successfully"


def delete_book(isbn):
    for index, book in enumerate(book_repository):
        if book["ISBN"] == isbn:
            book_repository.pop(index)
            return "Deleted Successfully..."

def search_book(title):
    for index, book in enumerate(book_repository):
        if book["Title"] == title:
            return f" {index + 1} - {book}"


def borrow_book(isbn):
    for book in book_repository:
        if book["ISBN"] == isbn:
            if book["Available"] == True:
                book["Available"] = False
                return f"The book '{book['Title']}' has been successfully borrowed"
            else:
                return "The book is not available for borrowing"
    return "Book not found"

def return_book(isbn):
    for book in book_repository:
        if book["ISBN"] == isbn:
            if book["Available"] == False:
                book["Available"] = True
                return f"The book '{book['Title']}' has been successfully returned"
            else:
                return "The book was never borrowed"
    return "Book not found"
   


# MAIN OPERATIONS


while True:

    print('''

Select 1 to add a new book to the library.
Select 2 to display all the books in the library.
Select 3 to update the information of a book given its ISBN.
Select 4 to remove a book from the library using its ISBN.
Select 5 to search for a book by its exact title.
Select 6 borrow_book(isbn): Mark a book as borrowed (not available).
Select 7 return_book(isbn): Mark a book as returned (available).
Select 8 to quit
        

''')

    user_inputs = input("Select an Operation from 1- 8: ")

    if user_inputs == "8":
        break

    if user_inputs == "1":
        print(add_book())

    elif user_inputs == "2":
         print(view_books())

    elif user_inputs == "3":
        search_with_isbn = int(input("Enter the ISBN of the book you want to update: "))
        print(update_book(search_with_isbn))

    elif user_inputs == "4":
        book_delete_search = int(input("Enter the ISBN of the book you want to delete: "))
        print(delete_book(book_delete_search))

    elif user_inputs == "5":
        book_search = (input("Enter the title of the book you want to search for: "))
        print(search_book(book_search))
    
    elif user_inputs == "6":
        borrow_with_isbn = int(input("Enter the ISBN of the book you want to borrow: "))
        print(borrow_book(borrow_with_isbn))

    elif user_inputs == "7":
        return_with_isbn = int(input("Enter the ISBN of the book you want to return: "))
        print(borrow_book(return_with_isbn))
    
    else:
        print("Error!!!... only select from 1 - 8")

    