from models.file import File
import json
from exceptions.exceptions import *
from models.book import Book 

class Books(File):
    
    def read_all(self):
        lines = super().read_all()
        self.values = []
        for item in lines:
            self.values.append(Book(**json.loads(item)))
            
        return self.values
        
   
