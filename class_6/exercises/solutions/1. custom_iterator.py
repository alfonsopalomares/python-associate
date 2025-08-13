
# 1. create a your custom iterator to retrieve power of two number. Parameters: initial, end, exponent (is not valid if you use a yield)
# example 1:
# for a in mi_power(1, 5, 2):
#   print (a)

## expected result:
## 1
## 4
## 9
## 16


# example 2:
# for a in mi_power(2, 6, 3):
#   print (a)

## expected result:
## 8
## 27
## 64
## 125


class MiPower:
    def __init__(self, _from, to, power):
        self.__n = to
        self.__i = _from - 1
        self.power = power 

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i >= self.__n:
            raise StopIteration

        return self.__i ** self.power
    

object = MiPower(1, 5, 2)

for i in object:
    print(i)


object = MiPower(2, 6, 3)

for i in object:
    print(i)

