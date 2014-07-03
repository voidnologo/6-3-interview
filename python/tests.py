import unittest
from timer import Timer

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


    def test_end_of_set_returns_true_if_end_of_set(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        timer.current_cycle = len(timer.exercises) - 1
        self.assertTrue (timer.end_of_set())    

    def test_end_of_set_returns_false_if_not_end_of_set(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        # timer.current_cycle = 1
        self.assertFalse (timer.end_of_set())

    def test_wait_counts_down_to_one(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=10, time_limit=60)
        self.assertEqual(timer.wait(3), 1)


