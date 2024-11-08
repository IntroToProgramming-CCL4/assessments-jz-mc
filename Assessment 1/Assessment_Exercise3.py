name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = int(input("Enter your age: "))

user = {"Name": name, "Hometown": hometown, "Age": age}

print("Your name is", user["Name"], "and you are from", user["Hometown"], "and you are", user["Age"])