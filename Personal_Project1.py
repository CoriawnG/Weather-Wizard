# Description: A simple Python script to get the current weather of a city using the OpenWeatherMap API.
# The get_weather function takes the city name and API key as input and returns the weather details.
# The API key is required to access the OpenWeatherMap API.
# The function makes a GET request to the API and extracts the weather information from the response.
# The weather details include the description, temperature, feels like temperature, city name, and country.
# The temperature is in Celsius by default, but it can be changed to Fahrenheit by setting the "units" parameter to "imperial".
# The function returns an error message if the response status code is not 200 or if the city name or API key is invalid.


import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial" # Change to "metric" for Celsius
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        city_name = data["name"]
        country = data["sys"]["country"]
        return f"Weather in {city_name}, {country}:\n" \
               f"- {weather.capitalize()}\n" \
               f"- Temperature: {temperature}°F\n" \
               f"- Feels like: {feels_like}°F"
    else:
        return f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}"


# Example Usage
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual API key
    api_key = "44fff8e62e170a9c909764c255289b45"  # Your API key
    city = input("Enter city name: ")
    print(get_weather(city, api_key))
