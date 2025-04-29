class Person:
    """To implement"""
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def __repr__(self):
        return self.__str__()
antoine = Person("Antoine", "Dupont")
print(antoine)    

class Book:

    def __init__(self, title: str, author: Person):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} ({self.author})"

    def __repr__(self):
        return self.__str__()

novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
print(novel_book)


class LibraryError(Exception):
    """Base class for Library errors"""


class Library:
    def __init__(self, name: str):
        self.name = name
        self._books = []                
        self._members = set()           
        self._borrowed_books = {}       

    def __str__(self):
        return f"{self.name} Library with {len(self._books)} books and {len(self._members)} members."

    def __repr__(self):
        return self.__str__()
    
    def is_book_available(self, book):
        if book not in self._books:
            raise LibraryError(f"Le livre '{book}' n'est pas dans le catalogue.")
        return book not in self._borrowed_books
    
    def borrow_book(self, book, person):
        if person not in self._members:
            raise LibraryError(f"{person} n'est pas membre de la bibliothèque.")
    
        if book not in self._books:
            raise LibraryError(f"Le livre '{book}' n'est pas dans le catalogue.")
    
        if book in self._borrowed_books:
            raise LibraryError(f"Le livre '{book}' est déjà emprunté.")
    
        self._borrowed_books[book] = person

    def return_book(self, book):
        if book not in self._borrowed_books:
            raise LibraryError(f"Le livre '{book}' n'est pas emprunté.")
    
    
        del self._borrowed_books[book]

    def add_new_member(self, person):
        if person in self._members:
           raise LibraryError(f"{person} est déjà membre de la bibliothèque.")
        self._members.add(person)

    def add_new_book(self, book):
        if book in self._books:
           raise LibraryError(f"Le livre '{book}' est déjà dans le catalogue.")
        self._books.append(book)

    def print_status(self):
      print(f"{self.name} status:")
      print(f"Books catalogue: {self._books}")
      print(f"Members: {self._members}")
      available_books = [book for book in self._books if book not in self._borrowed_books]
      print(f"Available books: {available_books}")
      print(f"Borrowed books: {self._borrowed_books}")
      print("-----")

    
def main():
    """Test your code here"""
    library = Library("Public library")

    antoine = Person("Antoine", "Dupont")
    print(antoine)

    julia = Person("Julia", "Roberts")
    print(julia)

    rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "Bb"))
    print(rugby_book)

    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)

    library = Library("Public library")
    library.print_status()

    library.add_new_book(rugby_book)
    library.add_new_book(novel_book)
    library.add_new_member(antoine)
    library.add_new_member(julia)
    library.print_status()

    print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
    library.borrow_book(rugby_book, antoine)
    library.print_status()

    try:
        library.borrow_book(rugby_book, julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(novel_book, Person("Simone", "Veil"))
    except LibraryError as error:
        print(error)

    try:
        library.return_book(novel_book)
    except LibraryError as error:
        print(error)

    library.return_book(rugby_book)
    library.borrow_book(novel_book, julia)
    library.print_status()

    library.borrow_book(rugby_book, julia)
    library.print_status()

if __name__ == "__main__":
    main()
