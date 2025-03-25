

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f'Book(title = {self.title}, author = {self.author})'
    
    def update_info(self, title: str=None, author: str=None):
        if title:
            self.title = title
        if author:
            self.author = author


Book_1 = Book("Evgeniy Onegin", "A.S.Pushkin")
print(Book_1)
Book_1.update_info(author='Pushkin A.S.')
print(Book_1)
 

class User: 
    def __init__(self, name: str, mail: str):
        self.name = name
        self.mail = mail

    def __str__(self):
        return f'User(name = {self.name}, mail = {self.mail})'
    
    def update_info(self, name: str=None, mail: str=None):
        if name:
            self.name = name
        if mail:
            self.mail = mail

            7
User_1 = User("Dima", "d@gmail.com")
print(User_1)
User_1.update_info(name='DDima')
print(User_1)


