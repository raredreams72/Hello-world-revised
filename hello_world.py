from datetime import datetime

# Get current time
current_hour = datetime.now().hour

# Get user's name
name = input("What is your name? ")

# Time-based greeting
if 5 <= current_hour < 12:
    time_greeting = "Good morning"
elif 12 <= current_hour < 17:
    time_greeting = "Good afternoon"
else:
    time_greeting = "Good evening"

# Special greeting for Nadira
if name == "Nadira":
    print(f"🌟 {time_greeting}, it's the awesome AI Director, {name}! 🌟")
else:
    print(f"🌟 {time_greeting}, {name}! 🌟")
    print(f"Welcome to our special program, {name}!")

# Ask about mood
mood = input("How are you feeling today? (happy/sad/okay): ").lower()

# Respond based on mood
if mood == "happy":
    print(f"That's wonderful! Your positive energy is contagious! ✨")
elif mood == "sad":
    print(f"I'm here to cheer you up! Would you like to hear a joke? (yes/no): ")
    want_joke = input().lower()
    if want_joke == "yes":
        print("Why don't scientists trust atoms? Because they make up everything! 😄")
    else:
        print("That's okay! I hope your day gets better! 🌈")
else:
    print(f"Hope your day gets even better! 🌟")

print(f"Have a wonderful day, {name}! ✨") 