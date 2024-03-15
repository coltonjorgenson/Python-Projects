current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
#creating a new function with budget and expense as the parameters
#Line 12 makes the function return budget - exp
def deduct_expense(budget, expense):
  return budget - expense

#creating a shirt_expense variable. Because it's a variable we want with global scope it's not defined in a function
shirt_expense = 9

#setting a variable to a function
#note we don't use def to call the function, that is just for inital use
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

#calling an established function and passing the established variable in as the argument
print_remaining_budget(new_budget_after_shirt)
