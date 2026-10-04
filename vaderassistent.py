import requests
import csv
from datetime import datetime


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    return latitude, longitude


def get_weather(latitude, longitude):
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code"
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params,
        timeout=10
    )

    weather_data = weather_response.json()

    temperature = weather_data["current"]["temperature_2m"]
    weather_code = weather_data["current"]["weather_code"]

    return temperature, weather_code


def describe_weather(weather_code):
    if weather_code == 0:
        return "Klart väder"
    elif weather_code in [1, 2, 3]:
        return "Molnigt"
    elif weather_code in [51, 53, 55]:
        return "Duggregn"
    elif weather_code in [61, 63, 65]:
        return "Regn"
    elif weather_code in [71, 73, 75]:
        return "Snö"
    else:
        return "Annat väder"


def save_weather(city, temperature, condition):
    with open("weather_data.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            city,
            temperature,
            condition,
            datetime.now().strftime("%Y-%m-%d %H:%M")
        ])


def analyze_temperature(temperature):
    if temperature >= 30:
        return "Varning: Det är mycket varmt."
    elif temperature < 0:
        return "Varning: Det är minusgrader."
    else:
        return "Temperaturen är normal."


class WeatherData:
    def __init__(self, city, temperature):
        self.city = city
        self.temperature = temperature

    def show_temperature(self):
        return f"{self.city}: {self.temperature} °C"


class WeatherAssistant(WeatherData):
    def show_warning(self):
        return analyze_temperature(self.temperature)


print("Väderassistenten startar")

try:
    city = input("Vilken stad vill du veta väder för? ")

    latitude, longitude = get_coordinates(city)

    temperature, weather_code = get_weather(
        latitude,
        longitude
    )

    condition = describe_weather(weather_code)

    weather = WeatherAssistant(
        city,
        temperature
    )

    print(weather.show_temperature())
    print(f"Väder: {condition}")
    print(weather.show_warning())

    save_weather(
        city,
        temperature,
        condition
    )

    print("Väderdata har sparats.")

    temperatures = [temperature]

    for value in temperatures:
        print(f"Registrerad temperatur: {value} °C")

except (KeyError, IndexError):
    print("Staden kunde inte hittas.")

except requests.RequestException:
    print("Kunde inte ansluta till vädertjänsten.")

except Exception as error:
    print(f"Ett fel uppstod: {error}")