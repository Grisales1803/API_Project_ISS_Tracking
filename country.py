import requests

def info_country(country):
  '''
  Function that shows the national flag of a country.
  '''
  # Save the content of the API in a variable called 'r'
  r = requests.get(f'https://restcountries.com/v3.1/alpha/{country}')

  # Try to parse the response as JSON
  try:
      response_dict = r.json()

      # Check if the response is a list and contains at least one element
      if isinstance(response_dict, list) and len(response_dict) > 0:
          info_country = response_dict[0]
          flag = info_country['flags']['png']
          flag_meaning = info_country['flags']['alt']
      else:
          # Handle cases where the response is not as expected
          flag = "https://static.vecteezy.com/system/resources/previews/028/086/717/original/ocean-water-surface-waves-isolated-on-transparent-background-file-cut-out-ai-generated-png.png"
          flag_meaning = "The ISS is over water"
  except Exception:
      # Handle any exceptions that occur during the API call or JSON parsing
      flag = "https://via.placeholder.com/150?text=Error"
      flag_meaning = "Error retrieving country information"

  # Return the flag and flag meaning
  return flag, flag_meaning