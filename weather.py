from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Houston"):

    request_url= request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\n Please choose your city name> ")
    if not bool(city.strip()):
        city = "Houston"

    weather_data = get_current_weather(city)

    if not weather_data['cod'] == 200:
        print("City not Found")

    print("\n")
    pprint(weather_data)