class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def set_surname(self, surname):
    self.surname = surname

  def get_surname(self):
    return self.surname


  def __str__(self):
    s = "%s %s --> age: %s"
    if "surname" in self.__dict__:
        return s % (self.name, self.surname, self.age)

    return s % (self.name, "", self.age)
    

p1 = Person("Juan", 36)
p2 = Person("Ana", 39)

print(p1.name)
print("%s -> %s" % (p2.name, p2.age))

p1.set_surname("gomez")

print(p1.get_surname())

print ("use the str function")

print(p1)
print(p2)


