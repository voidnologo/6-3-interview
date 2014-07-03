from timer import Timer


print """
   Exercises: "push ups", "burpees", "pull ups"
   Time Limit: 60
   Break Time: 10
   Sets: 2
"""

timer = Timer(exercises=['Push Ups', 'Burpees', 'Pull Ups'], break_time=3, time_limit=5)
num_of_sets = 2


while (timer.set_number <= num_of_sets):
   print ("BREAK! Up Next:")
   current_exercises = timer.get_current_exercises()
   print ("Person 1: " + current_exercises[0])
   print ("Person 2: " + current_exercises[1])
   timer.wait(timer.break_time)
   print ("Person 1: " + current_exercises[0])
   print ("Person 2: " + current_exercises[1])
   timer.wait(timer.time_limit)
   if timer.end_of_set():
      # print ("IN END OF SET: " + str(timer.set_number) + "  " + str(timer.current_cycle))
      print ("\n\n*** END OF SET : " + str(timer.set_number) + "\n\n")
      timer.reset()
   # else:
      # print ("NOT END OF SET: "  + str(timer.set_number) + "  " + str(timer.current_cycle))