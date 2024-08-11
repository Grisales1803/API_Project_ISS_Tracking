import requests

def weather(lat, lon):
    '''
    Function that obtains the weather and country code based on the coordinates (Latitude and Longitude). 
    '''
    try:
        # Call the API with the latitude and longitude
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=21ef0bb1788c87ed4b0fa9b7a851e162&units=metric')
        # Save the JSON content of the variable r in a variable called response_dict
        response_dict = r.json()

        # Capture the weather description and temperature
        description = response_dict["weather"][0]["description"].title()
        temp = response_dict['main']['temp']

        # Capture the country code
        country_code = response_dict['sys'].get('country', '')

        # Determine if the ISS is over water
        water = False
        if country_code == '':
            water = True
            country_code = "The Ocean"

    except Exception:
        # If an error occurs, keep description and temp if they were already set
        description = locals().get('description', "null")
        temp = locals().get('temp', "null")
        country_code = "Error"
        water = False

    # Return all values
    return temp, description, country_code, water

