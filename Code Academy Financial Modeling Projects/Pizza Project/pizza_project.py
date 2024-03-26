# Your code below:
#list of toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
#list of prices
prices = [2, 6, 1, 3, 2, 7, 2]
#count number of times 2 occurs in prices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
#length of toppings
num_pizzas = len(toppings)
#print variables from above in a string
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')
#creating topping prices
pizza_and_prices = [(2, 'pepperoni'), (6, 'pineapple'), (1, 'cheese'), (3, 'sausage'), (2, 'olives'), (7, 'anchovies'), (2, 'mushrooms')]
print(pizza_and_prices)
#sorting price in ascending order
pizza_and_prices.sort()
#store first element from pizza_and_prices
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
#find most expensive pizzas
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
#remove anchovies from pizza_and_prices
pizza_and_prices.pop(-1)
print(pizza_and_prices)
#add peppers to pizza_and_prices
pizza_and_prices.insert(4,(2.5, 'peppers'))
print(pizza_and_prices)
#finding 3 cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)