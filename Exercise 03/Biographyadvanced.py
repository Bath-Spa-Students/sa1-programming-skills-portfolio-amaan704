# Step 1: Recieve user input for name, hometown, and age
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

#  Regulate input for age and check if it is a valid number
while True:
    try:
        age = int(input("Enter your age: "))  # Shift input to an integer
        break  # Depart loop if the age is a valid number
    except ValueError:
        print("Please enter a valid number for age.")

# Step 2:  obtain the information in a dictionary
person_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Step 3: Emit the values on separate lines using a single print statement
print(f"\nName: {person_info['name']}")
print(f"Hometown: {person_info['hometown']}")
print(f"Age: {person_info['age']}")