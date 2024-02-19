class Library:
    def __init__(self, file_path="books.txt"):
        self.file_path = file_path
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def addBook(self, bookName, author, releaseDate, number_of_pages):
        self.file.write(f"{bookName},{author},{releaseDate},{number_of_pages}\n")

    def listBooks(self):
        print("\nBooks in the library:\n ")
        self.file.seek(0)
        print(self.file.read())

    def removeBook(self, bookName):
        self.file.seek(0)
        lines = self.file.readlines()

        self.file.truncate(0)
        for line in lines:
        # Check if the given bookName is not in the current line
            if bookName not in line:
            # If the bookName is not found in the line, write it back to the file
                self.file.write(line)


        self.file.seek(0, 2)


library = Library()

def menu():
    print("\n1- Add a book")
    print("2- List books")
    print("3- Remove a book")
    print("4- Exit")
    choice = input("Enter your choice: ")
    return choice

while True:
    choice = menu()
    if choice == "1":
        bookName = input("\nEnter the book name: ")
        author = input("Enter the author: ")
        releaseDate = input("Enter the release date: ")
        number_of_pages = input("Enter the number of pages: ")
        library.addBook(bookName, author, releaseDate, number_of_pages)
    elif choice == "2":
        library.listBooks()
    elif choice == "3":
        bookName = input("Enter the book name: ")
        library.removeBook(bookName)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
        continue
