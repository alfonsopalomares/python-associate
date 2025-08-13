from exceptions.exceptions import *


class File(object):
    values = []

    def __init__(self, filename):
        self.filename = filename
        

    def read_all(self):
        l = []
        try:
            f = open(self.filename, "r")
            l = f.readlines()
            f.close()
            return l
        except FileNotFoundError:
            return l
            
    
    def find_object(self, code=None):
        if not code:
            raise NotExistsException
        
        l = self.read_all()
        for item in self.values:
            if code == item.values["id"]:
                return item
            
        return None

    def clear(self):
        try:
            f = open(self.filename,"w")
            f.write("")
            f.close()
            return None
        except FileNotFoundError:
            return None

    def save(self):
        try:
            f = open(self.filename,"w")
             
        except FileNotFoundError:
            return None
            
        for obj in self.values:
            f.write(str(obj) + "\n")
            
        f.close()
        
        
    def add(self, item):
        if "id" not in item.values.keys():
            raise NotExistsException("id is not present")
            
        if self.find_object(item.values["id"]):
            raise AlreadyExistsException("id is already present into database")
            
        try:
            f = open(self.filename,"a")
            f.write(str(item) + "\n")
            f.close()
        except FileNotFoundError:
            return None

    def delete(self, id):
        objs = self.read_all()
        for obj in self.values:
            if obj.values["id"] == id:
                objs.remove(obj)
            
        self.values = objs
         
        self.clear()
        self.save()
        
    def update(self, item):
        if "id" not in item.values.keys():
            raise NotExistsException("id is not present")
        
        self.delete(item.values["id"])
        self.add(item)
        