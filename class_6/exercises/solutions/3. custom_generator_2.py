
# 3. write a steps generator. 

# example 1:
# for a in steps(5):
#   print (a)

## expected result:
## left
## right
## left
## right


# example 2:
# for a in steps(4):
#   print (a)

## expected result:
## left
## right
## left

# example 3:
# for a in steps(4, "right"):
#   print (a)

## expected result:
## right
## left
## right

# example 4:
# for a in steps(7, "left"):
#   print (a)

## expected result:
## left
## right
## left
## right
## left
## right8

def steps(n, foot="left"):
  foots = ["left", "right"] if foot=="left" else ["right", "left"]
  for i in range(n-1):
    yield foots[0] if i % 2 == 0 else foots[1]
    

walk = list(steps(5))
print(walk)

walk = list(steps(4))
print(walk)


walk = list(steps(4, "right"))
print(walk)

walk = list(steps(7, "left"))
print(walk)

