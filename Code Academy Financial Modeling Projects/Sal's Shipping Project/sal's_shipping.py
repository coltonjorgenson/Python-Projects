#set a random number to the weight variable to check against the if statememnts
weight = 41.5
#Ground Shipping
#The elif statements take the end range amount rather than needing to use both numbers
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <=6:
  cost_ground = weight * 3 + 20 
elif weight <=10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
  #printing out the ground_cost with the message
print('Ground cost $',cost_ground)

#Ground Shipping Premium variable
cost_ground_premium = 125
print('Ground premium cost $',cost_ground_premium)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25
print('Drone cost $',cost_drone)


