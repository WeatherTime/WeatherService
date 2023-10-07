
class Weather:
  def __init__(self, location, weather_type, f_temperature, c_temperature):
    self.location = location
    self.weather_type = weather_type
    self.f_temperature = f_temperature
    self.c_temperature = c_temperature
  
  def weather_to_dict(self):
    data = {
      "location":       self.location,
      "weather_type":   self.weather_type,
      "f_temperature":  self.f_temperature,
      "c_temperature":  self.c_temperature
    }
    return data
