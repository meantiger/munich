import json
import os

# 1. 호텔 데이터
hotel_data = {
    "name": "노보텔 뮌헨 시티 아르눌프파크 (우리 숙소)",
    "nameDe": "Novotel München City Arnulfpark",
    "lat": 48.1454917,
    "lng": 11.5389985,
    "address": "Arnulfstraße 57, 80636 München",
    "googleMapsUrl": "https://maps.app.goo.gl/LNwTawdtw64NZc248",
    "desc": "이번 뮌헨 여행의 베이스캠프! Donnersbergerbrücke S-Bahn역 및 트램(16, 17번) 정류장 도보 2분. 중앙역 SIXT 렌터카, 시내 중심, 님펜부르크 궁전 이동 최적.",
    "tip": "호텔 바로 앞 트램 17번을 타면 중앙역(SIXT) 및 님펜부르크 궁전까지 환승 없이 5~15분 직통 이동!"
}

# 2. 사용자 확정 최적화 일정 데이터
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
    "title": "22일: 과학 기술과 황금 궁전(레지덴츠), 여름 별궁 & 호프브로이 맥주 파티!",
    "summary": "어제 장거리 운전 피로를 감안해 느긋하게 출발! 국립 독일 박물관 알짜 관람 후 뮌헨공대 학식 점심, 오데온 광장 테라스 카페, 독일 최대 도심 궁전 뮌헨 레지덴츠(안티콰리움), 님펜부르크 궁전 대운하 석양, 그리고 저녁엔 호프브로이하우스에서 신나는 맥주 파티!",
    "color": "#8b5cf6",
    "transitTip": "대중교통: M구역 1일권 (트램 16/17번 및 지하철 무제한). 님펜부르크 궁전은 호텔 앞 트램 17번 직통 연결",
    "googleRouteUrl": "https://www.google.com/maps/dir/Deutsches+Museum/TU+Mensa/Odeonsplatz/Residenz+M%C3%BCnchen/Schloss+Nymphenburg/Hofbr%C3%A4uhaus+M%C3%BCnchen",
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
        "time": "14:15 - 15:00",
        "name": "오데온 광장 테라스 카페 타임",
        "nameDe": "Odeonsplatz Café & Hofgarten",
        "lat": 48.1420,
        "lng": 11.5775,
        "category": "감성 카페 / 테라스 휴식",
        "desc": "이탈리아 피렌체 분위기가 물씬 풍기는 오데온 광장과 홉가르텐(왕실 정원) 주변 테라스 카페에서 즐기는 여유로운 카페 타임! 진한 커피와 디저트를 즐기며 다리를 쉽니다.",
        "tip": "테아티너 성당의 노란 파사드를 바라보며 야외 테라스에 앉아 여유를 만끽하기 좋습니다."
      },
      {
        "id": "d3-4",
        "day": 3,
        "num": 4,
        "period": "오후",
        "time": "15:00 - 16:30",
        "name": "뮌헨 레지덴츠 궁전 (Residenz München)",
        "nameDe": "Residenz München & Antiquarium",
        "lat": 48.1412,
        "lng": 11.5786,
        "category": "도심 황금 궁전 복합체",
        "desc": "지루한 미술관 대신 선택한 최고의 랜드마크! 600년간 바이에른 군주들의 거처였던 독일 최대 규모 도심 궁전입니다. 66m 길이의 아치형 천장 갤러리 '안티콰리움(Antiquarium)'의 화려한 르네상스 프레스코화가 압도적입니다.",
        "tip": "안티콰리움 홀은 광각 렌즈나 파노라마로 촬영하면 영화 속 한 장면 같은 웅장한 인생 사진이 완성됩니다.",
        "highlight": True
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
    "title": "23일: ⚽ 11:45 아레나 투어 & 뮤지엄 ➔ 슈바빙 카페 ➔ 낮의 영국정원 ➔ 여유로운 슈퍼/기념품 쇼핑 ➔ 켐핀스키 디너!",
    "summary": "10:30 알리안츠 아레나 도착 후 비스트로 브런치, 11:45 스타디움 가이드 투어(1시간) & FCB 뮤지엄(1시간), 슈바빙 테라스 카페, 화창한 낮의 영국정원 서핑 직관, 구시가지 대형 마트/dm 기념품 싹쓸이 쇼핑, 그리고 5성급 켐핀스키 슈바르츠라이터 파인다이닝 완결 축배",
    "color": "#10b981",
    "transitTip": "대중교통: U6 지하철(Fröttmaning 아레나 왕복 및 슈바빙 이동) 및 시내 도보",
    "googleRouteUrl": "https://www.google.com/maps/dir/Allianz+Arena/M%C3%BCnchner+Freiheit/Eisbachwelle/Dallmayr/Schwarzreiter+Tagesbar+%26+Restaurant",
    "spots": [
      {
        "id": "d4-1",
        "day": 4,
        "num": 1,
        "period": "오전",
        "time": "10:30 - 11:35",
        "name": "알리안츠 아레나 도착 & 비스트로 런치 (Arena Bistro)",
        "nameDe": "Allianz Arena Ankunft & Arena Bistro",
        "lat": 48.2188,
        "lng": 11.6247,
        "category": "경기장 도착 & 간단한 브런치",
        "desc": "11:45 스타디움 투어 시작 전 여유 있게 도착! 경기장 내 Arena Bistro 또는 Paulaner Fan Treff에서 바이에른 화이트 소시지(바이스부어스트), 갓 구운 브레첼, 슈니첼 샌드위치나 맥주/커피로 든든하게 요기합니다.",
        "tip": "입장 보안 검색과 투어 체크인을 위해 11:35까지는 투어 가이드 미팅 포인트(대기 구역)로 이동하세요."
      },
      {
        "id": "d4-2",
        "day": 4,
        "num": 2,
        "period": "오전~낮",
        "time": "11:45 - 12:45",
        "name": "알리안츠 아레나 스타디움 투어 (★ 11:45 정각 시작)",
        "nameDe": "Allianz Arena Tour (Start 11:45)",
        "lat": 48.2185,
        "lng": 11.6242,
        "category": "경기장 가이드 투어 (1시간)",
        "desc": "★ 11:45 정각 가이드 투어 출발 (약 1시간 소요)! 김민재 선수가 머무는 홈팀 라커룸, 믹스트존 인터뷰 구역, 웅장한 선수 입장 터널을 걸어 나가 피치사이드 잔디 벤치까지 생생하게 체험합니다.",
        "tip": "선수 입장 터널을 통과할 때 챔피언스리그 테마곡이 울려 퍼지는 순간은 평생 잊지 못할 하이라이트입니다!",
        "highlight": True
      },
      {
        "id": "d4-3",
        "day": 4,
        "num": 3,
        "period": "낮",
        "time": "12:45 - 13:50",
        "name": "FC 바이에른 뮤지엄 & 공식 메가스토어",
        "nameDe": "FC Bayern Museum & Megastore",
        "lat": 48.2191,
        "lng": 11.6252,
        "category": "클럽 박물관 & 공식 굿즈 (1시간)",
        "desc": "투어 종료 후 독일 최대 규모의 축구 클럽 박물관 관람(약 1시간 소요)! 수많은 분데스리가 마이스터샬레와 챔피언스리그 빅이어 트로피, 전설들의 유니폼을 감상하고 메가스토어에서 김민재 유니폼/머플러를 구매합니다.",
        "tip": "트로피 진열장 앞 포토존에서 빅이어를 배경으로 기념사진을 꼭 남기세요."
      },
      {
        "id": "d4-4",
        "day": 4,
        "num": 4,
        "period": "오후",
        "time": "14:20 - 15:40",
        "name": "슈바빙(Schwabing) 지구 산책 & 테라스 카페 타임",
        "nameDe": "Schwabing & Münchner Freiheit Café",
        "lat": 48.1614,
        "lng": 11.5866,
        "category": "예술가 거리 / 감성 카페",
        "desc": "U-Bahn U6을 타고 곧바로 예술과 유행의 거리 슈바빙으로 이동! 뮌히너 프라이하이트 주변의 감각적인 테라스 카페에서 향긋한 커피와 디저트를 즐기며 여유롭게 개성 넘치는 부티크 거리 풍경을 즐깁니다.",
        "tip": "경기장에서 이미 점심을 먹었으므로, 이곳에서는 가벼운 커피와 디저트로 여유를 즐기기 좋습니다."
      },
      {
        "id": "d4-5",
        "day": 4,
        "num": 5,
        "period": "오후",
        "time": "16:00 - 17:15",
        "name": "낮의 영국정원 & 아이스바흐 파도타기 (Eisbachwelle)",
        "nameDe": "Englischer Garten & Eisbachwelle",
        "lat": 48.1432,
        "lng": 11.5877,
        "category": "도심 속 자연 & 이색 서핑",
        "desc": "화창한 대낮의 영국정원은 유럽에서 가장 활기찬 도시 공원입니다. 차가운 아이스바흐 급류에서 능숙하게 회전 기술을 펼치는 도심 서퍼들의 다이내믹한 서핑을 눈앞에서 구경하며 공원을 산책합니다.",
        "tip": "다리 위에 서서 시원한 물살을 가르는 서퍼들을 가장 가까이에서 역동적으로 촬영할 수 있습니다."
      },
      {
        "id": "d4-6",
        "day": 4,
        "num": 6,
        "period": "늦은 오후",
        "time": "17:30 - 18:50",
        "name": "구시가지 슈퍼마켓(마트) & 귀국 기념품 싹쓸이 쇼핑 (1시간 20분)",
        "nameDe": "Souvenirs & Supermarkt Shopping (dm / Edeka / Dallmayr)",
        "lat": 48.1380,
        "lng": 11.5770,
        "category": "여유로운 기념품 & 슈퍼마켓 쇼핑",
        "desc": "레지덴츠 관람을 3일차로 앞당겨 확보된 황금 같은 여유 시간! 저녁 식사 장소(막시밀리안 거리) 주변의 대형 마트(Edeka, Rewe), dm 드럭스토어, 달마이어 본점에서 시간에 쫓기지 않고 독일 과자, 초콜릿, 발포비타민, 핸드크림, 맥주 등 귀국 선물을 완벽하게 쓸어 담습니다!",
        "tip": "쇼핑 후 호텔에 짐을 두고 오거나, 가벼운 쇼핑백을 들고 바로 앞 켐핀스키 호텔로 여유롭게 이동하세요."
      },
      {
        "id": "d4-7",
        "day": 4,
        "num": 7,
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

# 3. 렌트카 경로 좌표
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

# 4. HTML 파일의 head 부분 가져오기
base_html = open('/Users/min/orca/workspaces/trip/여행/index.html', encoding='utf-8').read()
html_head = base_html.split('<script>')[0]

# 5. 모든 클릭 이벤트와 UI 상호작용이 100% 정상 작동하는 완전무결 JS 코드 작성
robust_js = f"""
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
    url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{{z}}/{{y}}/{{x}}',
    options: {{
      attribution: '&copy; Esri World Street Map',
      maxZoom: 19
    }}
  }},
  esri_satellite: {{
    url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}',
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
      zoomControl: true
    }});

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

function createHotelPin() {{
  const svg = `
    <svg class="marker-svg" viewBox="0 0 36 44" width="36" height="44" xmlns="http://www.w3.org/2000/svg">
      <path d="M18 0C8.06 0 0 8.06 0 18c0 12 18 26 18 26s18-14 18-26c0-9.94-8.06-18-18-18z" fill="#b45309" stroke="#ffffff" stroke-width="1.5"/>
      <circle cx="18" cy="17" r="12" fill="#f59e0b" opacity="0.95"/>
      <text x="18" y="22" font-size="14" text-anchor="middle">🏨</text>
    </svg>
  `;
  return L.divIcon({{
    className: 'custom-div-icon',
    html: `<div class="marker-pin hotel-pin">` + svg + `</div>`,
    iconSize: [36, 44],
    iconAnchor: [18, 42],
    popupAnchor: [0, -40]
  }});
}}

function createHotelMarker() {{
  if (!map) return;
  const pinIcon = createHotelPin();
  hotelMarker = L.marker([HOTEL_DATA.lat, HOTEL_DATA.lng], {{
    icon: pinIcon,
    zIndexOffset: 1000
  }}).addTo(map);

  const popupContent = `
    <div class="popup-badge" style="background:#b45309">🏨 우리 숙소 (Basecamp)</div>
    <div class="popup-title">` + HOTEL_DATA.name + `</div>
    <div style="font-size:11.5px; color:#475569; font-style:italic; margin-bottom:4px;">` + HOTEL_DATA.nameDe + `</div>
    <div style="font-size:11.5px; color:#0f172a; margin-bottom:6px;">📍 ` + HOTEL_DATA.address + `</div>
    <div class="popup-desc">` + HOTEL_DATA.desc + `</div>
    <div style="background:#fef3c7; border-left:3px solid #b45309; padding:5px 8px; border-radius:4px; font-size:11px; color:#92400e; margin-bottom:8px;">💡 ` + HOTEL_DATA.tip + `</div>
    <a class="popup-link" href="` + HOTEL_DATA.googleMapsUrl + `" target="_blank" style="color:#b45309; font-weight:800;">🗺️ Google 지도 열기 →</a>
  `;
  hotelMarker.bindPopup(popupContent);
}}

function createCustomPin(number, color, isHighlight) {{
  const strokeColor = isHighlight ? '#fbbf24' : '#ffffff';
  const strokeWidth = isHighlight ? '2.5' : '1.5';
  const svg = `
    <svg class="marker-svg" viewBox="0 0 32 40" width="32" height="40" xmlns="http://www.w3.org/2000/svg">
      <path d="M16 0C7.163 0 0 7.163 0 16c0 10.5 16 24 16 24s16-13.5 16-24c0-8.837-7.163-16-16-16z" fill="` + color + `" stroke="` + strokeColor + `" stroke-width="` + strokeWidth + `"/>
      <circle cx="16" cy="15" r="10" fill="#ffffff" opacity="0.95"/>
      <text x="16" y="19" fill="` + color + `" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="900" text-anchor="middle">` + number + `</text>
    </svg>
  `;
  return L.divIcon({{
    className: 'custom-div-icon',
    html: `<div class="marker-pin">` + svg + `</div>`,
    iconSize: [32, 40],
    iconAnchor: [16, 38],
    popupAnchor: [0, -36]
  }});
}}

function setMobileView(view) {{
  currentMobileView = view;
  document.body.classList.remove('mobile-mode-list', 'mobile-mode-map');
  document.body.classList.add('mobile-mode-' + view);

  document.querySelectorAll('.mobile-switch-btn').forEach(btn => {{
    if (btn.getAttribute('data-view') === view) {{
      btn.classList.add('active');
    }} else {{
      btn.classList.remove('active');
    }}
  }});

  if (view === 'map') {{
    setTimeout(fixMapSize, 100);
    setTimeout(fixMapSize, 300);
  }}
}}

function focusOnHotel() {{
  if (window.innerWidth <= 900) {{
    setMobileView('map');
  }}
  if (map && hotelMarker) {{
    map.flyTo([HOTEL_DATA.lat, HOTEL_DATA.lng], 15, {{ duration: 0.8 }});
    hotelMarker.openPopup();
  }}
  highlightCarouselCard('carousel-hotel');
}}

function renderView() {{
  if (markersLayerGroup) markersLayerGroup.clearLayers();
  if (polylinesLayerGroup) polylinesLayerGroup.clearLayers();
  spotMarkerMap.clear();

  const timelineContainer = document.getElementById('timelineList');
  if (!timelineContainer) return;

  const existingHotelCard = document.getElementById('hotelBannerCard');
  timelineContainer.innerHTML = '';
  if (existingHotelCard) {{
    timelineContainer.appendChild(existingHotelCard);
  }}

  const latLngsToFit = [
    [HOTEL_DATA.lat, HOTEL_DATA.lng]
  ];

  const targetDays = currentDayFilter === 'all'
    ? ITINERARY_DATA
    : ITINERARY_DATA.filter(d => d.day === parseInt(currentDayFilter));

  updateHeaderSummary(targetDays);
  renderBottomCarousel(targetDays);

  targetDays.forEach(dayData => {{
    const daySection = document.createElement('div');
    daySection.style.marginBottom = '28px';

    if (currentDayFilter === 'all') {{
      const dayHeader = document.createElement('div');
      dayHeader.style.display = 'flex';
      dayHeader.style.alignItems = 'center';
      dayHeader.style.justifyContent = 'space-between';
      dayHeader.style.padding = '8px 0';
      dayHeader.style.marginBottom = '12px';
      dayHeader.style.borderBottom = `2px solid ` + dayData.color;
      dayHeader.innerHTML = `
        <span style="font-weight: 800; font-size: 15px; color: ` + dayData.color + `;">` + dayData.dayLabel + `</span>
        <span style="font-size: 11.5px; color: var(--text-secondary);">` + dayData.spots.length + `개 장소</span>
      `;
      daySection.appendChild(dayHeader);
    }}

    const dayCoords = [];

    if (dayData.day === 2) {{
      ROADTRIP_ROUTE_COORDS.forEach(c => dayCoords.push(c));
    }} else {{
      dayData.spots.forEach(spot => dayCoords.push([spot.lat, spot.lng]));
    }}

    if (polylinesLayerGroup && dayCoords.length > 1) {{
      L.polyline(dayCoords, {{
        color: dayData.color,
        weight: dayData.day === 2 ? 5 : 4,
        opacity: 0.85,
        dashArray: dayData.day === 2 ? '8, 6' : undefined,
        lineJoin: 'round'
      }}).addTo(polylinesLayerGroup);
    }}

    let currentPeriod = '';
    let currentPeriodContainer = null;

    dayData.spots.forEach((spot) => {{
      latLngsToFit.push([spot.lat, spot.lng]);

      if (markersLayerGroup) {{
        const pinIcon = createCustomPin(spot.num, dayData.color, spot.highlight);
        const marker = L.marker([spot.lat, spot.lng], {{
          icon: pinIcon,
          zIndexOffset: spot.highlight ? 500 : 100
        }}).addTo(markersLayerGroup);

        const googleLink = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(spot.name + ' ' + (spot.nameDe || 'Munich'));
        const popupContent = `
          <div class="popup-badge" style="background:` + dayData.color + `">` + dayData.dayLabel + ` #` + spot.num + `</div>
          <div class="popup-title">` + spot.name + `</div>
          <div class="popup-time">🕒 ` + spot.period + ` ` + spot.time + `</div>
          <div class="popup-desc">` + spot.desc + `</div>
          ` + (spot.tip ? `<div style="background:#fffbeb; border-left:3px solid ` + dayData.color + `; padding:5px 8px; border-radius:4px; font-size:11px; color:#92400e; margin-bottom:8px;">💡 ` + spot.tip + `</div>` : '') + `
          <a class="popup-link" href="` + googleLink + `" target="_blank" style="color:` + dayData.color + `; font-weight:800;">🗺️ Google 지도에서 보기 →</a>
        `;
        marker.bindPopup(popupContent);
        spotMarkerMap.set(spot.id, marker);

        marker.on('click', () => {{
          highlightCard(spot.id);
          highlightCarouselCard(`carousel-` + spot.id);
        }});
      }}

      if (spot.period !== currentPeriod) {{
        currentPeriod = spot.period;
        currentPeriodContainer = document.createElement('div');
        currentPeriodContainer.className = 'period-section';
        currentPeriodContainer.innerHTML = `<div class="period-title">` + currentPeriod + ` 일정</div>`;
        daySection.appendChild(currentPeriodContainer);
      }}

      const googleLink = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(spot.name + ' ' + (spot.nameDe || 'Munich'));
      const card = document.createElement('div');
      card.className = 'spot-card';
      card.id = `card-` + spot.id;
      card.innerHTML = `
        <div class="card-top">
          <div class="badge-wrap">
            <span class="spot-num-badge" style="background: ` + dayData.color + `">` + spot.num + `</span>
            <span class="time-badge">` + spot.time + `</span>
          </div>
          <span class="category-badge">` + spot.category + `</span>
        </div>
        <div class="spot-name">` + spot.name + `</div>
        <div class="spot-name-de">` + (spot.nameDe || '') + `</div>
        <div class="spot-desc">` + spot.desc + `</div>
        ` + (spot.tip ? `
          <div class="spot-tip ` + (spot.highlight ? 'highlight' : '') + `">
            <span>` + (spot.highlight ? '🚗' : '💡') + `</span>
            <span>` + spot.tip + `</span>
          </div>
        ` : '') + `
        <div class="card-actions">
          <button class="mini-action-link" style="background:#eff6ff; border:1px solid #bfdbfe; color:#2563eb; cursor:pointer;" onclick="focusOnSpot('` + spot.id + `', ` + spot.lat + `, ` + spot.lng + `)">
            📍 지도에서 보기
          </button>
          <a class="mini-action-link" href="` + googleLink + `" target="_blank">
            🗺️ Google ↗
          </a>
        </div>
      `;

      card.addEventListener('click', (e) => {{
        if (e.target.tagName && (e.target.tagName.toLowerCase() === 'a' || e.target.tagName.toLowerCase() === 'button')) return;
        focusOnSpot(spot.id, spot.lat, spot.lng);
      }});

      if (currentPeriodContainer) {{
        currentPeriodContainer.appendChild(card);
      }}
    }});

    timelineContainer.appendChild(daySection);
  }});

  if (map && latLngsToFit.length > 0) {{
    map.fitBounds(latLngsToFit, {{ padding: [40, 40], maxZoom: 15 }});
  }}
}}

function renderBottomCarousel(targetDays) {{
  const carouselTrack = document.getElementById('carouselTrack');
  const dayTitleElem = document.getElementById('carouselDayTitle');
  if (!carouselTrack) return;

  if (dayTitleElem) {{
    if (currentDayFilter === 'all') {{
      dayTitleElem.textContent = '전체 4일 코스 스팟 둘러보기';
    }} else {{
      const cur = targetDays[0];
      dayTitleElem.textContent = `${{cur.dayLabel}} 스팟 (${{cur.spots.length}}곳)`;
    }}
  }}

  let cardsHtml = '';

  // 첫 번째 카드는 항상 우리 숙소
  cardsHtml += `
    <div class="carousel-card" id="carousel-hotel" onclick="focusOnHotel()">
      <div class="carousel-card-top">
        <span class="carousel-badge" style="background:#b45309;">🏨 베이스캠프</span>
        <a class="carousel-google-link" href="${{HOTEL_DATA.googleMapsUrl}}" target="_blank" rel="noopener" onclick="event.stopPropagation();">길찾기 ↗</a>
      </div>
      <div class="carousel-card-title">${{HOTEL_DATA.name}}</div>
      <div class="carousel-card-sub">중앙역 트램 5분 · 님펜부르크 직통</div>
      <div class="carousel-card-desc">${{HOTEL_DATA.desc}}</div>
    </div>
  `;

  targetDays.forEach(dayInfo => {{
    dayInfo.spots.forEach(spot => {{
      const gUrl = `https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent(spot.name + ' ' + (spot.nameDe || 'Munich'))}}`;
      cardsHtml += `
        <div class="carousel-card" id="carousel-${{spot.id}}" onclick="focusOnSpot('${{spot.id}}', ${{spot.lat}}, ${{spot.lng}})">
          <div class="carousel-card-top">
            <span class="carousel-badge" style="background:${{dayInfo.color}};">${{dayInfo.dayLabel}} #${{spot.num}}</span>
            <a class="carousel-google-link" href="${{gUrl}}" target="_blank" rel="noopener" onclick="event.stopPropagation();">Google ↗</a>
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

function highlightCard(spotId) {{
  document.querySelectorAll('.spot-card').forEach(c => c.classList.remove('selected'));
  const targetCard = document.getElementById(`card-` + spotId);
  if (targetCard) {{
    targetCard.classList.add('selected');
    targetCard.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
  }}
}}

function highlightCarouselCard(carouselId) {{
  document.querySelectorAll('.carousel-card').forEach(c => c.classList.remove('active'));
  const target = document.getElementById(carouselId);
  if (target) {{
    target.classList.add('active');
    target.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
  }}
}}

function focusOnSpot(spotId, lat, lng) {{
  highlightCard(spotId);
  highlightCarouselCard(`carousel-` + spotId);

  if (window.innerWidth <= 900) {{
    setMobileView('map');
  }}
  if (map) {{
    map.flyTo([lat, lng], 15, {{ duration: 0.8 }});
    const marker = spotMarkerMap.get(spotId);
    if (marker) {{
      marker.openPopup();
    }}
  }}
}}

function updateHeaderSummary(targetDays) {{
  const titleEl = document.getElementById('dayTitleText');
  const countBadge = document.getElementById('spotCountBadge');
  const transitTipEl = document.getElementById('transitTipText');
  const googleHeaderBtn = document.getElementById('googleRouteHeaderBtn');

  if (currentDayFilter === 'all') {{
    if (titleEl) titleEl.textContent = '전체 4일 일정 개요 (20일 ~ 23일)';
    const totalSpots = ITINERARY_DATA.reduce((acc, cur) => acc + cur.spots.length, 0);
    if (countBadge) countBadge.textContent = `총 ` + totalSpots + `개 방문지`;
    if (transitTipEl) transitTipEl.innerHTML = `💡 날짜 탭을 누르면 렌트카 코스 및 일자별 세부 동선을 확인할 수 있습니다.`;
    if (googleHeaderBtn) {{
      googleHeaderBtn.href = ITINERARY_DATA[1].googleRouteUrl;
      googleHeaderBtn.textContent = '🚗 2일차 렌트카 전체 경로 (Google Maps)';
    }}
  }} else {{
    const d = targetDays[0];
    if (titleEl) titleEl.textContent = d.title;
    if (countBadge) countBadge.textContent = d.spots.length + `개 방문지`;
    if (transitTipEl) transitTipEl.innerHTML = d.transitTip;
    if (googleHeaderBtn) {{
      googleHeaderBtn.href = d.googleRouteUrl || 'https://www.google.com/maps';
      googleHeaderBtn.textContent = `🗺️ ` + d.dayLabel + ` Google Maps 경로 열기`;
    }}
  }}
}}

// ==========================================
// ★★★ 모든 이벤트 리스너 완벽 연결 ★★★
// ==========================================

// 1. 일자별 탭 버튼 클릭
document.querySelectorAll('.tab-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentDayFilter = btn.getAttribute('data-day');
    renderView();
    setTimeout(fixMapSize, 150);
  }});
}});

// 2. 모바일 세그먼트 스위치 버튼 (일정 목록 / 지도 전체 보기)
document.querySelectorAll('.mobile-switch-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    const targetView = btn.getAttribute('data-view');
    setMobileView(targetView);
  }});
}});

// 3. 지도 맞춤 버튼
const fitBtn = document.getElementById('btnFitBounds');
if (fitBtn) {{
  fitBtn.addEventListener('click', () => {{
    const targetDays = currentDayFilter === 'all' 
      ? ITINERARY_DATA 
      : ITINERARY_DATA.filter(d => d.day === parseInt(currentDayFilter));
    
    const coords = [[HOTEL_DATA.lat, HOTEL_DATA.lng]];
    targetDays.forEach(d => d.spots.forEach(s => coords.push([s.lat, s.lng])));
    if (map && coords.length > 0) {{
      map.fitBounds(coords, {{ padding: [40, 40] }});
    }}
  }});
}}

// 4. 지도 스타일 전환 버튼
const toggleTileBtn = document.getElementById('btnToggleTile');
if (toggleTileBtn) {{
  toggleTileBtn.addEventListener('click', () => {{
    if (!map) return;
    map.removeLayer(tileLayer);
    if (currentTileMode === 'voyager') {{
      currentTileMode = 'esri_street';
      tileLayer = L.tileLayer(TILE_PROVIDERS.esri_street.url, TILE_PROVIDERS.esri_street.options).addTo(map);
    }} else if (currentTileMode === 'esri_street') {{
      currentTileMode = 'esri_satellite';
      tileLayer = L.tileLayer(TILE_PROVIDERS.esri_satellite.url, TILE_PROVIDERS.esri_satellite.options).addTo(map);
    }} else {{
      currentTileMode = 'voyager';
      tileLayer = L.tileLayer(TILE_PROVIDERS.voyager.url, TILE_PROVIDERS.voyager.options).addTo(map);
    }}
  }});
}}

// 5. 일정표 모달 팝업
const modal = document.getElementById('originalModal');
const pdfBtn = document.getElementById('btnOriginalPdf');
const closeBtn = document.getElementById('modalCloseBtn');
if (pdfBtn && modal) {{
  pdfBtn.addEventListener('click', () => {{ modal.classList.add('open'); }});
}}
if (closeBtn && modal) {{
  closeBtn.addEventListener('click', () => {{ modal.classList.remove('open'); }});
}}
if (modal) {{
  modal.addEventListener('click', (e) => {{
    if (e.target === modal) modal.classList.remove('open');
  }});
}}

// 6. 숙소 배너 카드 클릭
const hotelBanner = document.getElementById('hotelBannerCard');
if (hotelBanner) {{
  hotelBanner.addEventListener('click', (e) => {{
    if (e.target.tagName && e.target.tagName.toLowerCase() === 'a') return;
    focusOnHotel();
  }});
}}

// 7. 지도 범례 접기/펼치기
const legendHeader = document.getElementById('legendHeader');
if (legendHeader) {{
  legendHeader.addEventListener('click', () => {{
    const mapLegend = document.getElementById('mapLegend');
    if (mapLegend) mapLegend.classList.toggle('collapsed');
  }});
}}

// 8. 하단 캐러셀 제어 버튼 (접기/열기, 이전, 다음)
const carouselToggleBtn = document.getElementById('carouselToggleBtn');
if (carouselToggleBtn) {{
  carouselToggleBtn.addEventListener('click', () => {{
    const container = document.getElementById('bottomCarousel');
    if (!container) return;
    const isCollapsed = container.classList.toggle('collapsed');
    carouselToggleBtn.textContent = isCollapsed ? '▲ 스팟 보기' : '▼ 접기';
  }});
}}

const carouselPrevBtn = document.getElementById('carouselPrevBtn');
if (carouselPrevBtn) {{
  carouselPrevBtn.addEventListener('click', () => {{
    const track = document.getElementById('carouselTrack');
    if (track) track.scrollBy({{ left: -260, behavior: 'smooth' }});
  }});
}}

const carouselNextBtn = document.getElementById('carouselNextBtn');
if (carouselNextBtn) {{
  carouselNextBtn.addEventListener('click', () => {{
    const track = document.getElementById('carouselTrack');
    if (track) track.scrollBy({{ left: 260, behavior: 'smooth' }});
  }});
}}

// 9. 페이지 로드 초기화
window.addEventListener('DOMContentLoaded', () => {{
  if (window.innerWidth <= 900) {{
    setMobileView('list');
    const mapLegend = document.getElementById('mapLegend');
    if (mapLegend) mapLegend.classList.add('collapsed');
  }}
  initMap();
}});
"""

final_html = f"{html_head}<script>{robust_js}</script>\n</body>\n</html>"

# 파일 3개 작성
target_files = [
    '/Users/min/orca/workspaces/trip/여행/index.html',
    '/Users/min/orca/workspaces/trip/여행/munich_itinerary.html',
    '/Users/min/orca/workspaces/trip/여행/뮌헨_여행_일정_지도.html'
]

for tf in target_files:
    with open(tf, 'w', encoding='utf-8') as f:
        f.write(final_html)

print("All HTML files rebuilt with 100% robust event listeners!")
