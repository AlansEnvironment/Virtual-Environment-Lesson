import requests
import os
from pprint import pprint
from dotenv import load_dotenv #reading the variable from the .env file and sets 
                               # them in .osenviron code of the application which envrionment variables

load_dotenv()

def get_current_weather():
    print('\n*** Get current weather conditions ***\n')

    city = input('\nName of City: ')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    #print(request_url)

    weather_data = requests.get(request_url).json()
    #pprint(weather_data) making it easier to read the .json data

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nTemperature Feels like {weather_data["main"]["feels_like"]}')
    print(f'\nActual Temperature is {weather_data["main"]["temp"]} and {weather_data["weather"][0]["description"].capitalize()}')
    print(f'\nHighs of {weather_data["main"]["temp_max"]} with lows of {weather_data["main"]["temp_min"]}\n')


if __name__ =="__main__":

    get_current_weather()
