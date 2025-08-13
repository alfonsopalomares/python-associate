class Timer:

    def validate(self):
        if self.hours > 23 or self.hours < 0:
                print ("hora incorrecta...")
                self.hours = 0

        if self.minutes > 59 or self.minutes < 0:
            print ("minutes incorrecta...")
            self.hours = 0

        if self.seconds > 59 or self.seconds < 0:
            print ("seconds incorrecta...")
            self.hours = 0

                
    def __init__(self, hours, minutes, seconds ):
        try:
            self.hours = int(hours)
            self.minutes = int(minutes)
            self.seconds = int(seconds)

            self.validate()            
            
        except ValueError:
            self.hours = None
            self.minutes = None
            self.seconds = None
            
            print ("Only allow intengers...")
            
    def __str__(self):
        return "%s:%s:%s" % (self.hours, self.minutes, self.seconds)

    def next_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1

        if self.hours == 24:
            self.hours = 0
            

    def prev_second(self):
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds = 59
            self.minutes -= 1

        if self.minutes == -1:
            self.minutes = 59
            self.hours -= 1

        if self.hours == -1:
            self.hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
