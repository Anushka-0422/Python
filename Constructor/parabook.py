class Book:
    def __init__(self,title,publisher,author):
        self.title = title
        self.publisher = publisher
        self.author = author

    def display(self):
        print("Title of the book : ",self.title)
        print("Publisher of the book : ",self.publisher)
        print("Author of the book : ",self.author)

books = []
for i in range(3):
    print("\n Enter Book info...!!")
    title = input("Enter title of the book : ")
    publisher= (input("Publisher : "))
    author = (input("Author of the book : "))
    book=Book(title,publisher,author)
    books.append(book)

for book in books:
    book.display()