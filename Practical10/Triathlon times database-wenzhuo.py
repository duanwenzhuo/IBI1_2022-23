class triathlon (object):
    def __init__(self,firstname,lastname,location,swim_time,cycle_time,run_time):
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time+cycle_time+run_time
    def print_details(self):
        print(a.firstname)
        print(a.lastname)
        print(a.location)
        print(a.swim_time)
        print(a.cycle_time)
        print(a.run_time)
        print(a.total_time)




#example        
a = triathlon('ming','xiao','china',2,2,2)
a.print_details()
