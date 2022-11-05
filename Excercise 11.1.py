"""
Implement the following class hierarchy using Python: A publication can be either a book or a magazine.
Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
Also write the required initializers to both classes.
Create a print_information method to both subclasses for printing out all information of the publication in question.
In the main program, create publications Donald Duck (chief editor) and Compartment No. 6 (author Rosa Liksom, 192 pages).
Print out all information of both publications using the methods you implemented.
"""

class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"this publication is {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"The author of the book is {self.author} and the book has {self.page_count} pages")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"The chief editor of the magazine is {self.chief_editor}")

publication = []

publication.append(Book("Compartment No. 6", "Rosa Liksom", 192))
publication.append(Magazine("Donald Duck", "Aki Hyyppä"))

for p in publication:
    p.print_info()

