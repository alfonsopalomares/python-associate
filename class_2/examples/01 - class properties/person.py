class Person:
  surname = "gomez"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

  
  

p1 = Person("Juan", 36)
p2 = Person("Ana", 39)

print(p1.name)
print("%s -> %s" % (p2.name, p2.age))




