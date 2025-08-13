class Alphabet:
    def __init__( ??? ):
        #
        # Write code here
        #

    def __str__(self):
        #
        # Write code here
        #

    def next(self):
        #
        # Write code here
        #

    def prev(self):
        #
        # Write code here
        #

    def __str__(self):
        #
        # Write code here
        #

alpha = Alphabet()
print(alpha) #print current (if not exist, print None)
alpha.next() 
print(alpha) # expected "a" 
alpha.next()
print(alpha) # expected "b"
alpha.prev()
print(alpha) # expected "a"
alpha.prev()
print(alpha) # expected "z"

