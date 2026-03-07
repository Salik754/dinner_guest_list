# Create empty guest list
guests = []


# Function to get a properly formatted guest name with validation
def get_guest_name(prompt):
    while True:
        name = input(prompt).strip().title()
        if name == "":
            print("Name cannot be empty. Try again.")
        elif name in guests:
            print("Guest already exists. Try again.")
        else:
            return name
        
# Function to add a guest
def add_guest():
    name = get_guest_name("Enter guest name to add: ")
    guests.append(name)
    print(f"Guest '{name}' added successfully!")

# Function to modify a guest's name
def modify_guest():
    if not guests:
        print("No guests to modify.")
        return
    #ask which guest to modify
    name = input("Enter the guest name to modify: ").strip().title()
    #check if guest exists
    if name not in guests:
        print("Guest not found.")
        return
    #ask for new name
    new_name = input("Enter the new name: ").strip().title()
    #validate new name
    if new_name == "":
        print("Name cannot be empty.")
        return
    elif new_name in guests:
        print("Duplicate name not allowed.")
        return
    #update guest name
    index = guests.index(name)
    guests[index] = new_name
    print(f"Guest '{name}' has been updated to '{new_name}'.")

# Function remove_guest
#     ask which guest to remove
#     if guest exists
#         remove guest

# Function sort_guests
#     sort the guest list alphabetically

# Function show_guest_count
#     print number of guests

# Function show_invitations
#     for each guest
#         print invitation message

# Main program
#     show menu
#     ask for choice
#     run correct function