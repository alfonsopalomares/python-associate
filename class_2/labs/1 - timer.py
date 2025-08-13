class Timer:
    def __init__( ??? ):
        #
        # Write code here
        #

    def __str__(self):
        #
        # Write code here
        #

    def next_second(self):
        #
        # Write code here
        #

    def prev_second(self):
        #
        # Write code here
        #


timer = Timer(23, 59, 59)
print(timer)            # 23:59:59
timer.next_second() 
print(timer)            # 0:0:0
timer.prev_second()
print(timer)            # 23:59:59


