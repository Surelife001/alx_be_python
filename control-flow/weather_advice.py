# user input

user_input = input("What's the weather like today? (sunny/rainy/cold):").lower()
# control flow to provide advice based on weather
if user_input is "sunny":
    recommendation = "Wear a t-shirt and sunglasses."
elif user_input is "rainy":
    recommendation ="Don't forget your umbrella and a raincoat."
elif user_input is "cold":
    recommendation =" Make sure to wear a warm coat and a scarf."
else:
    recommendation="Sorry, I don't have recommendations for this weather."
print(recommendation)