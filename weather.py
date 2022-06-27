temperature = 75
forecast = "sunny"
if temperature > 80 or temperature < 60:
    print("Stay inside!")
else: 
    print("Enjoy the outdoors!")

if temperature < 80 and forecast != "rain":
    print("Go outside!")
else: 
    print("Stay inside!")