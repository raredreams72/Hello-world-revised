def get_welcome_message(name):
    return f"Welcome, {name}! We're glad to have you here."

def main():
    # Ask the user to enter their name and store it in the 'name' variable
    name = input("Please enter your name: ")
    
    # Call the get_welcome_message function with the user's name and store the result
    welcome_message = get_welcome_message(name)
    
    # Display the welcome message on the screen
    print(welcome_message)

if __name__ == "__main__":
    main() 