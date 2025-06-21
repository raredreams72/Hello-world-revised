# Ask the user about the weather
print("=== Weather Checker ===")
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"

# Now, our if/else statement!
if is_raining: # This is our condition: "Is 'is_raining' True?"
    print("It's raining! Don't forget your umbrella and rain jacket! ☔")
else: # This block runs ONLY if the condition above (is_raining) is False
    print("It's not raining. Enjoy the clear skies! ☀️")

print("Have a great day!")

# Now let's change is_raining to False and run it again
print("\n--- Running the code again with is_raining = False ---\n")

is_raining = False

if is_raining:
    print("It's raining! Don't forget your umbrella and rain jacket! ☔")
else:
    print("It's not raining. Enjoy the clear skies! ☀️")

print("Have a great day!")

# Next, update your bullet points for the Week 2 showcase presentation to include this new logical feature and its benefit.

