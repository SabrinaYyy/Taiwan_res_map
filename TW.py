#code by Sabrina Yan and ChatGPT 3.5
import gmaps
import googlemaps
import collections 
from collections.abc import Iterable 
collections.Iterable = Iterable
import matplotlib.pyplot as plt
from IPython.display import display
import requests
import json
# Replace with your own Google API key,this api key only works for me
google_api_key = 'AIzaSyDkUMceiQ-9zSkB4RlJwMvH14lNO1SZ48k'

# Initialize the Google Maps client
gmaps_client = googlemaps.Client(key=google_api_key)

# Initialize gmaps for displaying the results on a map
gmaps.configure(api_key=google_api_key)

# Define a list of restaurants and their addresses
restaurants = [
    {
        'name': '好咖Thai',
        'address': '桃園市中壢區中北路19號, Taiwan'
    },
    {
        'name': '柒息地串燒居酒屋',
        'address': '台北市中山區長春路128-1號, Taiwan'
    },
    # Add more restaurants and addresses as needed
    {
        'name': '島語自助餐',
        'address': '台北市南港區經貿一路168號2樓, Taiwan'
    },
    {
        'name': '小王煮瓜',
        'address': '108台北市萬華區華西街17之4號攤位153號, Taiwan'
    },
    {
        'name': '查記',
        'address': '台北市信義區吳興街37號, Taiwan'
    },

    {
        'name': '雄記蔥抓餅',
        'address': '台北市中正區羅斯福路四段108巷2號, Taiwan'
    },
    {
        'name': '姜蔬菜大蛋餅',
        'address': '台北市中正區羅斯福路四段90巷, Taiwan'
    },
    {
        'name': '賢夫美食',
        'address': '台北市中正區羅斯福路四段92號1號79攤, Taiwan'
    },
    {
        'name': '516雞排',
        'address': '士林夜市, Taiwan'
    },
    {
        'name': '大茗',
        'address': '台北市中正區汀州路三段158之1號, Taiwan'
    },{
        'name': '藍家割包',
        'address': '台北市中正區羅斯福路三段316巷8弄3號, Taiwan'
    },
    {
        'name': '回味麵煎餅',
        'address': '台北市中正區羅斯福路四段90巷2號, Taiwan'
    },
    {
        'name': '阿鸞手工法國麵包',
        'address': '台北市中正區羅斯福路四段90巷2號, Taiwan'
    },
    {
        'name': '菠蘿麵包',
        'address': '台北市中正區羅斯福路四段80號, Taiwan'
    },
    {
        'name': '螺絲瑪麗Rosemary',
        'address': '10491台北市中山區南京西路12巷13弄9號, Taiwan'
    },
    {
        'name': '徐徐燒鳥',
        'address': '台北市大安區安和路一段78巷34號, Taiwan'
    },
    {
        'name': '魚韻日式料理 北醫店',
        'address': '台北市中山區樂群三路200號5樓(忠泰樂生活), Taiwan'
    },
    {
        'name': 'JK STUDIO Burger',
        'address': '台北市信義區吳興街220巷21號, Taiwan'
    },
    {
        'name': '饃饃噠心動肉夾饃',
        'address': '台北市大安區金山南路二段25-1號, Taiwan'
    },
    {
        'name': '豆豆里',
        'address': '台北市大安區永康街2巷7號, Taiwan'
    },
    {
        'name': '悄悄好食',
        'address': '台北市大安區永康街31巷14-4號, Taiwan'
    },
    {
        'name': '錐子日式可麗餅',
        'address': '台北市大安區麗水街16巷8號, Taiwan'
    },
    {
        'name': 'アツアツ章魚燒',
        'address': '台北市中山區中山北路一段83巷11-2號, Taiwan'
    },
    {
        'name': ' FRENCH TOAST FACTORY',
        'address': '新北市板橋區府後街7號, Taiwan'
    },
    {
        'name': 'Lazy Pasta 慵懶義式廚房 信義市府店',
        'address': '台北市信義區忠孝東路五段71巷30號1樓, Taiwan'
    },
    {
        'name': '野人花園',
        'address': '台北市士林區菁山路131巷13-1號, Taiwan'
    },
    {
        'name': '1001 Nights Kitchen Taipei 一千零一夜廚房',
        'address': '台北市松山區八德路四段618號2樓, Taiwan'
    },
    {
        'name': '韓江烤肉 市民總店',
        'address': '台北市大安區市民大道四段104號, Taiwan'
    },
    {
        'name': '品都串燒攤忠孝店',
        'address': '台北市大安區忠孝東路四段299號, Taiwan'
    },
    {
        'name': '四川吳抄手',
        'address': '台北市信義區松仁路58號（遠百A13 4樓）, Taiwan'
    },
    {
        'name': 'sumidatw',
        'address': '台北市中山區中山北路二段20巷23號2樓, Taiwan'
    },
    {
        'name': '好正商行 HAO ZHENG',
        'address': '台北市大安區市民大道四段48巷3號之2, Taiwan'
    },
    {
        'name': '草山夜未眠',
        'address': '111台湾台北市士林區東山路25巷81弄99號, Taiwan'
    },
    {
        'name': '爆汁老上海生煎',
        'address': '台北市中山區中山北路一段105巷4-9號4-8號, Taiwan'
    },
    {
        'name': '爆汁老上海生煎',
        'address': '台北市中正區汀州路三段213號, Taiwan'
    },
    {
        'name': '鶴橋風月',
        'address': '新北市林口區文化三路一段356號2F, Taiwan'
    },
    {
        'name': '豆留森林',
        'address': '台北市士林區格致路70號, Taiwan'
    },
    {
        'name': '窗邊cafe',
        'address': '台北市士林區中山北路六段476號2樓, Taiwan'
    },
    {
        'name': '漾波酒食処',
        'address': '台北東區, Taiwan'
    },
    {
        'name': 'The Platypus Café',
        'address': '114台北市內湖區陽光街321巷40號, Taiwan'
    },
    {
        'name': '草里一號店',
        'address': '253001台湾新北市石門區阿里荖1號, Taiwan'
    },
    {
        'name': 'BounceBackBurger',
        'address': '板橋裕民街60號, Taiwan'
    },
    {
        'name': '士林夜市銅鑼燒',
        'address': '士林夜市, Taiwan'
    },
    {
        'name': '揚日式料理',
        'address': '新北市中和區中正路839巷7號, Taiwan'
    },
    {
        'name': 'At · First 早寓',
        'address': '106台湾台北市大安區延吉街70巷5弄6號, Taiwan'
    },
    {
        'name': '咖哩日和 Curry Biyori',
        'address': '台北市大安區忠孝東路三段216巷4弄23號1樓, Taiwan'
    },
    {
        'name': '饌澤原超市火鍋',
        'address': '桃園市蘆竹區桃園街6號, Taiwan'
    },
    {
        'name': '1993韓國烤肉餐酒吧',
        'address': '台北市大安區敦化南路一段160巷9號4，1樓, Taiwan'
    },
    {
        'name': '酒食人餐酒館',
        'address': '新北市板橋區中山路一段124號, Taiwan'
    },
    {
        'name': '有吉豐盛丼',
        'address': '台北市大安區復興南路一段107巷5弄15號1樓, Taiwan'
    },
    {
        'name': '三緣舍居酒屋 炭火串燒',
        'address': '300新竹市東區光華街18巷3號, Taiwan'
    },
    {
        'name': '和牛研究室 WAGYU LAB ',
        'address': '台北市中山區樂群三路303號, Taiwan'
    },
    {
        'name': '生生kapi',
        'address': '新竹縣竹北市勝利八街二段117號, Taiwan'
    },
    {
        'name': ' 鐵 F.f Teppanyaki 鐵板燒',
        'address': '臺北市萬華區西昌街49號(西門店), Taiwan'
    },
    {
        'name': '特香齋西餐廳',
        'address': '新北市板橋區中山路一段26號2樓, Taiwan'
    },
    {
        'name': '小小麥 台北信義店',
        'address': '台北市信義區永吉路30巷75號, Taiwan'
    },
    {
        'name': '涮八方',
        'address': '台北市大安區安和路二段209巷6號, Taiwan'
    },
    {
        'name': '大葉高島屋',
        'address': '台北市士林區忠誠路二段𝟱𝟱號大葉髙島屋𝟱樓, Taiwan'
    },
    {
        'name': '寅和鐵板燒',
        'address': '110台湾台北市信義區忠孝東路四段559巷16弄2號, Taiwan'
    },
    {
        'name': '龍潭·名人堂花園大飯店',
        'address': '桃園市龍潭區民生路141巷150號, Taiwan'
    },
    {
        'name': 'L’idée Sweet 時甜',
        'address': '台北市大安區忠孝東路四段216巷27弄12號, Taiwan'
    },
    {
        'name': '小倉屋 Kokuraya',
        'address': '台北市中山區樂群三路303號, Taiwan'
    },
    {
        'name': '美好年代',
        'address': '台北市大安區大安路一段52巷23號, Taiwan'
    },
    {
        'name': '京町 山本屋',
        'address': '台北市大安區金華街143號 （榕錦時光文化園區）, Taiwan'
    },
    {
        'name': 'Takumi Dumplings 巧之味手工水餃 濟南店',
        'address': '100台北市中正區濟南路二段6號, Taiwan'
    },
    {
        'name': '帕泰家 新竹巨城店',
        'address': '新竹市東區中央路229號7F, Taiwan'
    },
    {
        'name': '桃園神社',
        'address': '桃園, Taiwan'
    },
    {
        'name': '子曰深夜食堂',
        'address': '台北市中山區中山北路二段59巷38號, Taiwan'
    },
    {
        'name': '承繼 CHENG JI',
        'address': '臺北市松山區興安街222號1樓, Taiwan'
    },
    {
        'name': '一江小籠包',
        'address': '一江街與松江路108巷, Taiwan'
    },
    {
        'name': 'Morton’s The Steakhouse',
        'address': '台北市信義區忠孝東路五段68號45F, Taiwan'
    },
    {
        'name': '福湯岩盤浴',
        'address': '新竹市北區大雅路88號B1, Taiwan'
    },
    {
        'name': '丸舢拉麵',
        'address': '台北市中正區八德路一段48號, Taiwan'
    },
    {
        'name': '查壹茶',
        'address': '新光南西B2, Taiwan'
    },
    {
        'name': '墾丁鹿ㄦ島水豚生態園區',
        'address': '屏東縣恆春鎮省北路275之1號, Taiwan'
    },
    {
        'name': '春桃手作厚工甜品',
        'address': '台北市萬華區永福街56號, Taiwan'
    },
    {
        'name': '平禄壽司-松竹店',
        'address': '台中市北屯區松竹路三段362號, Taiwan'
    },
    {
        'name': '寧夏夜市',
        'address': '103台湾台北市大同區寧夏路, Taiwan'
    },
    {
        'name': '劉記古早味蔥蛋餅',
        'address': '台北市中正區羅斯福路四段108巷2-3號, Taiwan'
    },
    {
        'name': 'KANSYA Japanese Tea Salon日本茶專門店',
        'address': '高雄市苓雅區廣州一街145-6號, Taiwan'
    },
    {
        'name': '順口香麥仔煎',
        'address': '台中第三市場, Taiwan'
    },
    {
        'name': '蔘源藥頭排骨',
        'address': '台北市大同區延平北路三段32號, Taiwan'
    },
    {
        'name': '茶餅舖 ',
        'address': '台北市萬華區漢口街二段54-35號, Taiwan'
    },
    {
        'name': '點點小食光紅豆餅',
        'address': '新北市板橋區龍泉街96號, Taiwan'
    },
    {
        'name': '吉哆火鍋百匯',
        'address': '新北市板橋區文化路二段181號, Taiwan'
    },
    {
        'name': '108抹茶茶廊',
        'address': '103台北市大同區承德路一段1號 B3F, Taiwan'
    },
    {
        'name': '饒河夜市',
        'address': '105台湾台北市松山區饒河街, Taiwan'
    },
    {
        'name': 'IKIGAI 燒肉專門店',
        'address': '111台北市士林區忠誠路二段55號B1, Taiwan'
    },
    {
        'name': '樓下那煎銅鑼燒',
        'address': '新北市三重區永安北路二段5巷3號, Taiwan'
    },
    {
        'name': '禾乃川國產豆製所',
        'address': '新北市三峽區民權街84巷12之1號, Taiwan'
    },
    {
        'name': '旱溪夜市',
        'address': '台中市東區旱溪東路一段, Taiwan'
    },
    {
        'name': '通化夜市九份芋圓',
        'address': '台北市大安區臨江街87號, Taiwan'
    },
    {
        'name': '兔子高帽雞蛋燒',
        'address': '台南市永康區中華路382號, Taiwan'
    },
    {
        'name': '越滿樓越式創意料理',
        'address': '408台中市南屯區文心南二路481號, Taiwan'
    },
    {
        'name': 'Fun Tower',
        'address': '台北市中山區南京西路14號 B1, Taiwan'
    },
    {
        'name': '梟FUKUROU',
        'address': '台北市大安區市民大道四段138之3號, Taiwan'
    },
    {
        'name': '湯旺麻辣迴轉火鍋',
        'address': '高雄市左營區明誠二路477號, Taiwan'
    },
    {
        'name': '章魚爆爆 瑞豐總店',
        'address': '瑞豐夜市第三排191號, Taiwan'
    },
    {
        'name': '尚禾手工湯包',
        'address': '台南市安南區國安街53號, Taiwan'
    },
    {
        'name': '黑心地瓜球',
        'address': '台中市西區中興街6號 (騎樓), Taiwan'
    },
    {
        'name': '肉粿',
        'address': '台南市永康區大灣路281號, Taiwan'
    },
    {
        'name': '清水堂',
        'address': '台南市中西區中正路305號, Taiwan'
    },
    {
        'name': '金呷好球',
        'address': '台南市中西區國華街二段210號對面, Taiwan'
    },
    {
        'name': '楊阿公店',
        'address': '台南市東區裕農路288巷94號, Taiwan'
    },
    {
        'name': '水森水產',
        'address': '台中市南屯區大墩十一街165號, Taiwan'
    },
    {
        'name': 'Being Different 手工香水實驗室',
        'address': '新竹縣竹北市勝利六街208號, Taiwan'
    },
    {
        'name': '阿姨蛋餅',
        'address': '高雄市鼓山區鼓山一路17號, Taiwan'
    },
    {
        'name': '築地【樂】厚蛋燒一中店',
        'address': '404台中市北區一中街235號, Taiwan'
    },
    {
        'name': '東大門韓國特色料理',
        'address': '台北市大安區浦城街13巷29號, Taiwan'
    },
    {
        'name': '烤麻糬製造所',
        'address': '高雄市三民區民禮路93號, Taiwan'
    },
    {
        'name': '橫油條',
        'address': '830台灣高雄市鳳山區光復路一段76號, Taiwan'
    },
    {
        'name': '橫油條',
        'address': '高雄市鳳山區光復路一段76號, Taiwan'
    },
    {
        'name': '蔦燒居酒屋',
        'address': '新北市蘆洲區長榮路207號, Taiwan'
    },
    {
        'name': '蔦燒居酒屋',
        'address': '台北市北投區溫泉路30巷24號, Taiwan'
    },
    {
        'name': '蔦燒居酒屋',
        'address': '新北市淡水區新市一路三段143-1號, Taiwan'
    },
    {
        'name': '蔦燒居酒屋',
        'address': '新北市淡水區民權路145巷3號, Taiwan'
    },
    {
        'name': '蔦燒居酒屋',
        'address': '台北市北投區石牌路二段68巷22號, Taiwan'
    },
    {
        'name': '蔦燒居酒屋',
        'address': '台北市士林區中山北路五段505巷42弄1號, Taiwan'
    },
    {
        'name': '芋芋甜點舖',
        'address': '台北市大安區新生南路三段76巷5號, Taiwan'
    },
    {
        'name': '隱家拉麵 芝山店',
        'address': '台北市士林區福華路140號1樓, Taiwan'
    },
    {
        'name': '紅豆麻吉 新海店',
        'address': '新北市板橋區新海路390號, Taiwan'
    },
    {
        'name': 'Toast Chat ',
        'address': '台北市大安區光復南路290巷58號, Taiwan'
    },
    {
        'name': '初幸居食屋',
        'address': '台南市中西區府前路一段124號, Taiwan'
    },
    {
        'name': '岡心食堂',
        'address': '臺北市大安區敦化南路一段190巷43號1樓, Taiwan'
    },
    {
        'name': 'Daruma Saroだるま茶廊',
        'address': '高雄市鼓山區青海路183號, Taiwan'
    },
    {
        'name': 'DAPYNZ 達胖滋',
        'address': '新北市淡水區英專路65號之一, Taiwan'
    },
    {
        'name': '御前上茶 淡水店 宇治抹茶專門店',
        'address': '新北市淡水區中正路一號, Taiwan'
    },
    {
        'name': '舞壽司美味專賣',
        'address': '台南市南區水交社路42號, Taiwan'
    },
    {
        'name': '梨花A5和牛放題',
        'address': '高雄市左營區安吉街468號, Taiwan'
    },
    {
        'name': '正宗韓式炸雞店',
        'address': '高雄市楠梓區大學東路215號, Taiwan'
    },
    {
        'name': 'Truewin初韻 台北饒河店',
        'address': '台北市松山區八德路四段765號, Taiwan'
    },  
]

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

                url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={name}&location={latitude},{longitude}&key={google_api_key}"
                response = requests.get(url)

                if response.status_code == 200:
                    search_results = response.json()
                    if "results" in search_results and search_results["results"]:
            # Extract the details of the first result (assuming it's the best match)
                        place_id = search_results["results"][0]["place_id"]
            
            # Construct the direct link to the restaurant using the place ID
                        link = f"https://www.google.com/maps/place/?q=place_id:{place_id}"
                        restaurant['link'] = link
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
        "link": res["link"]
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
    function initMap() {
      var mapOptions = {
        center: { lat: 23.6978, lng: 120.9605 },  // Centered on Taiwan
        zoom: 8,
      };
      var map = new google.maps.Map(document.getElementById('map'), mapOptions);
      
      // Create markers for restaurants
      var restaurants = {restaurant_data};
      
      restaurants.forEach(function(restaurant) {{
        var position = {{ lat: restaurant.latitude, lng: restaurant.longitude }};
        var marker = new google.maps.Marker({{
          position: position,
          map: map,
          title: restaurant.name,
        }});
        
        // Create an info window for the restaurant
        var contentString = `<div>
          <h3>${restaurant.name}</h3>
          <p>Rating: ${restaurant.rating}</p>
          <a href="${restaurant.link}" target="_blank">View on Google Maps</a>
        </div>`;
        
        var infowindow = new google.maps.InfoWindow({{
          content: contentString,
        }});
        
        // Open the info window when the marker is clicked
        marker.addListener('click', function () {{
          infowindow.open(map, marker);
        }});
      }});
    }
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
with open('ilu.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
