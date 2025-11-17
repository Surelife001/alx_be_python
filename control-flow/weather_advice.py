# user input

user_input = input("What's the weather like today? (sunny/rainy/cold):").lower()
# control flow to provide advice based on weather
if user_input is "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_input is "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_input is "cold":
    print(" Make sure to wear a warm coat and a scarf.")
else:
    print(" Sorry, I don't have recommendations for this weather.")