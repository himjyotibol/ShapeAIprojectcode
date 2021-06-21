import requests
from datetime import datetime
api_key = '427ef5d9e3479ed81afa2e4782976cc8'
location = input("Enter the city who's weather you want to see: ")
complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#collecting data from url through API
temp_city = ((api_data['main']['temp'])- 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wnd_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

#displaying the collected data 
print("Weather status for the" .format(location.upper(), date_time))
print("Current weather is: {:.2f} deg C".format(temp_city))
print("Current Weather Description:",weather_desc)
print("Current Humdity:",hmdt,"%")
print("Current Wind Speed:",wnd_spd,"kmph")

#storing the collected data in a text file for ShapeAi project
with open('weatherdatabyhimjyoti.txt','wb') as t:
    t.write(api_link.content)
