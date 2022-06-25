# Prints the weather for a location from text on clipboard
import json, requests, sys, pyperclip

# Compute location from clipboard text
import pprint

location = pyperclip.paste()

# Download the JSON data from OpenWeatherMap.org's API
url ='http://api.openweathermap.org/data/2.5/forecast/?q=%s&cnt=3&appid=efe4fe037aa09ad3436c8768df7718a7' % (location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable
weatherData = json.loads(response.text)
#pprint.pprint(weatherData)

# Print weather descriptions
w = weatherData['list']
print('--- --- ---')
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('---')
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('---')
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print('--- --- ---')
