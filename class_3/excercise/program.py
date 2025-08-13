from models.person import Person
from models.persons import Persons
from models.book import Book
from models.books import Books
from models.loan import Loan
from models.loans import Loans
import os

PEOPLE = os.getcwd() + "/data/p.txt"
BOOKS = os.getcwd() + "/data/b.txt"
LOANS = os.getcwd() + "\data/l.txt"

ps = Persons(PEOPLE)
books = Books(BOOKS)
loans = Loans(LOANS)

p1 = Person(name="alfonso", lastname="palomares", id=1)
p2 = Person(name="Ana", lastname="Lopez", id=2)
p3 = Person(name="Lorena", lastname="Gonzalez", id=3)
p4 = Person(name="Juan", lastname="Rodriguez", id=4)

b1 = Book (id=1, name="Frankenstein",  author="Mary Shelley", Country="United Kingdom")
b2 = Book (id=2, name="L2",  author="A2", Country="ARG")
b3 = Book (id=3, name="L3",  author="A3", Country="ARG")
b4 = Book (id=4, name="L4",  author="A4", Country="URU")

ps.add(p1)
ps.add(p2)
ps.add(p3)
ps.add(p4)

books.add(b1)
books.add(b2)
books.add(b3)
books.add(b4)

l1 = Loan(person=p1, book=b1, id=3)
loans.add(l1)

people = ps.read_all()
for p in people:
    print(p)
 

for i in books.read_all():
    print (i)
    


