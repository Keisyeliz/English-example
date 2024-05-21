library = []
sw = True

import os
def clear_screen():
    os.system('cls')
    print('Author: ✮ Keisy Murillo ✮')
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    book = {"title": title, "author": author}
    library.append(book)
    print("Book added successfully.")

def remove_book():
    title = input('Enter the title of the book to remove: ')
    for book in library:
        if book["title"] == title:
            library.remove(book)
            print("Book removed successfully.")
            return
    print("The book is not in the library.")

def show_books():
    if not library:
        print("The library is empty.")
    else:
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}")

while sw == True:
    print('\nLibrary')
    option = input('--Menu Options--\n\n1. Add\n2. Remove\n3. Show\n4. Exit\n->')

    if option == '1':
        clear_screen()
        add_book()
    elif option == '2':
        remove_book()
    elif option == '3':
        clear_screen()
        show_books()
    elif option == '4':
        clear_screen()
        print("Goodbye!")
        sw = False
    else:
        print("Invalid option. Please try again.")
