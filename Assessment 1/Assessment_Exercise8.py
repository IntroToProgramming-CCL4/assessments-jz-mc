name_list = ["jake", "zac", "ian", "ron", "sam", "dave"]

# Ask the user to enter a name they want to search for
search_name = input("Enter a name to search: ").lower()  # Convert input to lowercase which makes it not case sensitive anymore

for name in name_list:
    if name == search_name:  # Check if the current name matches the user's input
        print(f"{search_name} is found in the list.")  # Print if the name is in the list
        break  # Exit the loop as the name has been found
else:
    # If the loop completes without finding the name, print that it wasn't found
    print(f"{search_name} is not found in the list.")  # Print if the name is not in the list
