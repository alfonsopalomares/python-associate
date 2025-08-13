from models.myobject import MyObject

class Loan(MyObject):
    
    def __str__(self):
        r = []
        for key in self.values.keys():
            r.append(str(self.values[key]))
            
        return "|".join(r)
        

