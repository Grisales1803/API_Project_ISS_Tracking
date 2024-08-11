# Import the module to calculate the distance between two points using latitude and longitude
import geopy.distance

def distance_to_ISS(lat1, lon1, lat2, lon2):
  coords_1 = (lat1, lon1) # location of ISS
  coords_2 = (lat2, lon2) # My location
  # Return the distance in km with 2 decimals
  return round(geopy.distance.distance(coords_1, coords_2).km,2)