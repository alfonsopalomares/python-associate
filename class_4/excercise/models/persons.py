from models.file import File
import json
from models.person import Person 
from exceptions.exceptions import *

class Persons(File):
    
    def read_all(self):
        lines = super().read_all()
        self.values = []
        for item in lines:
            self.values.append(Person(**json.loads(item)))
            
        return self.values
        
    
    
    
