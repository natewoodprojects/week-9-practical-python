# temperature = 75
# forecast = "sunny"
# if temperature > 80 or temperature < 60:
#     print("Stay inside!")
# else: 
#     print("Enjoy the outdoors!")

# if temperature < 80 and forecast != "rain":
#     print("Go outside!")
# else: 
#     print("Stay inside!")

# if not forcast == "rain": 
#     print("Go outside!")
# else: 
#     print("Stay inside!")

import requests

api_key = "d66062829d96e9eaf8b2eb56f7d55f85"
city = "Orlando"
lat = "41"
lon = "87"
url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+api_key
print(url)