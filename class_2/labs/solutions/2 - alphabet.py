class Alphabet:
    def __init__( self ):
        self.current = None
        self.letters = "abcdefghijklmnñopqrstuvwxyz"
        
    def __str__(self):
        if self.current is None:
            return self.current
        else:
            return self.letters[self.current]

    def next(self):
        if self.current is None:
            self.current = 0
        else:
            self.current += 1

        if self.current == len(self.letters):
            self.current = 0
        

    def prev(self):
        if self.current is None:
            self.current = len(self.letters) - 1 
        else:
            self.current -= 1

        if self.current == -1:
            self.current = len(self.letters) - 1

    def __str__(self):
        if self.current is not None:
            return self.letters[self.current]

        return str(self.current)

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

