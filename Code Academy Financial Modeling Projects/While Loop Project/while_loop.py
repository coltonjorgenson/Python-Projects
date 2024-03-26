# While Loop Walkthrough
# count = 0
# print("Starting While Loop")
# while count <= 3:
#   # Loop Body
#   # Print if the condition is still true
#   print("Loop Iteration - count <= 3 is still true")
#   # Print the current value of count 
#   print("Count is currently " + str(count))
#   # Increment count
#   count += 1
#   print(" ----- ")
# print("While Loop ended")

# Your code below: 
# A variable to keep track of the count, and also help our loop eventually stop.
countdown = 10

# A condition that our while loop will check on each iteration.
#this is the while condidtion in a single line
# while countdown >= 0: print(countdown); countdown -= 1
#multiple lines
while countdown >= 0:
  print(countdown)
  countdown -= 1

# Several code statements to execute on each iteration of the loop.
print("We have liftoff!")
