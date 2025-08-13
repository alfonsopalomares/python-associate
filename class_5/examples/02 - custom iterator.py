class Prime:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.v = 1

    def __iter__(self):
        print("Prime iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration

        print ("iteration %s" % self.__i) 
        if self.__i ==  1:
            return self.v
    
        while True:
            self.v += 1
            cant = 0
            for i in range(self.v, 0, -1):
                if self.v % i == 0:
                    cant += 1
            if cant == 2:
                break

        return self.v
                
        
class Class:
    def __init__(self, n):
        self.__iter = Prime(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter;


object = Prime(8)

for i in object:
    print(i)
