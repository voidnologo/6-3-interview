import time


class Timer(object):

    def __init__(self, exercises, break_time, time_limit):
        self.original_exercises = exercises
        self.exercises = exercises
        self.break_time = break_time
        self.time_limit = time_limit
        self.current_cycle = -1
        self.set_number = 1 
        self.set_end = len(self.exercises) - 1

    def get_current_exercises(self):
        self.current_cycle += 1
        if self.current_cycle == self.set_end:
            self.exercises.append(self.exercises[0])

        return self.exercises[self.current_cycle:self.current_cycle + 2]

    def reset(self):
        self.current_cycle = -1
        self.set_number += 1
        self.exercises = self.original_exercises

    def end_of_set(self):
        if self.current_cycle >= self.set_end:
            return True
        else:
            return False

    def wait(self, time_delay):
        for i in range (time_delay, 0 , -1):
            print str(i)
            time.sleep(1)
        return(i) #for testing, make sure it counts down to 1
