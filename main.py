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

# Function modify_guest
#     ask which guest to modify
#     if guest exists
#         ask for new name
#         replace name

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