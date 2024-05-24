
import gmaps
import googlemaps
import collections 
from collections.abc import Iterable 
collections.Iterable = Iterable
import matplotlib.pyplot as plt
from IPython.display import display
import requests
import json
###

# Replace with your own Google API key,this api key only works for me
google_api_key = ''

# Initialize the Google Maps client
gmaps_client = googlemaps.Client(key=google_api_key)

# Initialize gmaps for displaying the results on a map
gmaps.configure(api_key=google_api_key)

restaurants = [
    {
        'name': '516雞排- Chicken-チキン-닭',
        'address': '111台湾台北市士林區大東路15-30號'
    },
    {
        'name': '士林夜市铜锣烧',
        'address': '111台湾台北市士林區大東路15-13號'
    },
    # Add more restaurants and addresses as needed
    {
        'name': '茑烧日式居酒屋-士林店',
        'address': '111台湾台北市士林區中山北路五段505巷42弄1號'
    }]
for restaurant in restaurants:
    places = gmaps_client.places(restaurant['name'] + ' ' + restaurant['address'])
    lat,lon=[places['results'][0]['geometry']['location']['lat'], places['results'][0]['geometry']['location']['lng']]
    print(lat,lon)

'''
endpoint = 'https://maps.googleapis.com/maps/api/directions/json'

# Define start and end points (latitude, longitude)
start_point = '25.0392193,121.4986043'  # Example
end_point = '25.0134436,121.5353398'  # Example

# Define transit waypoints (if any)
transit_waypoints = [
    '25.0313085,121.5600484',  # Replace with the latitude and longitude of your transit stop
     # Replace with the latitude and longitude of your transit stop
]

# Specify travel modes
travel_modes = ['bus', 'subway', 'walking']

# Construct the API request URL
params = {
    'origin': start_point,
    'destination': end_point,
    'mode': '|'.join(travel_modes),  # Combine travel modes with a pipe (|) separator
    'waypoints': '|'.join(transit_waypoints),  # Combine transit waypoints with a pipe (|) separator
    'key': google_api_key,
    'avoid': 'tolls',  # Optionally, you can specify avoidance preferences
}

# Make the API request
response = requests.get(endpoint, params=params)

if response.status_code == 200:
    data = response.json()
    routes = data.get('routes', [])
    
    if routes:
        # Consider the first route (you can iterate through multiple routes if available)
        route = routes[0]
        
        # Extract and print the summary of the route
        print(f"Summary of the Route:")
        print(f"Total Distance: {route['legs'][0]['distance']['text']}")
        print(f"Total Duration: {route['legs'][0]['duration']['text']}")
        
        # Extract and print steps for each leg of the journey
        for leg in route['legs']:
            print(f"\nLeg Summary:")
            print(f"Start Address: {leg['start_address']}")
            print(f"End Address: {leg['end_address']}")
            
            # Iterate through steps in this leg
            for step in leg['steps']:
                print(f"\nStep Instructions: {step['html_instructions']}")
                print(f"Distance: {step['distance']['text']}")
                print(f"Duration: {step['duration']['text']}")
                print(f"Travel Mode: {step['travel_mode']}")
                
                # Optionally, you can extract and print transit details for transit steps
                if step['travel_mode'] == 'TRANSIT':
                    transit_details = step['transit_details']
                    print(f"Transit Details:")
                    print(f"Line Name: {transit_details['line']['name']}")
                    print(f"Departure Stop: {transit_details['departure_stop']['name']}")
                    print(f"Arrival Stop: {transit_details['arrival_stop']['name']}")
    else:
        print("No routes found.")
    # Process the directions and steps in the response
else:
    print(f"Request failed with status code {response.status_code}")
'''
