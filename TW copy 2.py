
restaurants = [
    {
        'name': '故宫博物院',
        'address': '111台湾台北市士林區至善路二段221號'
    },
    {
        'name': '鐵 F.f Teppanyaki 鐵板燒（萬大店）',
        'address': '台北, 中国台湾'
    },
    {
        'name': '明日大饭店',
        'address': '108台湾台北市萬華區成都路23號'
    },
    {
        'name': 'Taipei 101 Observatory',
        'address': '110台湾台北市信義區信義路五段7號89樓'
    },
    {
        'name': '康桥慢旅',
        'address': '700台湾台南市中西區民生路二段416號'
    },
    {
        'name': '友爱街旅馆 (U.I.J Hotel&Hostel (UIJ))',
        'address': '友爱街115巷5号, 台南市, 台南, 中国台湾'
    },
    {
        'name': '台北北门窝泊旅 (Beimen Wow Poshtel)',
        'address': '太原路92巷2-1号, 台北车站, 台北, 中国台湾'
    },
    {
        'name': '寧夏夜市',
        'address': '台湾'
    },
    {
        'name': '王福芋圓',
        'address': '台湾'
    },
    {
        'name': 'Neko coffee 貓珈',
        'address': '台北, 中国台湾'
    },
    {
        'name': '津富倉 手作港式蘿蔔糕 小籠湯包 小燒包',
        'address': '台北, 中国台湾'
    },
    {
        'name': '藏壽司（甜品）',
        'address': '台北, 中国台湾'
    },
    {
        'name': '壽司郎',
        'address': '台北, 中国台湾'
    },
    {
        'name': '合點壽司 がってん寿司 京站店',
        'address': '台北, 中国台湾'
    },
    {
        'name': '武聖夜市',
        'address': '台南, 中国台湾'
    },
    {
        'name': 'Chun纯薏仁',
        'address': '台南, 中国台湾'
    },
    {
        'name': '立吞寿司',
        'address': '台南, 中国台湾'
    },
    {
        'name': '麵屋 壓軸',
        'address': '台南, 中国台湾'
    },
    {
        'name': '鸿品牛肉汤',
        'address': '台南, 中国台湾'
    },
    {
        'name': '邱家小卷米粉',
        'address': '台南, 中国台湾'
    },
    {
        'name': '一煥關東煮',
        'address': '台南, 中国台湾'
    },
    {
        'name': '老厝1933燒烤',
        'address': '台南, 中国台湾'
    },
    {
        'name': '小鹿家 面包店',
        'address': '台南, 中国台湾'
    },
    {
        'name': '小赤佬干锅 忠义店',
        'address': '台南, 中国台湾'
    },
    {
        'name': '阿江鳝鱼意面',
        'address': '台南, 中国台湾'
    },
    {
        'name': '青楼中式餐酒馆',
        'address': '台北, 中国台湾'
    },
    {
        'name': '金泰日式料理-内湖店',
        'address': '台北, 中国台湾'
    },
    {
        'name': '巴雷巴雷印度餐厅',
        'address': '台北, 中国台湾'
    },
    {
        'name': 'Solo Pasta',
        'address': '台北, 中国台湾'
    },
    {
        'name': '兴波咖啡 华山旗舰店',
        'address': '台北, 中国台湾'
    },
    {
        'name': '阜杭豆浆',
        'address': '台北, 中国台湾'
    },
    {
        'name': '温咖喱 Wen Curry',
        'address': '台北, 中国台湾'
    },
    {
        'name': '双月食品社 青岛店',
        'address': '台北, 中国台湾'
    },
    {
        'name': 'Oh my!原燒 台北林森北店',
        'address': '台北, 中国台湾'
    },
    {
        'name': '小仓屋鳗鱼饭',
        'address': '台北, 中国台湾'
    },
    {
        'name': '二屋牡蠣拉麵',
        'address': '台北, 中国台湾'
    },
    {
        'name': '阿柑姨芋圆',
        'address': '台北, 中国台湾'
    },
    {
        'name': 'CHLIV New Taipei Jiufen',
        'address': '台北, 中国台湾'
    },
    ]

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
#for reviews
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import certifi

# Set the SSL_CERT_FILE environment variable to the path of the certificate bundle
os.environ['SSL_CERT_FILE'] = certifi.where()

# Replace with your own Google API key,this api key only works for me
google_api_key = 'AIzaSyDkUMceiQ-9zSkB4RlJwMvH14lNO1SZ48k'

# Initialize the Google Maps client
gmaps_client = googlemaps.Client(key=google_api_key)

# Initialize gmaps for displaying the results on a map
gmaps.configure(api_key=google_api_key)

rest_res = []#useful restaurants
for restaurant in restaurants:
    # Perform a text search to find the restaurant
    places = gmaps_client.places(restaurant['name'] + ' ' + restaurant['address'])

    if places['status'] == 'OK':
        try:
            if places['results'][0]['rating'] < 3.9:
                print(f"{restaurant['name']} rating too low")
            elif 'location' not in places['results'][0]['geometry']:
                print(f"No results found for {restaurant['name']}")
            else:
                restaurant['rating']=places['results'][0]['rating']
                locations = [(places['results'][0]['geometry']['location']['lat'], places['results'][0]['geometry']['location']['lng'])]
                restaurant['lat'],restaurant['lng'] = locations[0][0],locations[0][1]
                name = restaurant["name"]
                latitude = restaurant["lat"]
                longitude = restaurant["lng"]
                #type_place = restaurant['results'][0]['type']
                #print(type_place)

                url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={name}&location={latitude},{longitude}&key={google_api_key}"
                response = requests.get(url)

                if response.status_code == 200:
                    search_results = response.json()
                    if "results" in search_results and search_results["results"]:
            # Extract the details of the first result (assuming it's the best match)
                        place_id = search_results["results"][0]["place_id"]
                        type_place = search_results['results'][0]['types']
                        if "restaurant" in type_place:
                            type_place = "restaurant"
                        elif "lodging" in type_place:
                            type_place = "hotel"
                            print(type_place)
                        #else:
                        #    type_place = "other"
                        restaurant["type"] = type_place
                        #print(f"Fetching reviews for restaurant with Place ID: {place_id}")
                        #review_rating = get_reviews_for_restaurant(place_id)
                        #print(review_rating)
            
            # Construct the direct link to the restaurant using the place ID
                        link = f"https://www.google.com/maps/place/?q=place_id:{place_id}"
                        restaurant["link"] = link
                        #restaurant['review_rating'] = review_rating
                        #restaurant['place_id'] = place_id
                    else:
                        restaurant["link"] = "empty link"
                #print(restaurant)
                rest_res.append(restaurant)
        except KeyError:
            print(f"No results found for {restaurant['name']}")
            #print(places['results'][0])
    else:
        print(f"No results found for {restaurant['name']}")

restaurants_data = []
for res in rest_res:
    # Create a JavaScript object (JSON) for each restaurant
    restaurant_data = {
        "name": res["name"],
        "latitude": res["lat"],
        "longitude": res["lng"],
        "rating": res["rating"],
        "link": res["link"],
        #"type": res["type"]
        #'review_rating': res['review_rating']
    }
    # Append the JavaScript object to the array
    restaurants_data.append(restaurant_data)

# Format the JavaScript array as a string
restaurants_data_js = json.dumps(restaurants_data)
# Define the HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"> 
  <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDkUMceiQ-9zSkB4RlJwMvH14lNO1SZ48k"></script>
</head>
<body>
  <div id="map" style="height: 950px; width: 100%;"></div>
  <script>
    async function initMap() {
      const { Map } = await google.maps.importLibrary("maps");
      const { AdvancedMarkerElement, PinElement } = await google.maps.importLibrary("marker");
      const map = new Map(document.getElementById("map"), {
        center: { lat: 23.6978, lng: 120.9605 },  // Centered on Taiwan
        zoom: 8,
      });

      
      // Create markers for restaurants
      var restaurants = {restaurant_data};
      restaurants.forEach(function(restaurant) {
        var position = { lat: restaurant.latitude, lng: restaurant.longitude };
        var iconColor = (restaurant.rating >= '4.5') ? 'yellow' : 'blue';
        if (restaurant.type === 'restaurant') {
    // If it's a restaurant, keep the iconColor as it is (based on rating)
        } else if (restaurant.type === 'hotel') {
            iconColor = 'green'; // If it's a hotel, set the label color to green
        } 

        var marker = new google.maps.Marker({
          position: position,
          map: map,
          title: restaurant.name,
          icon: {
            path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
            fillColor: iconColor,
            fillOpacity: 0.7,
            strokeWeight: 2,
            scale: 5
          }
        });

        // Create an info window for the restaurant
        var contentString = `<div>
          <h3>${restaurant.name}</h3>
          <p>Rating: ${restaurant.rating}</p>
          <a href="${restaurant.link}" target="_blank">View on Google Maps</a>
        </div>`;

        var infowindow = new google.maps.InfoWindow({
          content: contentString,
        });

        // Open the info window when the marker is clicked
        marker.addListener('click', function () {
          infowindow.open(map, marker);
        });
      });
    }
    initMap();
  </script>
  <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDkUMceiQ-9zSkB4RlJwMvH14lNO1SZ48k&callback=initMap">
  </script>
</body>
</html>
"""


# Insert the restaurant data into the HTML template
html_content = html_template.replace('{restaurant_data}', restaurants_data_js)

# Save the HTML content to a file
with open('ilu3.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
# Format the JavaScript array as a string
restaurants_data_js = json.dumps(restaurants_data)
