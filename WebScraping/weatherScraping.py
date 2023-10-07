from bs4 import BeautifulSoup
import var
import requests
import re
import copy
import classWeather

# Return the parsed web page.
def soup_get_page(url, parser="html.parser"):
  page = requests.get(url)
  return BeautifulSoup(page.text, parser)

def soup_get_weather_today_page(location):
  url = copy.copy(var.weather_today_url)
  if location:
    url = url + var.location_tag + location
  return soup_get_page(url)

def temperature_to_int(temperature):
  return int(re.findall(r'\d+',temperature)[0])

def get_temperature(soup):
  '''
  return Fahrenheit, Celsius
  '''
  temperature = temperature_to_int(soup.find(class_=re.compile(var.class_temp)).text)
  temperature_unit = soup.find(class_=re.compile(var.class_unit)).text
  if temperature_unit == var.fahrenheit:
    # Celsius = (Fahrenheits-32)/1.8
    return temperature, int((temperature-32)/1.8)
  elif temperature_unit == var.celsius:
    # Fahrenheit = (Celsius∗1.8)+32 
    return int((temperature*1.8)+32), temperature
  else:
    raise Exception("Error: No temperature unit accepted. Type: " + str(temperature_unit))

def create_weather(location):
  # Get weather page
  soup = soup_get_weather_today_page(location)
  # Scrape weather data
  location = soup.find(class_=re.compile(var.class_location)).text
  weather_type = soup.find(class_=re.compile(var.class_weather_type)).text
  f_temperature, c_temperature = get_temperature(soup)

  # Create weather
  return classWeather.Weather(location, weather_type, f_temperature, c_temperature)


# Function to get the weather information of the day.
def get_weather(location=""):
  # create weather type
  return create_weather(location)


