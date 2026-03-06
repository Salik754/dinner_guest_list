# Create empty guest list
guest = []

# Function add_guest
def add_guest():
    #     ask for guest name
    name = input("Enter guest name: ")
    #     format name
    name = name.strip().title()
    #     check if name is empty
    if not name:
        print("Invalid guest name.")
        return
    #     check if name already exists
    if name in guest:
        print("Guest already exists.")
        return
    #     if valid
    #         add guest to list
    guest.append(name)

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