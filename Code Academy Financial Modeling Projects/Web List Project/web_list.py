# Your code below:
#customer first names
first_names = ['Ainsley','Ben', 'Chani', 'Depak']
#customer preferred sizes
preferred_size = ['Small', 'Large', 'Medium']
#adding med to preferred_size list
preferred_size.append('Medium')
print(preferred_size)
#two-dimensional list
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
#change chani to regular shipping aka false
customer_data[2][2] = False
#removing boolean for ben. Have to actually enter the boolean for the .remove method to work
customer_data[1].remove(False)
#Adding new customers
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)