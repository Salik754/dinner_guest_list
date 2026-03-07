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

# Function to remove a guest
def remove_guest():
    if not guests:#check if guest list is empty
        print("No guests to remove.")
        return
    #ask which guest to remove
    name = input("Enter the guest name to remove: ").strip().title()
    #check if guest exists and remove
    if name in guests:#guest found
        guests.remove(name)#remove guest from list
        print(f"Guest '{name}' removed successfully!")
    else:#guest not found
        print("Guest not found.")


# Function to sort guests alphabetically
def sort_guests():
    if not guests:#check if guest list is empty
        print("No guests to sort.")
        return#sort guests alphabetically
    
    guests.sort()
    print("Guests have been sorted alphabetically.")


# Function to show the number of guests
def show_guest_count():
    print(f"Total number of guests: {len(guests)}")

# Function to show personalized invitations
def show_invitations():
    if not guests:#check if guest list is empty
        print("No guests to show invitations for.")
        return
    
    print("\n--- Invitations ---")
    for guest in guests:#show personalized invitation for each guest
        print(f"Dear {guest}, you are invited to the dinner reception!")
    print("------------------\n")

# Main menu loop
def main():
    print("Welcome to the Reception Guest Manager!\n")
    
    while True:
        print("Menu:")
        print("1. Add guest")
        print("2. Modify guest")
        print("3. Remove guest")
        print("4. Sort guests")
        print("5. Show number of guests")
        print("6. Show invitations")
        print("7. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":# Add guest
            add_guest()
        elif choice == "2":# Modify guest
            modify_guest()
        elif choice == "3":# Remove guest
            remove_guest()
        elif choice == "4":# Sort guests
            sort_guests()
        elif choice == "5":# Show number of guests
            show_guest_count()
        elif choice == "6":# Show invitations
            show_invitations()
        elif choice == "7":# Exit
            print("Goodbye! Thank you for using the Guest Manager.")
            break
        else:#handle invalid menu choice
            print("Invalid choice. Please try again.")
        print()  # Just adds a blank line for readability
