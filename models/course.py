class Course:
    def __init__(self, name, start_date,end_date,time, duration, capacity, active= True, id = None):
        self.name = name 
        self.start_date = start_date
        self.end_date=  end_date
        self.time = time
        self.duration = duration 
        self.capacity = capacity
        self.active = active 
        self.id = id 




def free_space(self):
    self.capacity -= 1 

    