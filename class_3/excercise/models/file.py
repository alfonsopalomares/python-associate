from exceptions.exceptions import *


class File(object):
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
        raise NotImplementedError

    def clear(self):
        try:
            f = open(self.filename,"w")
            f.write()
            f.close()
            return None
        except FileNotFoundError:
            return None

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

    
