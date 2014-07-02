import unittest
import time


class Timer(object):

    def __init__(self, exercises, break_time, time_limit):
        self.original_exercises = exercises
        self.exercises = exercises
        self.break_time = break_time
        self.time_limit = time_limit
        self.current_cycle = -1
        self.set_number = 1 

    def get_current_exercises(self):
        self.current_cycle += 1
        if self.current_cycle == len(self.exercises) - 1:
            self.exercises.append(self.exercises[0])

        return self.exercises[self.current_cycle:self.current_cycle + 2]

    def reset(self):
        self.current_cycle = -1
        self.set_number += 1
        self.exercises = self.original_exercises

    def wait(self, time_delay):
        for i in range (time_delay, 0 , -1):
            print('\t' + str(i), )
            # time.sleep(1)
        return(i) #for testing, make sure it counts down to 1


class TimerTests(unittest.TestCase):

    def test_displays_first_exercises(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        result = timer.get_current_exercises()
        self.assertEqual(['Push Ups', 'Burpees'], result)

    def test_displays_next_exercises(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        timer.get_current_exercises()
        result = timer.get_current_exercises()
        self.assertEqual(['Burpees', 'Pull Ups'], result)

    def test_rolls_over_to_first_on_last_cycle(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        timer.get_current_exercises()
        timer.get_current_exercises()
        result = timer.get_current_exercises()
        self.assertEqual(['Pull Ups', 'Push Ups'], result)

    def test_reset_cycle_for_next_set(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        timer.reset()
        self.assertEqual(timer.current_cycle, -1)

    def test_reset_set_number_for_next_set(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        before_reset_set = timer.set_number
        timer.reset()
        self.assertEqual(timer.set_number, before_reset_set + 1)

    def test_reset_reestablishes_original_exercise_list(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        original_exercises = timer.exercises
        timer.get_current_exercises()
        timer.get_current_exercises()
        timer.get_current_exercises()
        timer.get_current_exercises()
        timer.reset()
        self.assertEqual(original_exercises, timer.exercises)


    def test_end_of_set_triggers_reset(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        timer.get_current_exercises()
        timer.get_current_exercises()
        timer.get_current_exercises()

    def test_wait_counts_down_to_one(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        self.assertEqual(timer.wait(timer.break_time), 1)


