
# 2. Adapt the iterator from excercise 1 to be a generator
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

def mi_power(f, t, p):
  for i in range(f, t):
    yield i ** p

powers = list(mi_power(1, 5, 2))
print(powers)

powers2 = list(mi_power(2, 6, 3))
print(powers2)



