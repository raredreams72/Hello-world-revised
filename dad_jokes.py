#!/usr/bin/env python3
"""
Dad Jokes Generator
A fun interactive application that tells dad jokes!
"""

import random
import time
import sys

def generate_dad_joke():
    """
    Generates a dad joke with predictable & wholesome humor.
    The jokes have an obvious, non-offensive punchline, often relying on
    simple wordplay or puns, designed to elicit a lighthearted groan.
    """
    jokes = [
        ("Why don't scientists trust atoms?", "Because they make up everything!"),
        ("What do you call a fake noodle?", "An impasta!"),
        ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
        ("What do you call a bear with no teeth?", "A gummy bear!"),
        ("Why don't eggs tell jokes?", "They'd crack each other up!"),
    ]
    setup, punchline = random.choice(jokes)
    return f"{setup} {punchline}"

class DadJokes:
    def __init__(self):
        self.jokes = {
            "food": [
                ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
                ("What do you call a fake noodle?", "An impasta!"),
                ("Why don't eggs tell jokes?", "They'd crack each other up!"),
                ("What do you call cheese that isn't yours?", "Nacho cheese!"),
                ("Why did the tomato turn red?", "Because it saw the salad dressing!"),
                ("What's the best thing about Switzerland?", "I don't know, but the flag is a big plus!"),
                ("Why don't scientists trust atoms?", "Because they make up everything!"),
                ("What do you call a bear with no teeth?", "A gummy bear!")
            ],
            "animals": [
                ("What do you call a fish wearing a bowtie?", "So-fish-ticated!"),
                ("Why don't oysters donate to charity?", "Because they're shellfish!"),
                ("What do you call a sleeping bull?", "A bulldozer!"),
                ("Why did the chicken go to the séance?", "To talk to the other side!"),
                ("What do you call a duck that gets all A's?", "A wise quacker!"),
                ("Why don't elephants use computers?", "They're afraid of the mouse!"),
                ("What do you call a bear with no ears?", "B!"),
                ("Why did the cow go to outer space?", "To see the moooon!")
            ],
            "work": [
                ("Why did the math book look so sad?", "Because it had too many problems!"),
                ("What do you call a computer that sings?", "A Dell!"),
                ("Why did the programmer quit his job?", "Because he didn't get arrays!"),
                ("What do you call a computer that dances?", "A Dell-ightful computer!"),
                ("Why did the scarecrow get promoted?", "He was outstanding in his field!"),
                ("What do you call a bear with no teeth?", "A gummy bear!"),
                ("Why don't scientists trust atoms?", "Because they make up everything!"),
                ("What do you call a fake noodle?", "An impasta!")
            ],
            "family": [
                ("Why did the dad bring a ladder to the bar?", "Because he heard the drinks were on the house!"),
                ("What do you call a dad who's a magician?", "A dad-ician!"),
                ("Why did the dad bring string to the restaurant?", "In case he needed to tie one on!"),
                ("What do you call a dad who's a baker?", "A bread-winner!"),
                ("Why did the dad bring a pencil to the beach?", "In case he wanted to draw a line in the sand!"),
                ("What do you call a dad who's a musician?", "A dad-io!"),
                ("Why did the dad bring a map to the party?", "In case he got lost in the conversation!"),
                ("What do you call a dad who's a chef?", "A dad-cook!")
            ]
        }
        
        self.categories = list(self.jokes.keys())
        self.all_jokes = []
        for category_jokes in self.jokes.values():
            self.all_jokes.extend(category_jokes)
    
    def print_welcome(self):
        """Display a welcoming banner"""
        print("=" * 50)
        print("🎭 WELCOME TO DAD JOKES GENERATOR! 🎭")
        print("=" * 50)
        print("Get ready for some seriously dad-level humor!")
        print("(Warning: May cause eye-rolling and groaning)")
        print()
    
    def print_joke(self, joke_tuple):
        """Print a joke with dramatic timing"""
        setup, punchline = joke_tuple
        print(f"\n🤔 {setup}")
        time.sleep(1.5)  # Build suspense
        print(f"😄 {punchline}")
        print()
        time.sleep(1)
    
    def get_random_joke(self):
        """Get a random joke from any category"""
        return random.choice(self.all_jokes)
    
    def get_joke_by_category(self, category):
        """Get a random joke from a specific category"""
        if category in self.jokes:
            return random.choice(self.jokes[category])
        else:
            return None
    
    def show_categories(self):
        """Display available joke categories"""
        print("\n📂 Available Categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"  {i}. {category.title()}")
        print()
    
    def get_user_choice(self):
        """Get user's choice for what type of joke they want"""
        print("What would you like to do?")
        print("1. Get a random joke")
        print("2. Get a joke by category")
        print("3. See all categories")
        print("4. Tell me multiple jokes")
        print("5. Exit")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-5): ").strip()
                if choice in ['1', '2', '3', '4', '5']:
                    return choice
                else:
                    print("Please enter a number between 1 and 5.")
            except KeyboardInterrupt:
                print("\n\nGoodbye! Thanks for the laughs! 👋")
                sys.exit(0)
    
    def handle_category_choice(self):
        """Handle when user wants a joke by category"""
        self.show_categories()
        while True:
            try:
                category_choice = input("Enter category number or name: ").strip()
                
                # Try to match by number
                if category_choice.isdigit():
                    num = int(category_choice) - 1
                    if 0 <= num < len(self.categories):
                        category = self.categories[num]
                        break
                    else:
                        print("Invalid category number. Please try again.")
                        continue
                
                # Try to match by name
                category_choice = category_choice.lower()
                if category_choice in self.categories:
                    category = category_choice
                    break
                else:
                    print("Category not found. Please try again.")
                    continue
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye! Thanks for the laughs! 👋")
                sys.exit(0)
        
        joke = self.get_joke_by_category(category)
        if joke:
            print(f"\n🎯 Here's a {category} joke:")
            self.print_joke(joke)
        else:
            print("Sorry, no jokes found in that category!")
    
    def tell_multiple_jokes(self):
        """Tell multiple jokes in sequence"""
        try:
            num_jokes = int(input("How many jokes would you like to hear? (1-10): "))
            num_jokes = max(1, min(10, num_jokes))  # Clamp between 1 and 10
            
            print(f"\n🎪 Here are {num_jokes} dad jokes for you:")
            print("-" * 40)
            
            for i in range(num_jokes):
                print(f"\nJoke #{i+1}:")
                joke = self.get_random_joke()
                self.print_joke(joke)
                
                if i < num_jokes - 1:  # Don't ask after the last joke
                    continue_choice = input("Press Enter for next joke, or 'q' to quit: ").strip().lower()
                    if continue_choice == 'q':
                        break
                        
        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\nGoodbye! Thanks for the laughs! 👋")
            sys.exit(0)
    
    def run(self):
        """Main application loop"""
        self.print_welcome()
        
        while True:
            choice = self.get_user_choice()
            
            if choice == '1':
                print("\n🎲 Here's a random dad joke:")
                joke = self.get_random_joke()
                self.print_joke(joke)
                
            elif choice == '2':
                self.handle_category_choice()
                
            elif choice == '3':
                self.show_categories()
                
            elif choice == '4':
                self.tell_multiple_jokes()
                
            elif choice == '5':
                print("\n👋 Thanks for visiting Dad Jokes Generator!")
                print("Remember: A dad joke a day keeps the frowns away! 😄")
                break
            
            # Ask if user wants to continue
            if choice != '5':
                continue_choice = input("\nWould you like another joke? (y/n): ").strip().lower()
                if continue_choice not in ['y', 'yes']:
                    print("\n👋 Thanks for visiting Dad Jokes Generator!")
                    print("Remember: A dad joke a day keeps the frowns away! 😄")
                    break
                print("\n" + "="*50 + "\n")

def main():
    """Main function to run the Dad Jokes application"""
    try:
        dad_jokes = DadJokes()
        dad_jokes.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye! Thanks for the laughs! 👋")
    except Exception as e:
        print(f"\nOops! Something went wrong: {e}")
        print("But hey, at least it wasn't a dad joke! 😄")

if __name__ == "__main__":
    main() 