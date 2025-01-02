class Publisher:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"and is published by {self.name}")
        
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        print(f"The book titled {self.title} written by {self.author}")
        super().display()

class Python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        super().__init__(name,title,author)
        self.price = price
        self.   pages = no_of_pages

    def display(self):
        super().display()
        print(f"has a price of Rs.{self.price} which contains {self.pages} pages.")
        
python = Python(name = "DC Books",title = "My Python Knowledge",author = "Aaron Gladston",price = 2499.99,no_of_pages = "500")
python.display()
