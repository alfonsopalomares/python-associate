def Prime(n):
    v = 1
    for i in range(n):
        print ("iteration %s" % i) 
        if i ==  0:
            yield v
        else:
            while True:
                v += 1
                cant = 0
                for i in range(v, 0, -1):
                    if v % i == 0:
                        cant += 1
                if cant == 2:
                    break

            yield v
                
       
for i in Prime(25):
    print(i)
