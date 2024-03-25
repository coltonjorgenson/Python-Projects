last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#subjects list
subjects = ['physics', 'calculus', 'poetry', 'history']
#grades list
grades = ['98', '97', '85', '88']
# two deminsional list to gradebook
gradebook = [['physics', 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
#print(gradebook)
#adding to the two d list
#brackets needed so it takes it as one argument
gradebook.append(['computer science', 100])
#adding to two d list
gradebook.append(['visual arts', 93])
#modify visual arts grade
gradebook[-1][-1] = 98 
#adding pass to a sublist
gradebook[2].append('Pass')
#combined gradebook in a new variable
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)