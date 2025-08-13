import datetime

class Timer:
                    
    def __init__(self, hours, minutes, seconds ):
        try:
            self.datetime = datetime.datetime(1900, 1, 1, int(hours), int(minutes), int(seconds))

        except ValueError:
            self.datetime = datetime.datetime(1900, 1, 1, 0, 0, 0)
            
            print ("Only allow intengers...  ")
            
    def __str__(self):
        return self.datetime.time().__str__()

    def next_second(self):
        self.datetime += datetime.timedelta(seconds=1)
            

    def prev_second(self):
        self.datetime -= datetime.timedelta(seconds=1)


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
