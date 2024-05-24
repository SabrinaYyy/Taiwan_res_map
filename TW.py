

# Define a list of restaurants and their addresses
restaurants = [
    {
        'name': '太一脆皮五花肉-華江店​',
        'address': '新北市板橋區江寧路三段113號'
    },
    {
        'name': '無名關東煮​',
        'address': '新北市淡水區中山北路二段3號'
    },
    {
        'name': '福哥石頭餅​',
        'address': '新北市淡水區清水街9號'
    },
    {
        'name': '德記鍋貼​',
        'address': '新北市淡水區北新路34號'
    },
    {
        'name': '口福早餐店​',
        'address': '新北市淡水區水源街一段129號'
    },
    {
        'name': 'NAGOMI和食饗宴​',
        'address': '台北市大同區南京西路62號4樓'
    },
    {
        'name': '憨仔​',
        'address': '宜蘭縣羅東鎮公正街36號'
    },
    {
        'name': '正谷家​',
        'address': '330桃園市桃園區文中東路79號'
    },
    {
        'name': '集美煎包小籠包​',
        'address': '新北市三重區集美街199號'
    },
    {
        'name': '安格士牛排館樹林店​',
        'address': '220新北市板橋區大觀路三段236號'
    },
    {
        'name': '寶寶屋​',
        'address': '桃園市中壢區大仁五街37號'
    },
    {
        'name': '蝦蝦拉麵 元氣屋​',
        'address': '台中市西區中美街419之4號'
    },
    {
        'name': '天天鐵板燒​',
        'address': '桃園市中壢區龍川五街10號'
    },
    {
        'name': '石頭燒肉 土城館​',
        'address': '新北市土城區中央路三段73號'
    },
    {
        'name': '石頭燒烤 桃園旗艦館​',
        'address': '桃園市桃園區同德五街25號2樓'
    },
    {
        'name': '石頭燒肉 八德旗艦店​',
        'address': '桃園市八德區介壽路二段116號'
    },
    {
        'name': '111鮮蚵白蝦吃到飽​',
        'address': '334桃園市八德區東勇街49號'
    },
    {
        'name': '郁日式豬排​',
        'address': '新北市板橋區華興街78號'
    },
    {
        'name': '上品佑食堂​',
        'address': '宜蘭縣羅東鎮復興路二段111號'
    },
    {
        'name': '坐著做。海鮮丼飯專門店​',
        'address': '320桃園市中壢區大同路186號1樓'
    },
    {
        'name': '墨妃家京品燒肉​',
        'address': '台中市南屯區黎明路二段212號'
    },
    {
        'name': '寶屋​',
        'address': 'No. 6號, Lane 235, Zhongzheng Rd, Shilin District, Taipei City, Taiwan 111'
    },
    {
        'name': '一點酒意·桃花源​',
        'address': '桃園市中壢區大同路105號'
    },
    {
        'name': '青沐​',
        'address': '台北市中山區松江路97巷6號'
    },
    {
        'name': '串燒-殿​',
        'address': '台北市中山區民權東路二段13號'
    },
    {
        'name': '好日子韓酒館​',
        'address': '台北市大安區敦化南路一段233巷59號一樓'
    },
    {
        'name': '川畝園麵食館​',
        'address': '台北市大同區承德路二段1巷31號'
    },
    {
        'name': '川渝小吃坊​',
        'address': '台北市大同區南京西路18巷6弄8之1號'
    },
    {
        'name': '福大蒸餃館​',
        'address': '台北市中山區中山北路一段140巷11號'
    },
    {
        'name': '阿琴蚵嗲​',
        'address': '桃園市八德區廣福路1076號'
    },
    {
        'name': '焦糖楓串燒連鎖第一品牌 師大店​',
        'address': '台北市大安區師大路63號'
    },
    {
        'name': '馬路邊邊串串香 新竹站前店​',
        'address': '新竹市東區林森路2巷9號2F'
    },
    {
        'name': '泰Chill​',
        'address': '桃園市中壢區中山東路四段103號'
    },
    {
        'name': '江陵阿嬤강릉할매韓鍋料理吃到飽​',
        'address': '台北市萬華區西寧南路123號4樓'
    },
    {
        'name': '家常飯朴老師​',
        'address': '台北市信義區忠孝東路五段492巷26號'
    },
    {
        'name': '下大道蘭米糕​',
        'address': '康樂街6號'
    },
    {
        'name': '鐵牛早餐​',
        'address': '五妃街307號'
    },

    {
        'name': '千森製菓​',
        'address': '北區裕民街71號'
    },
    {
        'name': '阿文米粿​',
        'address': '保安路74號'
    },
    {
        'name': '鴨霸當歸鴨​',
        'address': '東區東安路1號'
    },
    {
        'name': '懷舊小棧杏仁豆腐冰​',
        'address': '五妃街206號'
    },
    {
        'name': '小鹿家麵包店​',
        'address': '海東七街49號'
    },
    {
        'name': '麻糬棟​',
        'address': '嘉義縣朴子市第一市場內'
    },
    {
        'name': '萬華小米蛋餅​',
        'address': '台北市萬華區康定路85號'
    },
    {
        'name': '總站夜市蚵蛋燒​',
        'address': '台中市北屯區敦富路與號敦富一街口'
    },
    {
        'name': '好滷舖子 台中精誠店',
        'address': '台中市西區精誠路334號一樓'
    },
    {
        'name': '懶糯糬蘸醬麻糬​',
        'address': '台南市東區建東路79巷939號'
    },
    {
        'name': '老朱店爌肉飯​',
        'address': '台中市西區東興路三段126號'
    },

    {
        'name': '浜江日式燒肉店​',
        'address': '241新北市三重區集賢路150號2樓'
    },
    {
        'name': '員林華成水煎包​',
        'address': '彰化縣員林市育英路428號'
    },
    {
        'name': '愛柒AiChi​',
        'address': '台中市西區健行路1049號3樓'
    },
    {
        'name': '隔壁飯糰​',
        'address': '台南市東區東平路164號'
    },
    {
        'name': '丸南生魚片​',
        'address': '台中市南屯區環中路四段2號第一攤'
    },
    {
        'name': '德興路早餐店​',
        'address': '台中市大甲區德興路125號'
    },
    {
        'name': '板橋高記生炒魷魚​',
        'address': '新北市板橋區宮口街28號'
    },
    {
        'name': '荷李活茶街​',
        'address': '台北市大安區忠孝東路四段45號2樓'
    },
    {
        'name': '豬一十五​',
        'address': '新竹縣竹北市三民路355號'
    },
    {
        'name': '呷知味​',
        'address': '台南市善化區中山路429號'
    },
    {
        'name': '二月牌沙茶爐​',
        'address': '新北市新莊區中華路二段103號'
    },
    {
        'name': 'Tart Space派塔空間甜點工作室​',
        'address': '新北市三重區安慶街165號1樓'
    },
    {
        'name': '借問酸辣粉 (外帶店)​',
        'address': '302新竹縣竹北市東興路一段416號'
    },
    {
        'name': '飲居​',
        'address': '桃園市大園區青昇路一段91巷121號'
    },
    {
        'name': '旭集 中茂店​',
        'address': '桃園市桃園區同德五街61號12樓（中茂新天地12樓'
    },
    {
        'name': '吾食Our Brunch​',
        'address': '桃園市桃園區寶慶路82號'
    },
    {
        'name': 'FÉ COFFEE​',
        'address': '320桃園市中壢區永平街67號'
    },
    {
        'name': '一和壽叔SUSHI BENTO​',
        'address': '高雄市左營區富國路290號1樓'
    },
    {
        'name': '廣閤珍饌鍋物​',
        'address': '桃園市中壢區九和一街18號2樓'
    },
    {
        'name': '花韓燒(高雄skm park店​',
        'address': '高雄市前鎮區中安路1-1號3樓'
    },
    {
        'name': '好飯糰DAILY NICE BALL​',
        'address': '330桃園市桃園區民權路46號'
    },
    {
        'name': '感丼現食​',
        'address': '高雄市鳳山區南正二路27號'
    },
    {
        'name': '感丼現食​',
        'address': '高雄市鳳山區文衡路11號'
    },
    {
        'name': '饗和牛​',
        'address': '330, Taiwan, Taoyuan City, Taoyuan District, Fuxing Rd, 83號2樓'
    },
    {
        'name': '老郭專業米腸包香腸​',
        'address': '新竹縣竹北市縣政三街17號'
    },
    {
        'name': '橫油條創意美食​',
        'address': '高雄市鳳山區中正路87號'
    },
    {
        'name': '白狐院華夫餅 흰여우와플​',
        'address': '台北市信義區虎林街119之17號1樓'
    },
    {
        'name': '可以可以地瓜球 吉林店​',
        'address': '高雄市三民區吉林街169號'
    },
    {
        'name': 'Coconut Sugar 南洋餐事​',
        'address': '台北市中山區龍江路106巷6號'
    },
    {
        'name': '品帝王蟹火鍋Omakase​',
        'address': '台北市中山區新生北路一段152號'
    },
    {
        'name': '飯糰霸​',
        'address': '台北市中正區許昌街2號'
    },
    {
        'name': '京厚屋 逢甲店​',
        'address': '台中市西屯區河南路二段255-1號'
    },
    {
        'name': '阿豬嘻烤肉村​',
        'address': '台北市萬華區峨眉街28號3樓'
    },
    {
        'name': '堺坊 shabu shabu 有機農場​',
        'address': '新竹縣竹北市光明二街79號'
    },
    {
        'name': '小歐圓炭烤雞腿排飯​',
        'address': '高雄市苓雅區苓雅二路166號'
    },
    {
        'name': '容燒居酒屋​',
        'address': '新北市板橋區中山路一段301號'
    },
    {
        'name': '參堂居酒屋​',
        'address': '新北市板橋區雙十路二段42-4號1樓'
    },
    {
        'name': '吾時食 5 10 10牛肉麵​',
        'address': '新北市板橋區公館街58號'
    },
    {
        'name': 'Bee\'s Knees彼斯尼​',
        'address': '台北市士林區大北路8號'
    },
    {
        'name': '轉雞炸物專賣店',
        'address': '桃園市龜山區復興北路6巷21號'
    },
    {
        'name': '淡水酒肉x與溪谷',
        'address': '大稻埕碼頭貨櫃市集'
    },
    {
        'name': '美天餐室​',
        'address': '台北市中山區中山北路二段84巷6號一樓'
    },
    {
        'name': '串燒殿 天母殿 / 極盛',
        'address': '台北市士林區天母西路53號'
    },
    {
        'name': '食尚吃到飽涮涮鍋',
        'address': '235新北市中和區員山路391號'
    },
    {
        'name': '美式木柴烤肉屋​',
        'address': '115台北市南港區南港路一段255號'
    },
    {
        'name': '韓金量​',
        'address': '台中市北區三民路三段164巷'
    },
    {
        'name': '梨谷韓式鐵板炭火烤肉',
        'address': '台北市信義區忠孝東路五段699號'
    },
    {
        'name': '屋伴餃子 WOOPAN​',
        'address': '台北市士林區大北路8號'
    },
    {
        'name': '鴻發饗食堂 ',
        'address': '新北市蘆洲區九芎街59號1樓'
    },
    {
        'name': '豐雞號',
        'address': '新北市蘆洲區長榮路148號1樓'
    },
    {
        'name': '開封府捲餅',
        'address': '台北市中正區開封街一段2號'
    },

    {
        'name': '古早味阿嬤手工肉圓',
        'address': '台中市北區青島路二段89號'
    },
    {
        'name': '提拉米蘇精緻蛋糕臺南店',
        'address': 'No. 97號, Section 1, Changrong Rd, East District, Tainan City, Taiwan 701'
    },
    {
        'name': '渣壽司sushi 瑞隆店',
        'address': '高雄市前鎮區瑞隆路220號'
    },
    {
        'name': '渣壽司sushi 仁武店',
        'address': '高雄市仁武區仁雄路29號101文具前'
    },
    {
        'name': '渣壽司sushi 金鼎店',
        'address': '高雄市三民區金鼎路291號'
    },
    {
        'name': 'PAI CAFÉ & BRUNCH',
        'address': '台北市松山區八德路二段366巷11號'
    },
    {
        'name': '品益合樂屋',
        'address': '高雄市前金區自強三路267號'
    },
    {
        'name': '金洹苑-日式燒肉火鍋吃到飽',
        'address': '台北市大安區延吉街131巷31號'
    },
    {
        'name': '麥仕佳烘焙坊-台中漢口店',
        'address': '台中市北區漢口路4段220號'
    },
    {
        'name': '波記茶餐廳',
        'address': '台北市大安區延吉街70巷8號'
    },
    {
        'name': 'JAG這個·浮洲',
        'address': '新北市板橋區大觀路一段29巷35號'
    },
    {
        'name': '小日秀秀',
        'address': '高雄市三民區鼎中路85號'
    },
    {
        'name': 'Neko coffee 貓珈',
        'address': '台北市信陽街9號2樓'
    },
    {
        'name': 'W.Bistro',
        'address': '300新竹市東區仁愛街87巷1號'
    },
    {
        'name': '阿裕壽司',
        'address': '台中市北區西屯路一段361號'
    },
    {
        'name': '沁玥食堂',
        'address': '高雄市三民區建興路243號'
    },
    {
        'name': '阿得飯店',
        'address': '高雄市鳳山區鳳松路124號'
    },
    {
        'name': '邊境串燒',
        'address': '桃園市中壢區環北路439號'
    },
    {
        'name': '馬的深夜食堂',
        'address': '新竹市東區民生路255號'
    },
    {
        'name': '回巢 Homing',
        'address': '宜蘭礁溪大塭路18-17號'
    },
    {
        'name': '捲餅達人',
        'address': '台北市信義區永吉路30巷104號'
    },
    {
        'name': 'Punjabi Grill 旁賈彼印度料理',
        'address': '桃園市中壢區新中北路378號'
    },
    {
        'name': '春潮商社',
        'address': '桃園市中壢區實踐路223號2樓'
    },
    {
        'name': 'CU 部隊鍋',
        'address': '桃園市中壢區大仁五街40號'
    },
    {
        'name': '有吉豐盛丼專門店',
        'address': '台北市大安區復興南路一段107巷5弄15號1樓'
    },
    {
        'name': '大溪·大溪港式點心',
        'address': '桃園市大溪區登龍路88巷19號'
    },
    {
        'name': '阿霞吃阿婆炸年糕',
        'address': '台南市北區公園路862巷'
    },
    {
        'name': '村豚拉麵',
        'address': '高雄市鳳山區五權南路226號'
    },
    {
        'name': '一隻熊甜點森林 沙鹿店',
        'address': '台中市沙鹿區鎮南路二段620號'
    },
    {
        'name': '米玥麻糬堂 – 台北大安店',
        'address': '台北市大安區大安路一段22號'
    },
    {
        'name': 'C’est Bon十分粉圓',
        'address': '台中市北區育強街119號'
    },
    {
        'name': '新莊黛比鹹粥',
        'address': '新北市新莊區中和街5號'
    },
    {
        'name': '信兵衛南門町目三代店',
        'address': '台中市南區南門路1號'
    },
    {
        'name': '天皇壽司',
        'address': '台中市大里區仁化路567號仁化黃昏市場'
    },
    {
        'name': '老串角居酒屋-江子翠本店',
        'address': '新北市板橋區文化路二段182巷7弄15號'
    },
    {
        'name': '金香豬腳涼麵',
        'address': '台北市中山區錦州街253-1號'
    },
    {
        'name': '香炬居酒屋',
        'address': '新北市板橋區莒光路200巷35號'
    },
    {
        'name': '二鍋頭東山鴨頭-精誠店',
        'address': '台中市西區精誠路131號'
    },
    {
        'name': '藍海子 Lazy Brunch-板橋美食',
        'address': '新北市板橋區仁化街98號1樓'
    },
    {
        'name': '小樂涼冰果室',
        'address': '台中市大甲區孔雀路100號'
    },
    {
        'name': 'アツアツ（ㄚㄗㄚㄗ）章魚燒',
        'address': '台北市中山區中山北路一段83巷11-2號'
    },
    {
        'name': '越好吃',
        'address': '台中市大里區大明路162號'
    },
    {
        'name': '妝兜花了',
        'address': '桃園市平鎮區南京路127號'
    },
    {
        'name': '中央市場糯米水餃',
        'address': '新竹市北區西門街2巷2號92攤'
    },
    {
        'name': '麵大廚（延吉店）',
        'address': '臺北市大安區延吉街70巷2弄1號'
    },
    {
        'name': 'NiNi小鬆餅',
        'address': '台中市南區復興園路33號'
    },
    {
        'name': '小媳婦鐵鍋燉',
        'address': '高雄市左營區華夏路983號'
    },
    {
        'name': '佐一茶屋',
        'address': '嘉義縣阿里山鄉樂野村一鄰2號附9'
    },
    {
        'name': '論石間鍋物',
        'address': '台中市西屯區西屯路三段166-70號'
    },
    {
        'name': '泉威布丁豆花 友愛分店',
        'address': '台南市中西區友愛街164號'
    },
    {
        'name': '大湖口火鍋城',
        'address': '新竹縣湖口鄉中山路一段508號'
    },
    {
        'name': '川辛拌味麵-大墩創始店',
        'address': 'No. 957號, Dadun Rd, Xitun District, Taichung City, Taiwan 40758'
    },
    {
        'name': '大腸包小腸',
        'address': '新北市永和區永平路81巷3號'
    },
    {
        'name': '熱那亞義式冰淇淋',
        'address': '台北市大同區延平北路一段66巷17號1樓'
    },
    {
        'name': '老主顧炭燒紅蟳薑母鴨總店',
        'address': '台北市中山區民權東路二段67號'
    },
    {
        'name': '芳塢碼頭專業麻糬',
        'address': '台中市東區建新街48號'
    },
    {
        'name': '一煥關東煮',
        'address': '台南市東區育樂街109號'
    },
    {
        'name': '創作麵坊・鮭の大助',
        'address': '403台中市西區向上路一段170號'
    },
    {
        'name': '饗食天堂',
        'address': '台中市東區進德路700號南館3樓'
    },
    {
        'name': '元之寶',
        'address': '台北市萬華區漢口街二段34巷13號'
    },
    {
        'name': '星夢森林劇場',
        'address': '宜蘭縣冬山鄉境安二路321號'
    },
    {
        'name': 'Lady nara曼谷新泰式料理',
        'address': '台北市南港區忠孝東路七段299號C棟10樓'
    },
    {
        'name': '私炑炭火燒肉',
        'address': '台南市中西區海安路二段303號'
    },
    {
        'name': '啡蒔 Verse Cafe by Minorcode',
        'address': '桃園市桃園區同德十一街45號'
    },
    {
        'name': 'Deerher甜點廚坊',
        'address': '彰化縣和美鎮線東路二段712號'
    },
    {
        'name': '咖啡任務 — 總部',
        'address': '台中市南區忠明南路787號36F'
    },
    {
        'name': '陳記鹹酥雞',
        'address': '桃園市中壢區中園路100號'
    },
    {
        'name': '麵屋 壓軸',
        'address': '台南市中西區新美街146號'
    },
    {
        'name': '百合穀室',
        'address': '台南市中西區西門路一段709號'
    },
    {
        'name': '旭暮 mu café',
        'address': '台中市西區民生北路126號B1'
    },
    {
        'name': '雞湯榮麵食館',
        'address': 'No. 14號, Jinzhou St, Zhongshan District, Taipei City, Taiwan 104'
    },
    {
        'name': '路易奇電力公司 復興電廠',
        'address': '106, Taiwan, Taipei City, Da’an District, Lane 79, Section 1, Fuxing S Rd, 4弄4號1樓'
    },
    {
        'name': '路易奇電力公司 中山第一電廠',
        'address': '104, Taiwan, Taipei City, Zhongshan District, Lane 83, Section 1, Zhongshan N Rd, 9之5號1 樓'
    },
    {
        'name': '路易奇電力公司 市民電廠',
        'address': 'No. 72號 1, Section 4, Civic Blvd, Da’an District, Taipei City, Taiwan 106'
    },
    {
        'name': '川麵道',
        'address': '台中市北屯區昌平路一段250號'
    },
    {
        'name': '夯下去新潮和牛燒肉',
        'address': '新竹市東區經國路一段673-1號1F'
    },
    {
        'name': '台北鳥喜 produced by Toriki とり喜',
        'address': '臺北市中山區樂群二路199號2樓'
    },
    {
        'name': 'Supple Coffee',
        'address': '台中市南區文心南路901巷8號1樓'
    },
    {
        'name': '台北西門 宏益水晶餃',
        'address': '台北市萬華區昆明街184之2號'
    },
    {
        'name': '小鵲sing 紅豆餅',
        'address': '新竹縣竹北市福興東路二段85號'
    },
    {
        'name': '時辣苑',
        'address': '桃園市中壢區環北路210號'
    },
    {
        'name': 'Home燒肉 逢甲店',
        'address': '台中市西屯區河南路二段256號'
    },
    {
        'name': 'Home燒肉 綠園道店',
        'address': '台中市西區五權六街 59號'
    },
    {
        'name': 'Home燒肉 永春店',
        'address': '台中市南屯區永春東七路845號2F'
    },
    {
        'name': '海福鹽滷製豆製所',
        'address': '台中市西屯區天水西六街42號'
    },
    {
        'name': '撈月麵館',
        'address': '新北市新莊區新泰路488號'
    },
    {
        'name': 'JT吉蒂牛排',
        'address': '桃園市中壢區民權路四段506號'
    },
    {
        'name': '一隅 居酒屋',
        'address': '台北市中山區四平街20號1樓'
    },
    {
        'name': '高沐手作料理',
        'address': '台中市北區太平路19巷3弄15號'
    },
    {
        'name': '58石磨玉米餅',
        'address': '宜蘭縣羅東鎮公園路148號'
    },
    {
        'name': '家溫體鍋物',
        'address': '台南市北區和緯路二段330號'
    },
    {
        'name': '瀧厚炙燒熟成牛排',
        'address': '台中市西屯區永福路172號'
    },
    {
        'name': '楊婆婆麵粉煎豆花',
        'address': '宜蘭市神農路二段3號'
    },
    {
        'name': '鴨點棧',
        'address': '807高雄市三民區明誠二路76-1號'
    },
    {
        'name': '阿利珈多',
        'address': '台中市北區永興街98巷14號'
    },
    {
        'name': '麟咖啡Lin Coffee',
        'address': '台中市西區美村路一段299號'
    },
    {
        'name': '金衛亭浮誇壽司樂群町二代目 South district branch',
        'address': '台中市西區樂群街439號, Taiwan'
    },
    {
        'name': '饗 A Joy',
        'address': '110, Taiwan, Taipei City, Xinyi District, Section 5, Xinyi Rd, 7號86樓'
    },
    {
        'name': '哼！燒肉 五常店',
        'address': '台中市北區五常街51號, Taiwan'
    },
    {
        'name': 'SUNWAY',
        'address': '108台湾台北市萬華區貴陽街二段116號'
    },
    {
        'name': '饕串烧酒场',
        'address': '500台湾彰化縣彰化市永樂街213號, Taiwan'
    },
    {
        'name': '麒麟創作拉麵',
        'address': '台北市中山區中山北路一段140巷25號, Taiwan'
    },
    {
        'name': '初魚鮨 富錦',
        'address': '台北市松山區富錦街448號, Taiwan'
    },
    {
        'name': '梨谷-韓式鐵板炭火烤肉',
        'address': '台北市信義區忠孝東路五段699號, Taiwan'
    },
    {
        'name': '慕十里韓式燒肉',
        'address': '台南市東區裕農路1036號, Taiwan'
    },
    {
        'name': 'Fermi Pasta',
        'address': '台北市大安區復興南路一段107巷5弄14號, Taiwan'
    },
    {
        'name': '菁饌海鮮涮涮鍋',
        'address': '406台中市北屯區旅順路二段298號, Taiwan'
    },
    {
        'name': '一路發綠豆沙',
        'address': '台中市大甲區蔣公路133號, Taiwan'
    },
    {
        'name': '火影忍者一樂拉麵',
        'address': '新竹市北區大雅路88號2樓, Taiwan'
    },
    {
        'name': '山林冰果店',
        'address': '屏東縣屏東市林森路48-1號, Taiwan'
    },
    {
        'name': '鄭家粉圓50年老店',
        'address': '高雄市前金區六合二路137號, Taiwan'
    },
    {
        'name': '曾家古早味剉冰',
        'address': '高雄市鹽埕區大禮街20號, Taiwan'
    },
    {
        'name': '芮妮法式手作甜點',
        'address': '台南市東區中華東路一段366號, Taiwan'
    },
    {
        'name': '肉次方',
        'address': '406台中市北屯區文心路四段585號1樓, Taiwan'
    },
    {
        'name': '猜心泡芙',
        'address': '高雄市苓雅區泰順街60號1樓, Taiwan'
    },
    {
        'name': '長勝君捲蛋餅',
        'address': '臺北市松山區興安街171號後間, Taiwan'
    },
    {
        'name': 'P.Ming泰式廚坊',
        'address': '台北市內湖區內湖路一段600巷2號, Taiwan'
    },
    {
        'name': '隔壁宵夜 台中大里店',
        'address': '台中市大里區成功路485號, Taiwan'
    },
    {
        'name': '格林小鎮',
        'address': '新竹市東區自由路27巷43號, Taiwan'
    },
    {
        'name': '白妞鹹酥雞-總店',
        'address': '台南市中西區民族路二段270號, Taiwan'
    },
    {
        'name': '綆粽林',
        'address': '雲林縣北港鎮中正路83號, Taiwan'
    },
    {
        'name': '海饕-四季主流宴',
        'address': '宜蘭縣頭城鎮濱海路二段562號, Taiwan'
    },
    {
        'name': '森麵堂 M.M Taipei',
        'address': '台北市大安區東豐街52號1樓, Taiwan'
    },
    {
        'name': '韓味食足',
        'address': '高雄市鳳山區成功路22號, Taiwan'
    },
    {
        'name': '津富倉',
        'address': '台北市萬華區萬大路495號（7-11旁）, Taiwan'
    },
    {
        'name': '紅磚園邸',
        'address': '新北市樹林區太平路247巷9號, Taiwan'
    },
    {
        'name': '馮姊姊飯糰',
        'address': '新竹縣竹北市光明一路402號, Taiwan'
    },
    {
        'name': '饃饃噠心動肉夾饃 台北站前店',
        'address': '台北市中正區信陽街5號1樓, Taiwan'
    },
    {
        'name': 'La Piada',
        'address': '163-11號南京東路五段松山區台北市105, Taiwan'
    },
    {
        'name': '蝦King活蝦料理',
        'address': '30054台湾新竹市北區中正路283號, Taiwan'
    },
    {
        'name': '武賀甲頂級燒肉吃到飽',
        'address': '新竹縣竹北市勝利十一路153號, Taiwan'
    },
    {
        'name': '時覓sumi 海鮮丼飯專門店',
        'address': '新竹市平和街32號, Taiwan'
    },
    {
        'name': '馬的生食丼',
        'address': '302台湾新竹縣竹北市縣政二路460號, Taiwan'
    },
    {
        'name': '和食川上',
        'address': '新竹市東區西門街1號2樓, Taiwan'
    },
    {
        'name': '麒麟拉麵創作坊',
        'address': '台北市中山區中山北路一段140巷25號, Taiwan'
    },
    {
        'name': '全旺蔥餅條',
        'address': '高雄市苓雅區苓雅二路101號, Taiwan'
    },
    {
        'name': '上海生煎包',
        'address': '高雄市三民區熱河一街208號, Taiwan'
    },
    {
        'name': '旗山紅糟肉',
        'address': '高雄市旗山區延平一路435號, Taiwan'
    },
    {
        'name': '無名麵店',
        'address': '高雄市苓雅區英明路240號, Taiwan'
    },
    {
        'name': '燒肉政宗',
        'address': '臺北市大安區忠孝東路四段101巷7號, Taiwan'
    },
    {
        'name': '明燒肉文自旗艦店',
        'address': '高雄市左營區文自路559號, Taiwan'
    },
    {
        'name': '鬥牛士二鍋桃園食尚店',
        'address': '桃園市桃園區中正路47號5樓, Taiwan'
    },
    {
        'name': '正香滷味',
        'address': '新竹市北區光華北街81號, Taiwan'
    },
    {
        'name': '逸茶酒室Golden bar',
        'address': '224台湾新北市瑞芳區基山街190號, Taiwan'
    },
    {
        'name': '玩味雞湯事務所',
        'address': '新竹市北區光華東街84號, Taiwan'
    },
    {
        'name': '麵宮浦島',
        'address': '新竹市北區北大路166巷65號, Taiwan'
    },
    {
        'name': '横浜家系ラーメン拉麵家',
        'address': '新竹市東區民生路119號, Taiwan'
    },
    {
        'name': 'ラーメン 鷄白湯',
        'address': '新竹市北區世界街1114號, Taiwan'
    },
    {
        'name': '柒餓食肆',
        'address': '新竹市北區大同路112號, Taiwan'
    },
    {
        'name': 'Tom&Maggy 幸福肥 • 手作點心',
        'address': '新北市三重區集美街33巷20號, Taiwan'
    },
    {
        'name': '神來一爐(永和店)',
        'address': '新北市永和區中正路492號, Taiwan'
    },
    {
        'name': 'FUN锅子',
        'address': '231新北市新店區二十張路1巷2弄8號, Taiwan'
    },
    {
        'name': '明水然・乐-信义松烟店',
        'address': '110台湾台北市信義區忠孝東路四段553巷6弄16號, Taiwan'
    },
    {
        'name': '近百樓美景咖啡廳 - Simple Kaffa Sola',
        'address': '110台北市信義區信義路五段7號88樓, Taiwan'
    },
    {
        'name': '海灣綠洲',
        'address': '新北市石門區楓林25-1號, Taiwan'
    },
    {
        'name': '鹿點咖啡Luna',
        'address': '桃園市桃園區成功路三段175號, Taiwan'
    },
    {
        'name': '夏夕夏景',
        'address': '桃園市龍潭區楊銅路二段588之1號, Taiwan'
    },
    {
        'name': 'Sylvie森林甜點',
        'address': '新北市板橋區文化路一段233號, Taiwan'
    },
    {
        'name': '島入冰店',
        'address': '台南市中西區民族路二段208巷9號, Taiwan'
    },
    {
        'name': '帕司達義式料理',
        'address': '新北市三峽區大觀路18號, Taiwan'
    },
    {
        'name': '燒鳩 刺身·串燒·夜食',
        'address': '台北市松山區市民大道四段85號, Taiwan'
    },
    {
        'name': '阿鴻串烤',
        'address': '台北市中山區五常街53巷17號, Taiwan'
    },
    {
        'name': '根萊鐵板燒',
        'address': '108台北市萬華區昆明街92號之1號B1, Taiwan'
    },
    {
        'name': '台韓民國 韓式燒肉店',
        'address': '106台北市大安區忠孝東路四段170巷6弄7號, Taiwan'
    },
    {
        'name': '温咖哩',
        'address': '台北市中正區濟南路二段3之8號, Taiwan'
    },
    {
        'name': '金水冷飲部',
        'address': '台南市新化區信義路227號, Taiwan'
    },
    {
        'name': '月月泰BBQ 遠百信義店',
        'address': '台北市信義區松仁路𝟧𝟪號𝟣𝟦樓 (信義區 遠東百貨𝖠𝟣𝟥), Taiwan'
    },
    {
        'name': '悄悄杯居酒屋The Cup',
        'address': '台北市松山區市民大道四段225號, Taiwan'
    },
    {
        'name': 'K TOWN',
        'address': '台北市大安區市民大道四段10號, Taiwan'
    },
    {
        'name': '裏月晴酒',
        'address': '新竹縣竹北市北崙里縣政十三路101號, Taiwan'
    },
    {
        'name': '滝禾製麵所-新竹新莊店',
        'address': '新竹市東區新莊街153號, Taiwan'
    },
    {
        'name': 'In Soul Studio',
        'address': '桃園市中壢區中央西路二段245號, Taiwan'
    },
    {
        'name': '紅玥緬因貓藝廊',
        'address': '103台北市大同區赤峰街71巷4號, Taiwan'
    },
    {
        'name': '艾摩多手工杏仁豆腐',
        'address': '台南市中西區赤崁東街26號, Taiwan'
    },
    {
        'name': '王福芋圓',
        'address': '台北市萬華區峨眉街5-2號, Taiwan'
    },
    {
        'name': '冷台北行天宮附設玄空圖書館',
        'address': '台北市北投區中央北路四段18巷48號, Taiwan'
    },
    {
        'name': '冷藏肉專門 鍋無敵 光復店',
        'address': '台北市大安區光復南路290巷53號, Taiwan'
    },
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
    {
        'name': '無所不包自助早餐吃到飽',
        'address': '新北市三重區大智街157號, Taiwan'
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
google_api_key = 

# Initialize the Google Maps client
gmaps_client = googlemaps.Client(key=google_api_key)

# Initialize gmaps for displaying the results on a map
gmaps.configure(api_key=google_api_key)

#######################################################
#reviews for restaurants
# Initialize the Sentiment Intensity Analyzer from NLTK
#nltk.download('vader_lexicon')  # Download the necessary data for VADER
#sia = SentimentIntensityAnalyzer()

# Define a function to fetch reviews for a restaurant
#def get_reviews_for_restaurant(place_id):
    # Define the Google Places API URL
#    urlr = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,review,rating&key={google_api_key}'

    # Make the GET request to the API
#    response = requests.get(urlr)

#    if response.status_code == 200:
#        data = response.json()
#        if 'result' in data:
#            result = data['result']
#            name = result['name']
#            reviews = result.get('reviews', [])

#            textblob_scores = []
#            vader_scores = []

#            print(f"Name: {name}")
#            print("Reviews_number:", len(reviews))#### only have 5 reviews for each place
#            for review in reviews:
#                rating = review['rating']
#                text = review['text']
#                print(f"Rating: {rating}")
#                print(f"Review: {text}")


                # Perform sentiment analysis using TextBlob
#                analysis = TextBlob(text)
#                textblob_sentiment = analysis.sentiment.polarity

                # Perform sentiment analysis using NLTK's Sentiment Intensity Analyzer (VADER)
#                vader_sentiment = sia.polarity_scores(text)['compound']

#                textblob_scores.append(textblob_sentiment)
#                vader_scores.append(vader_sentiment)


                # You can add your own logic here to analyze sentiments further

            # Calculate the average sentiment scores for TextBlob and VADER
#            try:
#                average_textblob_score = sum(textblob_scores) / len(textblob_scores)
#                average_vader_score = sum(vader_scores) / len(vader_scores)

                # Print the summary
#                print(f"Average TextBlob Sentiment: {average_textblob_score}")
#                print(f"Average VADER Sentiment: {average_vader_score}\n")
#                if average_textblob_score < 0.3 or average_vader_score < 0.5:
#                    return 'low rating in reviews'
#                elif 0.2 < average_textblob_score < 0.7 and 0.2 < average_vader_score < 0.7:
#                    return 'fine rating in reviews'
#                else:#one of the score above 0.7 and both above 0.2
#                    return 'worth to go'
#            except ZeroDivisionError:
#                print(f"No reviews found for {restaurant['name']}")

#        else:
#            print("Place not found.")
#    else:
#        print(f"Failed to retrieve data for Place ID: {place_id}")



#####################################################################
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
                        elif "hotel" in type_place:
                            type_place = "hotel"
                        else:
                            type_place = "other"
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
        "type": res["type"]
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
        } else {
            iconColor = 'orange'; // If it's not a restaurant or hotel, set the label color to orange
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
with open('ilu2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
