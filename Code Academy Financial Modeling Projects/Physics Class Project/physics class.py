# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
#function that takes an input of fahrenheit
def f_to_c(f_temp): 
  #defining celcius in an argument
  c_temp = (f_temp - 32) * 5/9
  #can also combine two lines with a single line 
  #return (f_temp - 32) * 5/9
  #we have to return the argument or the function doesn't do anything with it
  return c_temp
  #prints whatever we call into the function
#print(f_to_c(32))

#defining a new variable and setting it equal to f_to_c when 100 is passed in
f100_in_celsius = f_to_c(100)
#print(f100_in_celsius)

#takes celsius as an argument and converts to farenheit
def c_to_f(c_temp):
  #defining fahrenheit equation
  f_temp = (c_temp * 9/5) + 32
  #we have to return the above line or the equation doesn't do anything
  return f_temp
#print has to be indented same as the function
#print(c_to_f(120))

#defining a variable to be set to the function with 0 as the parameter
c0_in_fahrenheit = c_to_f(0)
#print(c0_in_fahrenheit)

#new function takes mass and acceleration as the parameters
def get_force(mass, acceleration):
  #we have to return mass * acceleration or the function doesn't do anything
  return mass * acceleration

#creating a new variable traing_force to store a test for get force
train_force = get_force(train_mass, train_acceleration)
print(train_force)

#printing out the statement with the integer (train force) needing to be turned into a string 
print('The GE train supplies ' + str(train_force) + ' Newtons of force.')

#default arguments for c are set in the parameter
def get_energy (mass, c=3*10**8):
  #Returning mass * c**2 for get_energy
  return mass * c**2

#testing get energy and saving the results to the bomb_energy variable
bomb_energy = get_energy(bomb_mass)
#print(bomb_energy)

#printing a string, bomb energy needs to be put in as a string rather than an integer
print('A 1kg bomb supplies ' + str(bomb_energy) + ' Joules.')

#define a function and then call get_force inside this function
def get_work(mass, acceleration, distance):
  #once get_work is run, we need to run this secondary function, get_force is run and we save that value to force
  force = get_force(mass, acceleration)
  #returning the function and multiplying it by distance
  return force * distance

#testing get_work on train_mass, train_acceleration and train_distance, then saving it to the train_work variable
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")











