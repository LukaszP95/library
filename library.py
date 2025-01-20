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


class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True


    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Book {self.title} {self.author} is borrowed.")
        else:
            print(f"Book {self.title} {self.author} is not available.")

    def return_(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book {self.title} {self.author} is returned.")


class Library:

    def __init__(self):
        self.books = list[Book]()


    def add_books(self, book: Book):
        print(f"Adding book: {book.title} by {book.author}.")
        self.books.append(book)

    def borrow_book(self, book_title: str) -> Book:
        print(f"Attempting to borrow book with title: {book_title}")
        for book in self.books:
            if book.title == book_title and book.is_available:
                print(f"checking book: {book_title} (Available: {book.is_available})")
                book.borrow()
                return book
        print(f"Book {book_title} is not available or does not exist")

    def return_book(self, book_title: str):
        print(f"Attempting to return book with title: {book_title}")
        for book in self.books:
            print(f"checking book: {book_title}")
            if book.title == book_title:
                if not book.is_available:
                    book.return_()
            else:
                print(f"book {book_title} was not borrowed")
                return
        print(f"Book {book_title} does not exist is the library")

    def get_available_books(self) -> list[Book]:
        available_books = [book for book in self.books if book.is_available]
        print(f"Available books: {[book.title for book in available_books]}")
        return available_books

    def filter_books_by_author(self, author: str) -> list[Book]:
        filtered_books = []
        print(f"Attempting to check books by {author}")
        for book in self.books:
            print(f"checking book {book.title} by {author}")
            if book.author == author:
                filtered_books.append(book)
                print(f"book added: {book.title}")
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

    library.borrow_book("Frankenstein")
    print("Borrowing a book: Frankenstein")


    show_books("--- All available books after borrow: ---", library.books)

    library.return_book("Frankenstein")
    print("returning a book: Frankenstein")

    show_books("--- All available books after return: ---", library.books)

if __name__ == '__main__':
    main()

