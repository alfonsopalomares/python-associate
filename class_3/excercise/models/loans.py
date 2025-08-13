from models.file import File
import json
from exceptions.exceptions import *
from models.loan import Loan 

class Loans(File):
    loans = []

    def read_all(self):
        lines = super().read_all()
        for item in lines:
            self.loans.append(Loan(**json.loads(item)))
            
        return self.loans
        
        
    def find_object(self, code=None):
        if not code:
            raise NotExistsException
        
        l = self.read_all()
        for item in self.loans:
            if code == item.values["id"]:
                return item
            
        return None
    
    
    def add(self, item):
    
        # maybe we can check if person and book exists in theirs stores...
        # also try to check if the book is not loan at the present
        # etc....
        
        try:
            f = open(self.filename,"a")
            f.write(str(item) + "\n")
            f.close()
        except FileNotFoundError:
            return None
