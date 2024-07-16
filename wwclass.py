class student:
    def __init__(self, name:str, std_id:int):
        self.name = name
        self.std_id = std_id
        self.borrowed_books = []

    def borrow_books(self, book_name: str):
        self.borrowed_books.append(book_name)


    def __str__(self):
        return f'Student: {self.name}\t Id: {self.std_id} \t borrowed books: {self.borrowed_books}\n'
    

class library:
    def __init__(self):
        self.books = {}
        self.issued_books = {}
    
# for adding books to library
#    
    def add_books(self, book_name: str):
        if book_name in self.books:
            self.books[book_name] += 1
        else:
            self.books[book_name] = 1

# taking books from library

    def issue_book(self, book_name: str, student):
        if book_name in self.books and self.books[book_name] > 0:
            self.books[book_name] -= 1
            student.borrow_books(book_name)
            if book_name in self.issued_books:
                self.issued_books[book_name] +=1
            else:
                self.issued_books[book_name] =1
            return True
        return False
    



    def __str__(self):
        return f'\nAvailable books: {self.books} \n'
    



    


#Objects:
lib = library()

#ADDING BOOKS TO LIBRARY
lib.add_books("physics")
lib.add_books("physics")
lib.add_books("physics")
lib.add_books("chemistry")
lib.add_books("chemistry")
lib.add_books("chemistry")
lib.add_books("mathematics")
lib.add_books("mathematics")
lib.add_books("mathematics")
lib.add_books("mathematics")


#ATUDENTS DETAILS
st1 = student("Ram", 1)
st2 = student("shyam", 2)


# BOOKS TAKEN BY STUDENTS

lib.issue_book("physics", st1)
lib.issue_book("chemistry", st2)
lib.issue_book("physics", st2)
#lib.take_book("matheamtics", st3)

#SHOWING STUDENT DETAILS 

print(lib)
print(st1)
print(st2)

