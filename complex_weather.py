# Let's create a more complex weather forecast program
# We'll consider both temperature and weather conditions

# First, let's set up our weather variables
temperature = 25  # in Celsius
is_raining = True
is_windy = False
is_snowing = False

print("=== Weather Forecast ===")
print(f"Current temperature: {temperature}°C")

# Complex conditions using logical operators
if temperature > 30:
    print("It's very hot! Stay hydrated! 🥵")
elif temperature > 20 and not is_raining:
    print("Perfect weather for outdoor activities! 😎")
elif temperature > 15 and is_raining:
    print("It's warm but rainy. Bring an umbrella! ☔")
elif temperature > 10:
    if is_windy:
        print("It's cool and windy. Wear a jacket! 🧥")
    else:
        print("It's cool but calm. Light jacket recommended! 🧥")
elif temperature > 0:
    if is_snowing:
        print("It's cold and snowing! Bundle up! ❄️")
    else:
        print("It's cold! Wear warm clothes! 🧣")
else:
    print("It's freezing! Stay warm! 🥶")

# Additional complex condition using 'or'
if is_raining or is_snowing:
    print("Wet conditions: Be careful on the roads! 🚗")
    
# Using 'not' operator
if not is_windy and not is_raining:
    print("Great day for a picnic! 🧺")

print("\n=== Weather Safety Tips ===")
# Multiple conditions combined
if temperature > 30 and not is_raining:
    print("⚠️ High temperature alert: Stay in the shade and drink plenty of water!")
elif temperature < 5 and (is_raining or is_snowing):
    print("⚠️ Cold weather alert: Risk of hypothermia. Stay dry and warm!")
elif is_windy and (is_raining or is_snowing):
    print("⚠️ Severe weather alert: Strong winds with precipitation. Stay indoors if possible!") 