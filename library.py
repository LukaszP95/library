"""Klasa Book:

Pola:
title (str) – tytuł książki,
author (str) – autor książki,
is_available (bool, domyślnie True) – czy książka jest dostępna.
Metody:
borrow() – zmienia status dostępności książki na False.
return_() – zmienia status dostępności książki na True.
Wyjątki:

Stwórz hierarchię wyjątków związanych z błędami w systemie:
Klasa bazowa: BookError z polem message.
Wyjątek BookNotFound – zgłaszany, gdy książka o podanym tytule nie istnieje.
Wyjątek BookNotAvailable – zgłaszany, gdy książka o podanym tytule jest już wypożyczona.
Wyjątek BookAlreadyReturned – zgłaszany, gdy książka o podanym tytule jest już zwrócona.

---Klasa Library:

Pola:
books (list[Book]) – lista książek w bibliotece.
Metody:
add_book(book: Book) – dodaje książkę do biblioteki.
borrow_book(book_title: str) -> Book – wypożycza książkę na podstawie jej tytułu, jeśli jest dostępna.
return_book(book_title: str) – zwraca książkę do biblioteki na podstawie jej tytułu.
get_available_books() -> list[Book] – zwraca listę książek dostępnych do wypożyczenia.
filter_books_by_author(author: str) -> list[Book] – zwraca listę książek napisanych przez podanego autora.
Funkcje Pomocnicze:

show_books(message: str, books: list[Book]) – wyświetla listę książek wraz z wiadomością (tytuł, autor, status dostępności).
Główna Funkcja main():

Wykorzystaj klasę Library i zaimplementowane metody do stworzenia przykładowej interakcji:
Dodaj książki do biblioteki.
Wyświetl dostępne książki.
Wypożycz i zwróć książkę.
Obsłuż wyjątki, takie jak wypożyczenie niedostępnej książki lub zwrot książki, która nie była wypożyczona."""



class BookError(Exception):

    def __init__(self):
        self.message = 'Book has not found.'


class BookNotFound(BookError):
    
    def __init__(self):
        self.message = 'Book has not found.'


class BookNotAvailable(BookError):

    def __init__(self):
        self.message = 'Book is not available.' 


class BookAlreadyReturned(BookError):

    def __init__(self):
        self.message = 'Book is already returned.' 


class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        self.is_available = False

    def return_(self):
        self.is_available = True


class Library:

    def __init__(self):
        self.books: list[Book] = []

    def add_books(self, book: Book):
        self.books.append(book)

    def borrow_book(self, book_title: str):
        
        for book in self.books:

            if book.title == book_title:

                if book.is_available:
                    book.borrow()
                    return
                
                else:
                    raise BookNotAvailable

        raise BookNotFound

    def return_book(self, book_title: str):

        for book in self.books:

            if book.title == book_title:

                if not book.is_available:
                    book.return_()
                    return 
                
                else:
                    raise BookAlreadyReturned
                
        raise BookNotFound

    def get_available_books(self) -> list[Book]:
        available_books = [book for book in self.books if book.is_available]
        return available_books

    def filter_books_by_author(self, author: str) -> list[Book]:
        filtered_books = []
        for book in self.books:
            if book.author == author:
                filtered_books.append(book)
        return filtered_books


def show_books(message: str, books: list[Book]):
    print(message)

    for book in books:
        availability = "available" if book.is_available else "not available"
        print(f"title: {book.title}, author: {book.author}, status: {availability}")


def main():

    library = Library()

    book1 = Book("No Longer Human", "Osamu Dazai")
    book2 = Book("Robinson Crusoe", "Daniel Defoe")
    book3 = Book("Frankenstein", "Marry Shelley")

    library.add_books(book1)
    library.add_books(book2)
    library.add_books(book3)

    show_books("--- All available books at beginning: ---", library.books)

    try:

        library.borrow_book("Frankenstein")
        library.return_book("Frankenstein")

    except BookError as e:
        print(e.message)
        return

    show_books("--- All available books after return: ---", library.books)

if __name__ == '__main__':
    main()


