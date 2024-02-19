# Get inches from user
inches = input("Enter distance in inches: ")

# Convert inches to integer
inches = int(inches)

# Set cm to inches * 2.54
cm = inches * 2.54

# Print cm
print(f"{cm} cm")

# Get pound from user
pounds = input("Enter weight in pound: ")

# Convert pounds to interger
pounds = int(pounds)

# Set kg to pounds / 2.2
kg = pounds / 2.2
print(f"{pounds} pounds is equal to {kg:.2f} kg")

# Get fahrenheit from user
fahrenheit = input("Enter temperature in Fahrenheit: ")

# Convert fahrenheit to interger
fahrenheit = int(fahrenheit)

# Set celcius to fahrenheit - 32 / (9/5)
celsius = (fahrenheit - 32) * 5/9

# Print celcius
print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")


