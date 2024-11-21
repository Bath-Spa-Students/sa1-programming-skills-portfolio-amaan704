# reviewing the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# incorporating the search term from the user
search_user = input("Enter the name you want to search for: ")

# looking for the name in the list
if search_user in names:
    print(f"{search_user} was found in the list.")
else:
    print(f"{search_user} was not found in the list.")