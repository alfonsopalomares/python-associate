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
    
class Student(Person):
  pass


class Teacher(Person):
  def __init__(self, name, age, initial_year):
    super().__init__(name, age)
    self.year = initial_year

  def welcome(self):
    print("Im the teacher: ", self.name)


p1 = Person("Juan", 36)
s1 = Student("Ana", 39)
t1 = Teacher("Ale", 25, 2000)

print(p1.name)
print("%s -> %s" % (s1.name, s1.age))

p1.set_surname("gomez")
s1.set_surname("rodriguez")

print(p1.get_surname())

print ("use the str function")

print(p1)
print(s1)
print(t1)
print(t1.welcome())



