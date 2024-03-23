# Write your code below: 
#step 1
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
#step 2
  car_rental_total = car_rental_rate * trip_time
#step 3
  hotel_total = hotel_rate * trip_time - 10
#step 4
  trip_total = car_rental_total + hotel_total + plane_ticket_price


  return trip_total

# Step 5: call your function
print(calculate_expenses(200, 100, 100, 5))