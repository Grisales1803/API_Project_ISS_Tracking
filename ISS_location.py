import requests

def locationISS():
  '''
  Function that determines where the space station is right now and returns the latitude and longitude. 
  '''
  try:
    # Save the content of the ISS Location API in a variable called 'r'
    r = requests.get('http://api.open-notify.org/iss-now.json')
  
    # Save the json content of the variable r in a variable called response_dict
    response_dict = r.json()
  
    # Extract the coordinates
    coor = response_dict['iss_position']
  
    # Extract Latitude
    lat = coor['latitude']
    # Extract Longitude:
    lon = coor['longitude']
    
    return lat, lon

  # Error management
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

    return None, None
