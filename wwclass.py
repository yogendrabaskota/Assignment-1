class library:
    def __init__(self):
        self.books = {}
        self.issued_books = {}
    
    def add_books(self, book_name: str):
        if book_name in self.books:
            self.books[book_name] += 1
        else:
            self.books[book_name] = 1



    def __str__(self):
        return f'Available books: {self.books} \n'
    



class student:
    def __init__(self, name:str, std_id:int):
        self.name = name
        self.std_id = std_id
        self.borrowed_books = []

    def borrow_books(self, book_name: str):
        self.borrowed_books.append(book_name)


    def __str__(self):
        return f'Student: {self.name}\t Id: {self.std_id} \t borrowed books: {self.borrow_books}'
        


#Objects:
lib = library()

lib.add_books("physics")
lib.add_books("chemistry")
lib.add_books("matheamtics")

st1 = student("Ram", 1)
st2 = student("shyam", 2)


# student details of library

print(lib)
print(st1)
print(st2)

