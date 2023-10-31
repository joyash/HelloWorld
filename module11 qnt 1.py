class Publication:

    def __init__(self, publication_name, chief_editor):
        self.publication_name = publication_name
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Publication name is: {self.publication_name}. The Chief Editor is: {self.chief_editor}")


class Book(Publication):

    def __init__(self, author, page_count, publication_name, chief_editor):
        self.author = author
        self.page_count = page_count
        super().__init__(publication_name, chief_editor)

    def print_information(self):
        super().print_information()
        print(f"The author of the book is: {self.author}. Number of pages in book is: {self.page_count}")


book1 = Book("Roman", 102, "Oxford", "Alex")

book1.print_information()
"""print(f"Publication name is: {book1.publication_name} and the Chief Editor name is: {book1.chief_editor} The author of the book is: {book1.author} and number of pages in the book is: {book1.page_count}.")"""
