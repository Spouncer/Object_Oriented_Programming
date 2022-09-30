'''
Create a class Author and a class Book, 
and add any relevant fields yourself, 
and make getters/setters methods. 
Then make it so you can add books to an author. 
Then make a function in Author so that you can print out all of their books, sorted. 
Also make it so you can figure out the Author from a Book instance.

Then make a class called Library that can include books. 
The Library class must have a function that will print all books from a certain author 
in alphabetical order. Also a function to print out all books, 
first sorted by the name of the author, then by the name of the book.
'''

class Books:
    def __init__(self, name, year, genre, author):
        self.name = name
        self.age = year
        self.genres = [genre]
        self.authors = [author]
        self.copies = 1
        
        if self in author.get_books() == False:
            author.add_book(self)
        
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def add_genre(self, genre):
        self.genres.append(genre)

    def get_genre(self):
        return self.genres

    def list_of_authors(self):
        return sorted(self.authors)

    def add_author(self, author):
        '''author is instance of author class not string'''
        self.authors.append(author)


class Author(Books):
    def __init__(self, name, age, genre):
        super().__init__(name, age, genre)
        self.books = []
        
    def get_books(self):
        return self.books

    def no_of_books(self):
        print(len(self.books))
    
    def no_of_genres(self):
        print(len(self.genres))

    def list_of_books(self):
        return sorted(self.books)

    def list_of_genres(self):
        print(sorted(self.genres))

    def add_book(self, book):
        if book in self.books == False:
            self.books.append(book)
            book.add_author(self)
        else:
            self.copies += 1

        for genre in book.get_genre():

            if genre in self.genres == False:
                self.genres.append(genre)
        

class Library(Author):

    def __init__(self, name, year, genre, author):
        super().__init__(name, year, genre, author)

    def sort_books(self):
        lib = []
        for authors in sorted(self.authors):
            for books in authors.list_of_books():
                lib.append(books)
        print(lib)
        

# Tests

JKRowling = Author('J.K.Rowling', 51, 'Fantasy')
StephenKing = Author('Stephen King', 60, 'Horror')
RoaldDahl = Author('Roald Dahl', 88, 'Childrens')

HarryPotter1 = Books('Harry Potter and the Philosophers Stone', 1997, 'Fantasy', JKRowling)
HarryPotter2 = Books('Harry Potter and the Chamber of Secrets', 1999, 'Fantasy', JKRowling)
HarryPotter3 = Books('Harry Potter and the Prisoner of Askaban', 2001, 'Fantasy', JKRowling)
HarryPotter4 = Books('Harry Potter and the Goblet of Fire', 2003, 'Fantasy', JKRowling)
HarryPotter5 = Books('Harry Potter and the Order of the Pheonix', 2005, 'Fantasy', JKRowling)
HarryPotter6 = Books('Harry Potter and the Half Blood Prince', 2007, 'Fantasy', JKRowling)


It = Books('IT', 1989, 'Horror', StephenKing)
TheShining = Books('The Shining', 1985, 'Horror', StephenKing)
Carrie = Books('Carrie', 1992, 'Horror', StephenKing)

Matilda = Books('Matilda', 1999, 'Childrens', RoaldDahl)
TheBFG = Books('The BFG', 1996, 'Childrens', RoaldDahl)
CharlieAndTheChoc = Books('Charlie and the Chocolate Factory', 2000, 'Childrens', RoaldDahl)

StephenKing.get_books()



