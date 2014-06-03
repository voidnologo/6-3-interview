import unittest


class Timer(object):

    def __init__(self, exercises):
        self.exercises = exercises
        self.current_cycle = -1

    def get_current_exercises(self):
        self.current_cycle += 1
        if self.current_cycle == len(self.exercises) - 1:
            self.exercises.append(self.exercises[0])

        return self.exercises[self.current_cycle:self.current_cycle + 2]


class TimerTests(unittest.TestCase):

    def test_displays_first_exercises(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'])
        result = timer.get_current_exercises()
        self.assertEqual(['Push Ups', 'Burpees'], result)

    def test_displays_next_exercises(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'])
        timer.get_current_exercises()
        result = timer.get_current_exercises()
        self.assertEqual(['Burpees', 'Pull Ups'], result)

    def test_rolls_over_to_first_on_last_cycle(self):
        timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'])
        timer.get_current_exercises()
        timer.get_current_exercises()
        result = timer.get_current_exercises()
        self.assertEqual(['Pull Ups', 'Push Ups'], result)
