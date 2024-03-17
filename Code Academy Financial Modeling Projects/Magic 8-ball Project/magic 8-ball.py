#this imports the randint
import random 
#preset variables
name = 'Colton'
question = 'Should I go for a run'
answer = ''
#generates a random number between 1 and 12 using the random.randint() functiona nd assigns it to the random_number variable
random_number = random.randint(1, 12)
#print(random_number)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
elif random_number == 10:
  answer = 'There is no way'
elif random_number == 11:
  answer = 'This will 100% happen'
elif random_number == 12:
  answer = 'Ask someone else'
else:
  answer = 'Error'


#If no name is provided, this statement will fill in the gap
if name == '':
  print('Question: ' + question)
#If there is a name, print the name and then asks:
else:
  print(name + ' asks: ' + question)
#\ is used to comment make the apostrophe work in the string
#this prints the second line with the magic 8-ball answer
#If question string is empty, print out a message to a user
if question == '':
  print('You must first ask me a question')
else:
  print('Magic 8-Ball\'s answer: ' + answer)




