from models.file import File
import json
from models.person import Person 
from exceptions.exceptions import *


class Persons(File):
    persons = []

    def read_all(self):
        lines = super().read_all()
        for item in lines:
            self.persons.append(Person(**json.loads(item)))
            
        return self.persons
        
    
    def find_object(self, code=None):
        if not code:
            raise NotExistsException
        
        l = self.read_all()
        for item in self.persons:
            if code == item.values["id"]:
                return item
            
        return None
    
    
