#declare a variable and find modulus 263 of 11 which has a remainder of 1
order_263_r = (263 % 11)
#print the result of the variable
print (order_263_r)



#if the modulus equation comes out to anything but equally divided, aka 0, then the coupon prints
if order_263_r == 0:
    order_263_coupon = "yes"
#if it doesn't come out to yes on the above to be evenly divided, then show no 
else:
    order_263_coupon = "no"
#this prints the above result
print(order_263_coupon)

#this is doing another modulus variable check which does evenly divide by zero, so the first part of the if statement will come out as yes. 
order_264_r = (264 % 11)
print (order_264_r)

if order_264_r == 0:
  order_264_coupon = "yes"
  #the indentation of the if else statement matters here
else:
    order_264_coupon = "no"

    print(order_264_coupon)