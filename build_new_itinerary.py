import json
import os

hotel_data = {
    "name": "노보텔 뮌헨 시티 아르눌프파크 (우리 숙소)",
    "nameDe": "Novotel München City Arnulfpark",
    "lat": 48.1454917,
    "lng": 11.5389985,
    "address": "Arnulfstraße 57, 80636 München",
    "googleMapsUrl": "https://maps.app.goo.gl/LNwTawdtw64NZc248",
    "desc": "이번 뮌헨 여행의 베이스캠프! Donnersbergerbrücke S-Bahn역 및 트램(16, 17번) 도보 2분. 중앙역 SIXT 렌터카, 마리엔 광장, 님펜부르크 궁전 이동 최적.",
    "tip": "호텔 바로 앞 트램 17번을 타면 중앙역(SIXT) 및 님펜부르크 궁전까지 환승 없이 5~15분 직통 이동!"
}

itinerary_data = [
  {
    "day": 1,
    "dayLabel": "20일 (1일차)",
    "title": "20일: BMW 테크 & 올림피아 피크닉, 구시가지 쇼핑 & 감성 산책",
    "summary": "BMW 미래 기술 관람 후 대학가 베이커리/카페에서 빵과 커피를 사서 올림피아 언덕 피크닉! 오후엔 구시가지 성당, 활기찬 야외 시장, 달마이어 본점, 17시 인형극, 막스마라 & 퓐프 회페 쇼핑 및 내일 로드트립 간식 구비",
    "color": "#2563eb",
    "transitTip": "대중교통: 뮌헨 시내 M구역 1일권 (U-Bahn, 트램, 버스 무제한) 이용 권장",
    "googleRouteUrl": "https://www.google.com/maps/dir/BMW+Welt/BMW+Museum/Studentenstadt+Olympisches+Dorf/Olympiapark/Marienplatz/Viktualienmarkt/Alois+Dallmayr/Neues+Rathaus/Max+Mara/F%C3%BCnf+H%C3%B6fe",
    "spots": [
      {
        "id": "d1-1",
        "day": 1,
        "num": 1,
        "period": "오전",
        "time": "09:00 - 10:00",
        "name": "BMW 벨트 (BMW Welt)",
        "nameDe": "BMW Welt München",
        "lat": 48.1770,
        "lng": 11.5560,
        "category": "전시 / 복합문화공간",
        "desc": "소용돌이 형태의 미래지향적 건물에 BMW, MINI, 롤스로이스의 최신 라인업이 전시된 첨단 쇼룸입니다. 무료입장이며 시승 및 포토존이 다채롭습니다.",
        "tip": "아침 9시 개장 직후 입장하면 여유롭게 신차 탑승 사진을 남길 수 있습니다."
      },
      {
        "id": "d1-2",
        "day": 1,
        "num": 2,
        "period": "오전",
        "time": "10:00 - 11:00",
        "name": "BMW 뮤지엄 (BMW Museum)",
        "nameDe": "BMW Museum",
        "lat": 48.1764,
        "lng": 11.5591,
        "category": "박물관",
        "desc": "사발(Bowl) 모양 랜드마크 건물로, 100년이 넘는 BMW의 모터사이클, 클래식 레이싱 카, 엔진 혁신의 역사를 나선형 슬로프를 따라 감상합니다.",
        "tip": "BMW Welt에서 구름다리 육교를 통해 바로 연결됩니다."
      },
      {
        "id": "d1-3",
        "day": 1,
        "num": 3,
        "period": "오전~점심",
        "time": "11:00 - 12:00",
        "name": "올리도르프(Olydorf) 대학가 베이커리 & 카페",
        "nameDe": "Studentenstadt Olympisches Dorf Café & Bäckerei",
        "lat": 48.1795,
        "lng": 11.5535,
        "category": "대학가 카페 / 베이커리",
        "desc": "선수촌을 개조한 올림픽 빌리지 학생촌입니다. 학생들이 개성 있게 꾸민 독창적인 외벽 벽화를 구경하며, 주변 로컬 베이커리와 카페에서 갓 구운 독일 빵과 따뜻한 커피를 테이크아웃합니다.",
        "tip": "피크닉용 브레첼, 크루아상, 샌드위치와 커피를 챙겨 바로 옆 올림피아 언덕으로 이동하세요."
      },
      {
        "id": "d1-4",
        "day": 1,
        "num": 4,
        "period": "점심~오후",
        "time": "12:00 - 13:30",
        "name": "올림피아 파크 언덕 피크닉 & 호숫가 산책",
        "nameDe": "Olympiapark München Picknick & Olympiaberg",
        "lat": 48.1731,
        "lng": 11.5466,
        "category": "공원 피크닉 / 힐링 산책",
        "desc": "테이크아웃한 맛있는 빵과 커피를 들고 올림픽 힐(Olympiaberg) 잔디밭에 앉아 여유로운 브런치 피크닉을 즐깁니다. 텐트형 스타디움과 뮌헨 시내 전경을 감상하며 힐링 산책!",
        "tip": "언덕 위에서 탁 트인 전경을 바라보며 시차 적응과 여독을 가볍게 풀기 좋습니다."
      },
      {
        "id": "d1-5",
        "day": 1,
        "num": 5,
        "period": "오후",
        "time": "14:00 - 14:50",
        "name": "마리엔 광장 & 프라우엔키르헤",
        "nameDe": "Marienplatz & Frauenkirche",
        "lat": 48.1386,
        "lng": 11.5732,
        "category": "역사 광장 & 대성당",
        "desc": "U-Bahn U3을 타고 시내 중심으로 이동! 뮌헨의 심장 마리엔 광장과 두 개의 돔 탑이 솟은 프라우엔키르헤 대성당 바닥의 전설적인 '악마의 발자국'을 관람합니다.",
        "tip": "성당 입구 악마의 발자국 위치에 서면 기둥에 가려 창문이 보이지 않는 신비한 구조를 직접 확인해보세요."
      },
      {
        "id": "d1-6",
        "day": 1,
        "num": 6,
        "period": "오후",
        "time": "14:50 - 15:40",
        "name": "빅투알리엔 마켓 (Viktualienmarkt)",
        "nameDe": "Viktualienmarkt",
        "lat": 48.1351,
        "lng": 11.5760,
        "category": "전통 야외 시장",
        "desc": "200년 전통의 활기찬 야외 식료품 시장입니다. 신선한 과일, 치즈, 바이에른 소시지, 향신료 부스를 구경하고 마이바움(오월제 기둥) 아래 비어가든의 활기찬 분위기를 느낍니다.",
        "tip": "생과일 주스나 치즈 한 조각을 간식으로 맛보기 좋습니다."
      },
      {
        "id": "d1-7",
        "day": 1,
        "num": 7,
        "period": "오후",
        "time": "15:45 - 16:35",
        "name": "달마이어 본점 (Dallmayr Delikatessenhaus)",
        "nameDe": "Alois Dallmayr Delikatessenhaus",
        "lat": 48.1382,
        "lng": 11.5768,
        "category": "왕실 납품 프리미엄 식료품점",
        "desc": "300년이 넘는 전통을 자랑하는 바이에른 왕실 공식 납품 프리미엄 델리카트슨 본점입니다. 명품 원두커피(Prodomo), 핸드메이드 초콜릿, 잼, 티 등 독일 최고급 미식 선물의 성지입니다.",
        "tip": "노란 틴케이스에 담긴 달마이어 시그니처 원두와 초콜릿은 지인 선물용으로 실패가 없습니다."
      },
      {
        "id": "d1-8",
        "day": 1,
        "num": 8,
        "period": "오후",
        "time": "16:50 - 17:20",
        "name": "신시청 인형극 관람 (Glockenspiel - 17시 정각)",
        "nameDe": "Neues Rathaus Glockenspiel",
        "lat": 48.1375,
        "lng": 11.5754,
        "category": "시계탑 인형극 공연",
        "desc": "네오고딕 양식 신시청사 시계탑에서 펼쳐지는 정교한 기계식 인형극입니다. 16세기 빌헬름 5세의 혼례 마상 시합과 축하 댄스가 43개 종소리와 함께 울려 퍼집니다.",
        "tip": "★ 17:00 정각 시작! 16:55까지 광장 분수대 앞으로 돌아와 자리를 잡으세요.",
        "highlight": True
      },
      {
        "id": "d1-9",
        "day": 1,
        "num": 9,
        "period": "오후~저녁",
        "time": "17:30 - 18:20",
        "name": "막스마라 (Max Mara 부티크)",
        "nameDe": "Max Mara München (Maximilianstraße)",
        "lat": 48.1396,
        "lng": 11.5815,
        "category": "명품 쇼핑",
        "desc": "뮌헨 최고급 명품 거리인 막시밀리안 슈트라세(Maximilianstraße)에 위치한 막스마라 플래그십 부티크입니다. 고급스러운 코트와 최신 컬렉션을 여유롭게 쇼핑합니다.",
        "tip": "주변에 샤넬, 루이비통, 에르메스 등 세계적 명품 플래그십이 함께 모여 있습니다."
      },
      {
        "id": "d1-10",
        "day": 1,
        "num": 10,
        "period": "저녁",
        "time": "18:20 - 19:15",
        "name": "퓐프 회페 (Fünf Höfe)",
        "nameDe": "Fünf Höfe Shopping Mall",
        "lat": 48.1406,
        "lng": 11.5756,
        "category": "세련된 쇼핑 아케이드",
        "desc": "세계적인 건축가 헤르초크 & 드 뫼롱이 설계한 감각적인 5개 중정 쇼핑 아케이드입니다. 공중에 매달린 거대한 행잉 플랜트와 감각적인 디자이너 숍, 라이프스타일 부티크를 둘러봅니다.",
        "tip": "건축물 자체가 현대 미술 작품 같아 사진 촬영하기에도 매우 멋진 명소입니다."
      },
      {
        "id": "d1-11",
        "day": 1,
        "num": 11,
        "period": "저녁",
        "time": "19:15 - 20:45",
        "name": "구시가지 저녁 식사 & 내일 로드트립 간식 구비 (Rewe/슈퍼)",
        "nameDe": "Abendessen & Snack-Einkauf für Roadtrip",
        "lat": 48.1398,
        "lng": 11.5745,
        "category": "디너 & 마트 장보기",
        "desc": "퓐프 회페 주변 세련된 비스트로/레스토랑에서 편안하게 저녁 식사를 즐깁니다. 식사 후 인근 슈퍼마켓(Rewe City 등)에 들러 내일 새벽 렌트카에서 먹을 생수, 과일, 음료, 빵을 미리 챙깁니다!",
        "tip": "★ 내일 06:00 이른 아침 렌터카 픽업이므로 차 안에서 먹을 간식과 물을 오늘 밤 꼭 사두세요."
      }
    ]
  },
  {
    "day": 2,
    "dayLabel": "🚗 21일 (2일차) 렌트카",
    "title": "21일: 🚗 렌트카 알프스 로드트립 (노이슈바인슈타인 성 & 추크슈피체 산)",
    "summary": "새벽 06:00 SIXT 뮌헨 중앙역에서 렌터카 픽업 후 로맨틱 가도 질주! 마리엔 다리 오픈런, 노이슈바인슈타인 성 내부 관람, 에메랄드빛 호수 점심, 오스트리아 국경 드라이브, 독일 최고봉(2,962m) 정복",
    "color": "#f97316",
    "transitTip": "이동 수단: SIXT 렌터카 드라이브 (총 약 280km 힐링 루프 코스). A96 고속도로 및 오스트리아 비네트 불필요 국도 이용",
    "googleRouteUrl": "https://www.google.com/maps/dir/SIXT+Car+Rental+Munich+Central+Station/Marienbr%C3%BCcke/Neuschwanstein+Castle/Alpsee/Eibsee+Cable+Car/Novotel+M%C3%BCnchen+City+Arnulfpark",
    "spots": [
      {
        "id": "d2-1",
        "day": 2,
        "num": 1,
        "period": "새벽~아침",
        "time": "06:00 - 06:45",
        "name": "SIXT 렌터카 뮌헨 중앙역점 (06:00 차량 픽업)",
        "nameDe": "SIXT Car Rental Munich Central Station",
        "lat": 48.1402,
        "lng": 11.5583,
        "category": "렌터카 픽업 / 출발",
        "desc": "SIXT 뮌헨 중앙역점(Bahnhofplatz 1)에서 예약 차량을 06:00 정각에 픽업합니다! 노보텔 숙소에서 트램 17번으로 5분 거리라 이동이 매우 편리합니다.",
        "tip": "국제운전면허증, 국내면허증, 여권, 본인 명의 신용카드를 미리 챙기세요. 차량 외관 사진을 꼼꼼히 촬영해 둡니다.",
        "highlight": True
      },
      {
        "id": "d2-2",
        "day": 2,
        "num": 2,
        "period": "오전",
        "time": "08:45 - 10:15",
        "name": "마리엔 다리 (Marienbrücke - 1순위 방문)",
        "nameDe": "Marienbrücke Neuschwanstein",
        "lat": 47.5552,
        "lng": 10.7496,
        "category": "전망 명소 / 협곡 다리",
        "desc": "페Polling 협곡 위 90m 상공에 걸린 아찔한 철교입니다. 디즈니 성의 모티브가 된 노이슈바인슈타인 성의 압도적인 전경을 가장 완벽한 각도에서 담을 수 있는 최고의 포토존입니다.",
        "tip": "★ 1순위 방문! 성 투어 전 먼저 올라가 단체 관광객이 몰리기 전 환상적인 인생 사진을 남기세요.",
        "highlight": True
      },
      {
        "id": "d2-3",
        "day": 2,
        "num": 3,
        "period": "오전",
        "time": "10:30 - 12:15",
        "name": "노이슈바인슈타인 성 내부 투어",
        "nameDe": "Schloss Neuschwanstein",
        "lat": 47.5576,
        "lng": 10.7498,
        "category": "궁전 투어 (사전예약)",
        "desc": "바이에른 국왕 루드비히 2세가 바그너의 오페라에 영감을 받아 지은 중세 환상 속 백조의 성입니다. 왕의 침실, 음유시인의 방, 인공 동굴 등 화려한 내부를 가이드 투어로 관람합니다.",
        "tip": "사전 예약 티켓의 입장 시간에 늦으면 입장이 절대 불가하므로 최소 15분 전 성 안뜰에 도착해 대기하세요."
      },
      {
        "id": "d2-4",
        "day": 2,
        "num": 4,
        "period": "점심",
        "time": "12:30 - 13:45",
        "name": "호엔슈방가우 마을 & 알프제(Alpsee) 점심",
        "nameDe": "Alpsee & Hohenschwangau Dorf",
        "lat": 47.5539,
        "lng": 10.7380,
        "category": "알프스 호수 & 런치",
        "desc": "알프스 산맥이 병풍처럼 둘러싼 에메랄드빛 알프제 호숫가를 산책하고, 마을 전통 레스토랑 테라스에서 슈니첼과 바이에른 요리로 기분 좋은 점심 식사를 즐깁니다.",
        "tip": "호숫가 벤치에서 호수와 호엔슈방가우 성을 배경으로 사진 찍기 좋습니다."
      },
      {
        "id": "d2-5",
        "day": 2,
        "num": 5,
        "period": "오후",
        "time": "13:45 - 15:00",
        "name": "알프스 파노라마 국도 드라이브 (오스트리아 국경)",
        "nameDe": "Alpen-Panoramastraße via Reutte (Österreich)",
        "lat": 47.4565,
        "lng": 10.9922,
        "category": "파노라마 드라이브 코스",
        "desc": "슈방가우에서 오스트리아 로이테(Reutte)와 에어발트(Ehrwald) 국도를 경유하여 추크슈피체 아이브제 호수로 향하는 환상적인 알프스 드라이브 코스입니다 (약 60km).",
        "tip": "국도(Landstraße B179/B187)를 이용하므로 오스트리아 고속도로 통행권(비네트 Vignette) 구매가 필요 없습니다!"
      },
      {
        "id": "d2-6",
        "day": 2,
        "num": 6,
        "period": "오후",
        "time": "15:00 - 17:45",
        "name": "추크슈피체 산 (2,962m) & 아이브제",
        "nameDe": "Zugspitze (2.962m) Seilbahn & Eibsee",
        "lat": 47.4211,
        "lng": 10.9853,
        "category": "독일 최고봉 전망대",
        "desc": "해발 2,962m 독일의 지붕! 최첨단 아이브제 케이블카로 단 10분 만에 정상으로 수직 상승합니다. 독일·오스트리아·스위스·이탈리아 4개국 알프스 고봉 400여 개가 파노라마로 펼쳐집니다.",
        "tip": "정상 테라스에서 독일과 오스트리아 국경선 표시판을 걸어서 넘어가는 이색 체험을 놓치지 마세요.",
        "highlight": True
      },
      {
        "id": "d2-7",
        "day": 2,
        "num": 7,
        "period": "저녁",
        "time": "18:00 - 19:30",
        "name": "뮌헨 복귀 드라이브 & 차량 반납 / 호텔 휴식",
        "nameDe": "Rückfahrt nach München & SIXT Rückgabe",
        "lat": 48.1455,
        "lng": 11.5390,
        "category": "귀환 & 휴식",
        "desc": "가르미슈-파르텐키르헨을 지나 A95 아우토반을 시원하게 달려 뮌헨으로 복귀합니다. SIXT 렌터카를 반납하고 호텔에서 뿌듯한 마음으로 편안한 휴식을 취합니다.",
        "tip": "차량 반납 전 중앙역 근처 주유소에서 기름을 가득(Full) 채워 반납하세요."
      }
    ]
  },
  {
    "day": 3,
    "dayLabel": "22일 (3일차)",
    "title": "22일: 과학 기술과 예술 힐링, 여름 궁전 & 호프브로이 맥주 축제",
    "summary": "어제 장거리 운전 피로를 고려해 느긋하게 출발! 국립 독일 박물관 알짜 관람 후 뮌헨공대 학식 점심, 미술관 지구 감성 카페 타임, 알테 피나코테크 명화, 님펜부르크 여름 별궁 석양, 그리고 저녁엔 호프브로이하우스에서 신나는 맥주 파티!",
    "color": "#8b5cf6",
    "transitTip": "대중교통: M구역 1일권 (트램 16/17번 및 지하철 무제한). 님펜부르크 궁전은 호텔 앞 트램 17번 직통 연결",
    "googleRouteUrl": "https://www.google.com/maps/dir/Deutsches+Museum/TU+Mensa/Caf%C3%A9+Klenze/Alte+Pinakothek/Schloss+Nymphenburg/Hofbr%C3%A4uhaus+M%C3%BCnchen",
    "spots": [
      {
        "id": "d3-1",
        "day": 3,
        "num": 1,
        "period": "오전",
        "time": "10:30 - 12:30",
        "name": "국립 독일 박물관 (Deutsches Museum)",
        "nameDe": "Deutsches Museum",
        "lat": 48.1301,
        "lng": 11.5838,
        "category": "과학기술 박물관 (알짜 코스)",
        "desc": "이자르강 섬 위에 자리한 세계 최대 규모의 과학·기술 박물관입니다. 무리하지 않고 약 1.5~2시간 동안 항공기 실물, 해양 선박, 지하 광산 모형 등 핵심 명물 위주로 콤팩트하게 관람합니다.",
        "tip": "입구에서 하이라이트 추천 동선 지도를 받아 항공·우주관 및 해양관 위주로 관람하면 딱 2시간 안에 알차게 즐길 수 있습니다."
      },
      {
        "id": "d3-2",
        "day": 3,
        "num": 2,
        "period": "점심",
        "time": "13:00 - 14:00",
        "name": "TU MENSA (뮌헨공대 학생식당 점심)",
        "nameDe": "Mensa Arcisstraße (TUM)",
        "lat": 48.1480,
        "lng": 11.5678,
        "category": "대학교 학생식당 (가성비 런치)",
        "desc": "유럽 최고의 공대 중 하나인 뮌헨공대(TUM) 메인 캠퍼스 학생식당입니다. 뮌헨 시내 최고의 가성비로 든든한 점심 식사를 즐기며 활기찬 독일 대학생들의 분위기를 경험합니다.",
        "tip": "★ 점심 영업이 14:30 정시 마감되므로 13:30 전에는 꼭 입장하세요!"
      },
      {
        "id": "d3-3",
        "day": 3,
        "num": 3,
        "period": "오후",
        "time": "14:00 - 14:50",
        "name": "미술관 지구 감성 카페 타임 (Café Klenze / 테라스)",
        "nameDe": "Café Klenze in der Alten Pinakothek",
        "lat": 48.1485,
        "lng": 11.5700,
        "category": "감성 카페 / 디저트 쉼터",
        "desc": "알테 피나코테크 내 높은 천장과 고풍스러운 샹들리에가 아름다운 카페 클렌체(Café Klenze) 또는 미술관 야외 테라스에서 즐기는 달콤한 카페 타임입니다. 진한 커피와 전통 사과파이(아펠슈트루델)를 맛보며 다리를 쉽니다.",
        "tip": "미술관 앞 푸른 잔디밭을 바라보며 마시는 커피 한 잔이 주는 여유가 일품입니다."
      },
      {
        "id": "d3-4",
        "day": 3,
        "num": 4,
        "period": "오후",
        "time": "14:50 - 16:30",
        "name": "알테 피나코테크 (Alte Pinakothek)",
        "nameDe": "Alte Pinakothek",
        "lat": 48.1483,
        "lng": 11.5700,
        "category": "클래식 미술관",
        "desc": "14~18세기 유럽 회화의 보고입니다. 독일 미술의 거장 알브레히트 뒤러의 신비로운 '모피 코트를 입은 자화상', 레오나르도 다빈치의 '카네이션을 든 성모', 루벤스의 거대한 종교화 대작들을 감상합니다.",
        "tip": "한국어 오디오 가이드가 잘 갖춰져 있어 명화의 해설을 들으며 둘러보기에 아주 좋습니다."
      },
      {
        "id": "d3-5",
        "day": 3,
        "num": 5,
        "period": "오후~해질녘",
        "time": "17:00 - 18:45",
        "name": "님펜부르크 궁전 (Schloss Nymphenburg)",
        "nameDe": "Schloss Nymphenburg",
        "lat": 48.1583,
        "lng": 11.5033,
        "category": "여름 별궁 / 대운하 정원",
        "desc": "바이에른 왕가(비텔스바흐 가문)의 여름 별궁입니다. 베르사유 궁전을 모티브로 한 광활한 바로크 양식 대운하 정원과 백조들이 유영하는 호숫가를 석양 무렵 여유롭게 산책합니다.",
        "tip": "돌아올 때는 궁전 정문 앞 정류장에서 트램 17번을 타면 우리 숙소(노보텔) 바로 앞까지 한 번에 이동합니다."
      },
      {
        "id": "d3-6",
        "day": 3,
        "num": 6,
        "period": "저녁",
        "time": "19:30 - 21:30",
        "name": "호프브로이하우스 (저녁 맥주 & 학센 파티!)",
        "nameDe": "Hofbräuhaus am Platzl",
        "lat": 48.1376,
        "lng": 11.5800,
        "category": "바이에른 전설의 맥주홀",
        "desc": "1589년에 설립된 전 세계에서 가장 유명한 맥주홀입니다! 흥겨운 바이에른 전통 라이브 관악 연주가 울려 퍼지는 가운데, 1L짜리 커다란 마스 맥주와 겉바속촉 슈바인학센을 즐기며 신나게 건배합니다.",
        "tip": "입구 공식 기념품샵에서 호프브로이 시그니처 1L 유리 맥주잔이나 전통 도자기 머그(Steinkrug), 마그넷을 기념품으로 구매하기 딱 좋습니다!",
        "highlight": True
      }
    ]
  },
  {
    "day": 4,
    "dayLabel": "23일 (4일차)",
    "title": "23일: 축구 성지 투어 ➔ 힙한 슈바빙 런치 ➔ 낮의 영국정원 ➔ 레지덴츠 & 슈퍼 기념품 ➔ 켐핀스키 파인다이닝!",
    "summary": "알리안츠 아레나 홈구장 투어 후 예술가 거리 슈바빙에서 감각적인 런치! 푸르른 낮의 영국정원에서 서퍼들 구경, 도심 궁전 레지덴츠 관람, 슈퍼마켓/기념품 싹쓸이 쇼핑, 그리고 5성급 켐핀스키 슈바르츠라이터 파인다이닝 완결 축배",
    "color": "#10b981",
    "transitTip": "대중교통: U6 지하철(Fröttmaning 아레나 왕복 및 슈바빙 이동) 및 시내 도보",
    "googleRouteUrl": "https://www.google.com/maps/dir/Allianz+Arena/M%C3%BCnchner+Freiheit/Eisbachwelle/Residenz+M%C3%BCnchen/Dallmayr/Schwarzreiter+Tagesbar+%26+Restaurant",
    "spots": [
      {
        "id": "d4-1",
        "day": 4,
        "num": 1,
        "period": "오전",
        "time": "10:00 - 12:00",
        "name": "알리안츠 아레나 투어 (Allianz Arena)",
        "nameDe": "Allianz Arena Tour & FC Bayern Museum",
        "lat": 48.2188,
        "lng": 11.6247,
        "category": "축구 전용 경기장 투어",
        "desc": "김민재 선수가 활약하는 FC 바이에른 뮌헨의 홈구장입니다. 다이아몬드 에어쿠션 외관을 감상하고, 선수 락커룸, 믹스트존, 입장 터널, 피치사이드 벤치 투어 및 트로피 박물관을 관람합니다.",
        "tip": "투어 후 아레나 메가스토어에서 김민재 유니폼, 머플러 등 공식 굿즈를 구매할 수 있습니다."
      },
      {
        "id": "d4-2",
        "day": 4,
        "num": 2,
        "period": "점심",
        "time": "12:40 - 14:15",
        "name": "슈바빙(Schwabing) 지구 & 점심 (뮌히너 프라이하이트)",
        "nameDe": "Schwabing & Münchner Freiheit Mittagessen",
        "lat": 48.1614,
        "lng": 11.5866,
        "category": "예술가 거리 / 감각적인 런치",
        "desc": "투어 후 지하철 U6을 타고 곧바로 예술과 유행의 거리 슈바빙으로 이동! 뮌히너 프라이하이트 주변 테라스 비스트로나 브런치 카페에서 활기찬 도심 분위기를 만끽하며 맛있는 점심 식사를 즐깁니다.",
        "tip": "개성 넘치는 부티크 숍과 감각적인 카페들이 즐비해 식사 후 가볍게 둘러보기 좋습니다."
      },
      {
        "id": "d4-3",
        "day": 4,
        "num": 3,
        "period": "낮~오후",
        "time": "14:30 - 16:00",
        "name": "낮의 영국정원 & 아이스바흐 파도타기 (Eisbachwelle)",
        "nameDe": "Englischer Garten & Eisbachwelle",
        "lat": 48.1432,
        "lng": 11.5877,
        "category": "도심 속 자연 & 이색 서핑",
        "desc": "화창한 대낮의 영국정원은 유럽에서 가장 활기찬 도시 공원입니다. 차가운 아이스바흐 급류에서 능숙하게 회전 기술을 펼치는 도심 서퍼들의 다이내믹한 서핑을 눈앞에서 구경하며 공원을 산책합니다.",
        "tip": "다리 위에 서서 시원한 물살을 가르는 서퍼들을 가장 가까이에서 역동적으로 촬영할 수 있습니다."
      },
      {
        "id": "d4-4",
        "day": 4,
        "num": 4,
        "period": "오후",
        "time": "16:15 - 17:45",
        "name": "오데온 광장 & 뮌헨 레지덴츠 (Residenz München)",
        "nameDe": "Odeonsplatz & Residenz München",
        "lat": 48.1412,
        "lng": 11.5786,
        "category": "도심 궁전 복합체",
        "desc": "이탈리아풍 오데온 광장을 지나 600년간 바이에른 군주들의 거처였던 독일 최대의 도심 궁전 레지덴츠로 들어섭니다. 66m 길이의 아치형 천장 갤러리 '안티콰리움(Antiquarium)'의 르네상스 프레스코화가 압권입니다.",
        "tip": "안티콰리움 홀은 광각 렌즈나 파노라마로 찍으면 영화 속 한 장면 같은 웅장한 사진이 완성됩니다."
      },
      {
        "id": "d4-5",
        "day": 4,
        "num": 5,
        "period": "늦은 오후",
        "time": "17:45 - 18:45",
        "name": "구시가지 슈퍼마켓(마트) & 기념품 싹쓸이 쇼핑 타임",
        "nameDe": "Souvenirs & Supermarkt Shopping (dm / Edeka / Dallmayr)",
        "lat": 48.1380,
        "lng": 11.5770,
        "category": "기념품 & 슈퍼마켓 쇼핑",
        "desc": "레지덴츠에서 저녁 식사 장소(막시밀리안 거리)로 이어지는 동선 주변의 대형 슈퍼마켓(Edeka, Rewe)과 dm 드럭스토어에서 귀국 전 독일 과자, 초콜릿, 발포비타민, 핸드크림, 로컬 맥주 등 기념품을 여유롭게 챙깁니다!",
        "tip": "숙소와 도보/트램으로 바로 연결되므로 선물용 캐리어 짐을 오늘 든든히 구비해 두세요."
      },
      {
        "id": "d4-6",
        "day": 4,
        "num": 6,
        "period": "저녁",
        "time": "19:00 - 21:00",
        "name": "Schwarzreiter Tagesbar & Restaurant (켐핀스키 파인다이닝)",
        "nameDe": "Schwarzreiter Restaurant & Tagesbar (Hotel Vier Jahreszeiten Kempinski)",
        "lat": 48.1394,
        "lng": 11.5818,
        "category": "모던 바이에른 파인다이닝 (미쉐린 수록)",
        "desc": "5성급 켐핀스키 호텔 내에 위치한 최고급 모던 바이에른 퀴진 레스토랑입니다. 루드비히 2세 국왕이 가장 사랑했던 '슈바르츠라이터(송어류)' 요리와 품격 있는 와인 페어링으로 4일간의 바이에른 여행을 완벽하게 마무리합니다.",
        "tip": "사전 예약 권장. 스마트 캐주얼 복장으로 우아하고 특별한 마지막 밤을 기념하세요.",
        "highlight": True
      }
    ]
  }
]

# 기존 roadtrip coords
roadtrip_coords = [
  [48.1402, 11.5583], # SIXT 뮌헨 중앙역
  [48.1300, 11.4500],
  [48.0600, 11.0000],
  [48.0500, 10.8700],
  [47.8000, 10.8700],
  [47.5750, 10.7400],
  [47.5552, 10.7496], # 마리엔 다리
  [47.5576, 10.7498], # 노이슈바인슈타인 성
  [47.5539, 10.7380], # 알프제
  [47.5300, 10.7100],
  [47.4890, 10.7180],
  [47.4000, 10.9160],
  [47.4565, 10.9922], # 오스트리아 파노라마 국도
  [47.4211, 10.9853], # 추크슈피체 아이브제
  [47.4565, 10.9922],
  [47.4920, 11.0950],
  [47.7100, 11.2000],
  [47.9900, 11.3400],
  [48.1455, 11.5390]  # 노보텔 복귀
]

# Leaflet CSS 읽기
css_path = '/Users/min/orca/workspaces/trip/여행/leaflet_inline.css'
if not os.path.exists(css_path):
    os.system(f'curl -s https://unpkg.com/leaflet@1.9.4/dist/leaflet.css > {css_path}')

with open(css_path, encoding='utf-8') as f:
    leaflet_css = f.read()

# HTML 템플릿 생성
# index.html에서 CSS/HTML 골격 읽어오기
base_html = open('/Users/min/orca/workspaces/trip/여행/index.html', encoding='utf-8').read()

# HTML에서 <script> 이전 부분과 이후 부분 분리
script_split = base_html.split('<script>')
html_head = script_split[0]

# 새로운 JS 스크립트 작성
new_js = f"""
const HOTEL_DATA = {json.dumps(hotel_data, ensure_ascii=False, indent=2)};

const ITINERARY_DATA = {json.dumps(itinerary_data, ensure_ascii=False, indent=2)};

const ROADTRIP_ROUTE_COORDS = {json.dumps(roadtrip_coords, ensure_ascii=False, indent=2)};

let currentDayFilter = 'all';
let currentMobileView = 'list';
let map = null;
let markersLayerGroup = null;
let polylinesLayerGroup = null;
let hotelMarker = null;
let tileLayer = null;
let currentTileMode = 'voyager';
const spotMarkerMap = new Map();
let currentActiveSpotId = null;

const TILE_PROVIDERS = {{
  voyager: {{
    url: 'https://basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}{{r}}.png',
    options: {{
      attribution: '&copy; CARTO & OpenStreetMap',
      subdomains: 'abcd',
      maxZoom: 19
    }}
  }},
  esri_street: {{
    url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{{z}}/{{x}}',
    options: {{
      attribution: '&copy; Esri World Street Map',
      maxZoom: 19
    }}
  }},
  esri_satellite: {{
    url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{x}}',
    options: {{
      attribution: '&copy; Esri World Imagery',
      maxZoom: 18
    }}
  }}
}};

function initMap() {{
  try {{
    map = L.map('map', {{
      center: [48.1455, 11.5390],
      zoom: 12,
      zoomControl: false
    }});

    L.control.zoom({{ position: 'topright' }}).addTo(map);
    tileLayer = L.tileLayer(TILE_PROVIDERS.voyager.url, TILE_PROVIDERS.voyager.options).addTo(map);

    polylinesLayerGroup = L.layerGroup().addTo(map);
    markersLayerGroup = L.layerGroup().addTo(map);

    createHotelMarker();
    renderView();

    setTimeout(fixMapSize, 100);
    setTimeout(fixMapSize, 300);
    setTimeout(fixMapSize, 800);
    window.addEventListener('resize', fixMapSize);
  }} catch (err) {{
    console.error('Map init error:', err);
  }}
}}

function fixMapSize() {{
  if (map) {{
    map.invalidateSize();
  }}
}}

function createHotelMarker() {{
  const hotelIcon = L.divIcon({{
    className: 'custom-div-icon',
    html: `
      <div class="marker-pin hotel-pin" title="${{HOTEL_DATA.name}}">
        <svg class="marker-svg" viewBox="0 0 36 44" width="36" height="44">
          <path d="M18 0 C8 0 0 8 0 18 C0 31.5 18 44 18 44 C18 44 36 31.5 36 18 C36 8 28 0 18 0 Z" fill="#b45309" stroke="#ffffff" stroke-width="2"/>
          <circle cx="18" cy="18" r="14" fill="#d97706"/>
          <text x="18" y="23" font-size="14" text-anchor="middle" fill="#ffffff">🏨</text>
        </svg>
      </div>
    `,
    iconSize: [36, 44],
    iconAnchor: [18, 44],
    popupAnchor: [0, -40]
  }});

  const popupHtml = `
    <div>
      <div class="popup-badge" style="background:#b45309;">우리 숙소 (Basecamp)</div>
      <div class="popup-title">${{HOTEL_DATA.name}}</div>
      <div class="popup-time" style="color:#78350f;">${{HOTEL_DATA.nameDe}}</div>
      <div class="popup-desc">${{HOTEL_DATA.desc}}</div>
      <div style="background:#fef3c7; border:1px solid #fde68a; border-radius:6px; padding:6px; font-size:11px; margin-bottom:8px; color:#92400e;">
        <strong>💡 교통 팁:</strong> ${{HOTEL_DATA.tip}}
      </div>
      <a class="popup-link" href="${{HOTEL_DATA.googleMapsUrl}}" target="_blank" rel="noopener">Google 지도에서 열기 &rarr;</a>
    </div>
  `;

  hotelMarker = L.marker([HOTEL_DATA.lat, HOTEL_DATA.lng], {{
    icon: hotelIcon,
    zIndexOffset: 1000
  }}).bindPopup(popupHtml);

  hotelMarker.addTo(map);
}}

function createCustomPin(num, color, isHighlight) {{
  const width = isHighlight ? 36 : 30;
  const height = isHighlight ? 44 : 38;
  const strokeColor = isHighlight ? '#fbbf24' : '#ffffff';
  const strokeWidth = isHighlight ? 2.5 : 1.5;

  return L.divIcon({{
    className: 'custom-div-icon',
    html: `
      <div class="marker-pin ${{isHighlight ? 'hotel-pin' : ''}}">
        <svg class="marker-svg" viewBox="0 0 36 44" width="${{width}}" height="${{height}}">
          <path d="M18 0 C8 0 0 8 0 18 C0 31.5 18 44 18 44 C18 44 36 31.5 36 18 C36 8 28 0 18 0 Z" fill="${{color}}" stroke="${{strokeColor}}" stroke-width="${{strokeWidth}}"/>
          <circle cx="18" cy="18" r="11" fill="#ffffff"/>
          <text x="18" y="22.5" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="900" text-anchor="middle" fill="${{color}}">${{num}}</text>
        </svg>
      </div>
    `,
    iconSize: [width, height],
    iconAnchor: [width / 2, height],
    popupAnchor: [0, -height + 4]
  }});
}}

function renderView() {{
  renderSidebar();
  renderMapLayers();
  renderBottomCarousel();
  updateLegend();
}}

function renderSidebar() {{
  const container = document.getElementById('itineraryList');
  if (!container) return;

  const daysToShow = currentDayFilter === 'all'
    ? ITINERARY_DATA
    : ITINERARY_DATA.filter(d => d.day === parseInt(currentDayFilter));

  let html = '';

  daysToShow.forEach(dayInfo => {{
    html += `
      <section class="day-section" id="day-sec-${{dayInfo.day}}">
        <div class="day-header" style="border-left-color: ${{dayInfo.color}};">
          <div class="day-header-meta">
            <span class="day-tag" style="background: ${{dayInfo.color}};">${{dayInfo.dayLabel}}</span>
            <span class="day-route-count">장소 ${{dayInfo.spots.length}}곳</span>
          </div>
          <h2 class="day-title">${{dayInfo.title}}</h2>
          <p class="day-summary">${{dayInfo.summary}}</p>
          <div class="day-transit-tip">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>
            ${{dayInfo.transitTip}}
          </div>
          <div style="margin-top: 8px;">
            <a href="${{dayInfo.googleRouteUrl}}" target="_blank" rel="noopener" class="google-nav-btn">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
              ${{dayInfo.dayLabel}} 전체 구글 경로 길찾기
            </a>
          </div>
        </div>
        <div class="spots-list">
    `;

    dayInfo.spots.forEach(spot => {{
      const gUrl = `https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent(spot.name + ' ' + (spot.nameDe || 'Munich'))}}`;
      html += `
        <div class="spot-card ${{spot.highlight ? 'highlight-spot' : ''}}" id="card-${{spot.id}}" onclick="onSpotCardClick('${{spot.id}}')">
          <div class="spot-card-header">
            <div class="spot-num-badge" style="background: ${{dayInfo.color}};">${{spot.num}}</div>
            <div class="spot-title-wrap">
              <div class="spot-time-category">
                <span class="spot-period-tag">${{spot.period}}</span>
                <span class="spot-time">${{spot.time}}</span>
                <span class="spot-category-tag">${{spot.category}}</span>
              </div>
              <h3 class="spot-name">${{spot.name}}</h3>
              ${{spot.nameDe ? `<div class="spot-name-de">${{spot.nameDe}}</div>` : ''}}
            </div>
          </div>
          <p class="spot-desc">${{spot.desc}}</p>
          <div class="spot-tip">
            <strong>TIP:</strong> ${{spot.tip}}
          </div>
          <div class="spot-links">
            <a class="spot-map-link" href="${{gUrl}}" target="_blank" rel="noopener" onclick="event.stopPropagation();">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
              Google 지도 열기
            </a>
          </div>
        </div>
      `;
    }});

    html += `
        </div>
      </section>
    `;
  }});

  container.innerHTML = html;
}}

function renderMapLayers() {{
  if (!map || !markersLayerGroup || !polylinesLayerGroup) return;

  markersLayerGroup.clearLayers();
  polylinesLayerGroup.clearLayers();
  spotMarkerMap.clear();

  const daysToShow = currentDayFilter === 'all'
    ? ITINERARY_DATA
    : ITINERARY_DATA.filter(d => d.day === parseInt(currentDayFilter));

  const allLatLngs = [];

  if (hotelMarker) {{
    allLatLngs.push([HOTEL_DATA.lat, HOTEL_DATA.lng]);
  }}

  daysToShow.forEach(dayInfo => {{
    const dayCoords = [];

    dayInfo.spots.forEach(spot => {{
      const latLng = [spot.lat, spot.lng];
      dayCoords.push(latLng);
      allLatLngs.push(latLng);

      const icon = createCustomPin(spot.num, dayInfo.color, spot.highlight);
      const marker = L.marker(latLng, {{
        icon: icon,
        zIndexOffset: spot.highlight ? 500 : 100
      }});

      const gUrl = `https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent(spot.name + ' ' + (spot.nameDe || 'Munich'))}}`;
      const popupHtml = `
        <div>
          <div class="popup-badge" style="background:${{dayInfo.color}};">${{dayInfo.dayLabel}} · 코스 #${{spot.num}}</div>
          <div class="popup-title">${{spot.name}}</div>
          <div class="popup-time">${{spot.period}} ${{spot.time}} (${{spot.category}})</div>
          <div class="popup-desc">${{spot.desc}}</div>
          <div style="background:#f8fafc; border-left:3px solid ${{dayInfo.color}}; padding:6px 8px; font-size:11px; margin-bottom:8px; border-radius:0 4px 4px 0;">
            <strong>TIP:</strong> ${{spot.tip}}
          </div>
          <a class="popup-link" href="${{gUrl}}" target="_blank" rel="noopener">Google 지도에서 보기 &rarr;</a>
        </div>
      `;

      marker.bindPopup(popupHtml);
      marker.on('click', () => {{
        highlightActiveSpot(spot.id, false);
      }});

      marker.addTo(markersLayerGroup);
      spotMarkerMap.set(spot.id, {{ marker, spot, dayInfo }});
    }});

    // 경로선 그리기
    if (dayInfo.day === 2) {{
      const roadPolyline = L.polyline(ROADTRIP_ROUTE_COORDS, {{
        color: dayInfo.color,
        weight: 4.5,
        opacity: 0.85,
        dashArray: '8, 6',
        lineCap: 'round',
        lineJoin: 'round'
      }}).addTo(polylinesLayerGroup);
    }} else if (dayCoords.length > 1) {{
      const line = L.polyline(dayCoords, {{
        color: dayInfo.color,
        weight: 3.5,
        opacity: 0.75,
        dashArray: '5, 5',
        lineCap: 'round',
        lineJoin: 'round'
      }}).addTo(polylinesLayerGroup);
    }}
  }});

  if (allLatLngs.length > 0) {{
    try {{
      const bounds = L.latLngBounds(allLatLngs);
      map.fitBounds(bounds, {{
        padding: [30, 30],
        maxZoom: 14
      }});
    }} catch (e) {{
      console.error(e);
    }}
  }}
}}

function renderBottomCarousel() {{
  const carouselTrack = document.getElementById('carouselTrack');
  const dayTitleElem = document.getElementById('carouselDayTitle');
  if (!carouselTrack) return;

  const daysToShow = currentDayFilter === 'all'
    ? ITINERARY_DATA
    : ITINERARY_DATA.filter(d => d.day === parseInt(currentDayFilter));

  if (dayTitleElem) {{
    if (currentDayFilter === 'all') {{
      dayTitleElem.textContent = '전체 4일 일정 스팟 둘러보기';
    }} else {{
      const cur = ITINERARY_DATA.find(d => d.day === parseInt(currentDayFilter));
      dayTitleElem.textContent = `${{cur.dayLabel}} 스팟 (${{cur.spots.length}}곳)`;
    }}
  }}

  let cardsHtml = '';

  // 첫 번째 카드는 우리 숙소
  cardsHtml += `
    <div class="carousel-card" id="carousel-hotel" onclick="focusHotel(true)">
      <div class="carousel-card-top">
        <span class="carousel-badge" style="background:#b45309;">🏨 베이스캠프</span>
        <a class="carousel-google-link" href="${{HOTEL_DATA.googleMapsUrl}}" target="_blank" rel="noopener" onclick="event.stopPropagation();">길찾기 &rarr;</a>
      </div>
      <div class="carousel-card-title">${{HOTEL_DATA.name}}</div>
      <div class="carousel-card-sub">중앙역 트램 5분 · 님펜부르크 직통</div>
      <div class="carousel-card-desc">${{HOTEL_DATA.desc}}</div>
    </div>
  `;

  daysToShow.forEach(dayInfo => {{
    dayInfo.spots.forEach(spot => {{
      const gUrl = `https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent(spot.name + ' ' + (spot.nameDe || 'Munich'))}}`;
      cardsHtml += `
        <div class="carousel-card" id="carousel-${{spot.id}}" onclick="onSpotCardClick('${{spot.id}}', true)">
          <div class="carousel-card-top">
            <span class="carousel-badge" style="background:${{dayInfo.color}};">${{dayInfo.dayLabel}} #${{spot.num}}</span>
            <a class="carousel-google-link" href="${{gUrl}}" target="_blank" rel="noopener" onclick="event.stopPropagation();">Google 지도 &rarr;</a>
          </div>
          <div class="carousel-card-title">${{spot.name}}</div>
          <div class="carousel-card-sub">${{spot.period}} ${{spot.time}} · ${{spot.category}}</div>
          <div class="carousel-card-desc">${{spot.desc}}</div>
        </div>
      `;
    }});
  }});

  carouselTrack.innerHTML = cardsHtml;
}}

function scrollCarousel(dir) {{
  const track = document.getElementById('carouselTrack');
  if (track) {{
    track.scrollBy({{ left: dir * 260, behavior: 'smooth' }});
  }}
}}

function toggleCarousel() {{
  const container = document.getElementById('bottomCarousel');
  const btn = document.getElementById('carouselToggleBtn');
  if (!container) return;
  const isCollapsed = container.classList.toggle('collapsed');
  if (btn) {{
    btn.innerHTML = isCollapsed
      ? `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"/></svg> 스팟 목록 보기`
      : `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg> 접기`;
  }}
}}

function toggleLegend() {{
  const legend = document.getElementById('mapLegend');
  const btn = document.getElementById('legendToggleBtn');
  if (!legend) return;
  const isCollapsed = legend.classList.toggle('collapsed');
  if (btn) {{
    btn.textContent = isCollapsed ? '펼치기 ▼' : '접기 ▲';
  }}
}}

function updateLegend() {{
  const body = document.getElementById('legendBody');
  if (!body) return;

  let html = `
    <div class="legend-item" style="cursor:pointer;" onclick="focusHotel(true)">
      <span class="legend-color" style="background:#b45309;"></span>
      <span><strong>🏨 우리 숙소 (노보텔)</strong></span>
    </div>
  `;

  ITINERARY_DATA.forEach(d => {{
    const activeStyle = (currentDayFilter === 'all' || currentDayFilter == d.day) ? 'font-weight:700; color:#0f172a;' : 'opacity:0.6;';
    html += `
      <div class="legend-item" style="cursor:pointer; ${{activeStyle}}" onclick="setDayFilter('${{d.day}}')">
        <span class="legend-color" style="background:${{d.color}};"></span>
        <span>${{d.dayLabel}} (${{d.spots.length}}곳)</span>
      </div>
    `;
  }});

  body.innerHTML = html;
}}

function setDayFilter(day) {{
  currentDayFilter = day;

  document.querySelectorAll('.day-tab').forEach(tab => {{
    if (tab.dataset.day === String(day)) {{
      tab.classList.add('active');
    }} else {{
      tab.classList.remove('active');
    }}
  }});

  renderView();

  if (window.innerWidth <= 768 && currentMobileView === 'list') {{
    setMobileView('map');
  }}
}}

function setMobileView(mode) {{
  currentMobileView = mode;

  const btnList = document.getElementById('btnViewList');
  const btnMap = document.getElementById('btnViewMap');
  const sidebar = document.getElementById('sidebar');
  const mapContainer = document.getElementById('mapContainer');

  if (mode === 'list') {{
    if (btnList) btnList.classList.add('active');
    if (btnMap) btnMap.classList.remove('active');
    if (sidebar) sidebar.classList.remove('hidden-on-mobile');
    if (mapContainer) mapContainer.classList.remove('active-on-mobile');
  }} else {{
    if (btnList) btnList.classList.remove('active');
    if (btnMap) btnMap.classList.add('active');
    if (sidebar) sidebar.classList.add('hidden-on-mobile');
    if (mapContainer) mapContainer.classList.add('active-on-mobile');
    setTimeout(fixMapSize, 150);
  }}
}}

function onSpotCardClick(spotId, isFromCarousel = false) {{
  highlightActiveSpot(spotId, true);

  if (window.innerWidth <= 768 && !isFromCarousel) {{
    setMobileView('map');
  }}
}}

function highlightActiveSpot(spotId, panTo = true) {{
  currentActiveSpotId = spotId;

  document.querySelectorAll('.spot-card').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('.carousel-card').forEach(c => c.classList.remove('active'));

  const card = document.getElementById(`card-${{spotId}}`);
  if (card) {{
    card.classList.add('active');
    if (window.innerWidth > 768) {{
      card.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
    }}
  }}

  const cCard = document.getElementById(`carousel-${{spotId}}`);
  if (cCard) {{
    cCard.classList.add('active');
    cCard.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
  }}

  const target = spotMarkerMap.get(spotId);
  if (target && map) {{
    if (panTo) {{
      map.flyTo([target.spot.lat, target.spot.lng], 15, {{
        duration: 0.8
      }});
    }}
    target.marker.openPopup();
  }}
}}

function focusHotel(openPopup = true) {{
  if (!map || !hotelMarker) return;

  document.querySelectorAll('.spot-card').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('.carousel-card').forEach(c => c.classList.remove('active'));

  const cCard = document.getElementById('carousel-hotel');
  if (cCard) {{
    cCard.classList.add('active');
    cCard.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
  }}

  map.flyTo([HOTEL_DATA.lat, HOTEL_DATA.lng], 15, {{
    duration: 0.8
  }});

  if (openPopup) {{
    hotelMarker.openPopup();
  }}

  if (window.innerWidth <= 768 && currentMobileView === 'list') {{
    setMobileView('map');
  }}
}}

function toggleMapLayer() {{
  if (!map || !tileLayer) return;

  if (currentTileMode === 'voyager') {{
    currentTileMode = 'esri_street';
  }} else if (currentTileMode === 'esri_street') {{
    currentTileMode = 'esri_satellite';
  }} else {{
    currentTileMode = 'voyager';
  }}

  map.removeLayer(tileLayer);
  const prov = TILE_PROVIDERS[currentTileMode];
  tileLayer = L.tileLayer(prov.url, prov.options).addTo(map);

  const btn = document.getElementById('tileToggleBtn');
  if (btn) {{
    btn.innerHTML = currentTileMode === 'voyager'
      ? `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg> 지도: 상세도`
      : (currentTileMode === 'esri_street'
          ? `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg> 지도: 표준`
          : `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg> 지도: 위성`);
  }}
}}

document.addEventListener('DOMContentLoaded', () => {{
  initMap();

  if (window.innerWidth <= 768) {{
    const legend = document.getElementById('mapLegend');
    if (legend) {{
      legend.classList.add('collapsed');
      const btn = document.getElementById('legendToggleBtn');
      if (btn) btn.textContent = '펼치기 ▼';
    }}
  }}
}});
"""

final_html = f"{html_head}<script>{new_js}</script>\n</body>\n</html>"

# 파일 3개 작성
target_files = [
    '/Users/min/orca/workspaces/trip/여행/index.html',
    '/Users/min/orca/workspaces/trip/여행/munich_itinerary.html',
    '/Users/min/orca/workspaces/trip/여행/뮌헨_여행_일정_지도.html'
]

for tf in target_files:
    with open(tf, 'w', encoding='utf-8') as f:
        f.write(final_html)

print("HTML files regenerated successfully with updated schedule!")
