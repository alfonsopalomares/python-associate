from models.file import File
import json
from exceptions.exceptions import *
from models.book import Book 

class Books(File):
    books = []

    def read_all(self):
        lines = super().read_all()
        for item in lines:
            self.books.append(Book(**json.loads(item)))
            
        return self.books
        
    

    
    def find_object(self, code=None):
        if not code:
            raise NotExistsException
        
        l = self.read_all()
        for item in self.books:
            if code == item.values["id"]:
                return item
            
        return None
    
    
