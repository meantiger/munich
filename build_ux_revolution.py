import json

hotel_data = {
    "name": "노보텔 뮌헨 시티 아르눌프파크 (우리 숙소)",
    "nameDe": "Novotel München City Arnulfpark",
    "lat": 48.1454917,
    "lng": 11.5389985,
    "address": "Arnulfstraße 57, 80636 München",
    "googleMapsUrl": "https://maps.app.goo.gl/LNwTawdtw64NZc248",
    "desc": "이번 뮌헨 여행의 베이스캠프! Donnersbergerbrücke S-Bahn역 및 트램(16, 17번) 정류장 도보 2분! 중앙역, 마리엔 광장, 님펜부르크 궁전 이동 최적.",
    "tip": "호텔 바로 앞 트램 17번을 타면 중앙역 및 님펜부르크 궁전까지 환승 없이 직통 이동!"
}

# 기존 munich_itinerary.html에서 ITINERARY_DATA 추출
content = open('/Users/min/orca/workspaces/trip/여행/munich_itinerary.html', encoding='utf-8').read()
itinerary_part = content.split('const ITINERARY_DATA = ')[1].split('const ROADTRIP_ROUTE_COORDS = ')[0].strip()

# Leaflet CSS 가져오기
import os
css_path = '/Users/min/orca/workspaces/trip/여행/leaflet_inline.css'
if not os.path.exists(css_path):
    os.system(f'curl -s https://unpkg.com/leaflet@1.9.4/dist/leaflet.css > {css_path}')

with open(css_path, encoding='utf-8') as f:
    leaflet_css = f.read()

# 모바일 최고 경험 JS 코드 작성
js_code = f"""
const HOTEL_DATA = {json.dumps(hotel_data, ensure_ascii=False, indent=2)};

const ITINERARY_DATA = {itinerary_part}

const ROADTRIP_ROUTE_COORDS = [
  [48.1374, 11.5755],
  [48.1300, 11.4500],
  [48.0600, 11.0000],
  [48.0500, 10.8700],
  [47.8000, 10.8700],
  [47.5750, 10.7400],
  [47.5552, 10.7496],
  [47.5576, 10.7498],
  [47.5539, 10.7380],
  [47.5300, 10.7100],
  [47.4890, 10.7180],
  [47.4000, 10.9160],
  [47.4565, 10.9922],
  [47.4211, 10.9853],
  [47.4565, 10.9922],
  [47.4920, 11.0950],
  [47.7100, 11.2000],
  [47.9900, 11.3400],
  [48.1374, 11.5755]
];

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
      zoomControl: false // 모바일 화면 확보를 위해 커스텀 컨트롤 사용
    }});

    // 줌 컨트롤 우측 상단 배치
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

function createHotelPin() {{
  const svg = `
    <svg class="marker-svg" viewBox="0 0 36 44" width="36" height="44" xmlns="http://www.w3.org/2000/svg">
      <path d="M18 0C8.06 0 0 8.06 0 18c0 12 18 26 18 26s18-14 18-26c0-9.94-8.06-18-18-18z" fill="#e11d48"/>
      <circle cx="18" cy="17" r="12" fill="#ffffff" opacity="0.95"/>
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
    <div class="popup-badge" style="background:#e11d48">🏨 우리 숙소 (Basecamp)</div>
    <div class="popup-title">` + HOTEL_DATA.name + `</div>
    <div style="font-size:11px; color:#475569; font-style:italic; margin-bottom:3px;">` + HOTEL_DATA.nameDe + `</div>
    <div style="font-size:11px; color:#0f172a; margin-bottom:5px;">📍 ` + HOTEL_DATA.address + `</div>
    <div class="popup-desc">` + HOTEL_DATA.desc + `</div>
    <div style="background:#fff1f2; border-left:3px solid #e11d48; padding:4px 8px; border-radius:4px; font-size:10.5px; color:#9f1239; margin-bottom:6px;">💡 ` + HOTEL_DATA.tip + `</div>
    <a class="popup-link" href="` + HOTEL_DATA.googleMapsUrl + `" target="_blank" style="color:#e11d48; font-weight:800;">🗺️ Google 지도 열기 →</a>
  `;
  hotelMarker.bindPopup(popupContent);

  hotelMarker.on('click', () => {{
    highlightCarouselCard('hotel');
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
  highlightCarouselCard('hotel');
  if (map && hotelMarker) {{
    map.flyTo([HOTEL_DATA.lat, HOTEL_DATA.lng], 16, {{ duration: 0.8 }});
    hotelMarker.openPopup();
  }}
}}

function createCustomPin(number, color) {{
  const svg = `
    <svg class="marker-svg" viewBox="0 0 32 40" width="32" height="40" xmlns="http://www.w3.org/2000/svg">
      <path d="M16 0C7.163 0 0 7.163 0 16c0 10.5 16 24 16 24s16-13.5 16-24c0-8.837-7.163-16-16-16z" fill="` + color + `"/>
      <circle cx="16" cy="15" r="10" fill="#ffffff" opacity="0.95"/>
      <text x="16" y="19" fill="` + color + `" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">` + number + `</text>
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

  // 하단 캐러셀 트랙 준비
  const carouselTrack = document.getElementById('carouselTrack');
  if (carouselTrack) {{
    carouselTrack.innerHTML = '';
  }}

  // 캐러셀 첫 번째 카드: 숙소 카드
  if (carouselTrack) {{
    const hotelCard = document.createElement('div');
    hotelCard.className = 'carousel-card';
    hotelCard.id = 'carousel-card-hotel';
    hotelCard.innerHTML = `
      <div class="carousel-card-top">
        <span class="carousel-badge" style="background:#e11d48">🏨 우리 숙소</span>
        <a class="carousel-google-link" href="` + HOTEL_DATA.googleMapsUrl + `" target="_blank">Google ↗</a>
      </div>
      <div class="carousel-card-title">` + HOTEL_DATA.name + `</div>
      <div class="carousel-card-sub">` + HOTEL_DATA.nameDe + `</div>
      <div class="carousel-card-desc">트램 16/17번 및 S-Bahn 도보 2분! 중앙역·궁전 이동 편리</div>
    `;
    hotelCard.addEventListener('click', (e) => {{
      if (e.target.tagName && e.target.tagName.toLowerCase() === 'a') return;
      focusOnHotel();
    }});
    carouselTrack.appendChild(hotelCard);
  }}

  const latLngsToFit = [
    [HOTEL_DATA.lat, HOTEL_DATA.lng]
  ];

  const targetDays = currentDayFilter === 'all' 
    ? ITINERARY_DATA 
    : ITINERARY_DATA.filter(d => d.day === parseInt(currentDayFilter));

  updateHeaderSummary(targetDays);

  targetDays.forEach(dayData => {{
    const daySection = document.createElement('div');
    daySection.style.marginBottom = '24px';

    if (currentDayFilter === 'all') {{
      const dayHeader = document.createElement('div');
      dayHeader.style.display = 'flex';
      dayHeader.style.alignItems = 'center';
      dayHeader.style.justifyContent = 'space-between';
      dayHeader.style.padding = '8px 0';
      dayHeader.style.marginBottom = '12px';
      dayHeader.style.borderBottom = `2px solid ` + dayData.color;
      dayHeader.innerHTML = `
        <span style="font-weight: 800; font-size: 14.5px; color: ` + dayData.color + `;">` + dayData.dayLabel + `</span>
        <span style="font-size: 11px; color: var(--text-secondary);">` + dayData.spots.length + `개 장소</span>
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
        const pinIcon = createCustomPin(spot.num, dayData.color);
        const marker = L.marker([spot.lat, spot.lng], {{ icon: pinIcon }})
          .addTo(markersLayerGroup);

        const googleLink = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(spot.name + ' ' + (spot.nameDe || ''));
        const popupContent = `
          <div class="popup-badge" style="background:` + dayData.color + `">` + dayData.dayLabel + ` #` + spot.num + `</div>
          <div class="popup-title">` + spot.name + `</div>
          <div class="popup-time">🕒 ` + spot.time + `</div>
          <div class="popup-desc">` + spot.desc + `</div>
          ` + (spot.tip ? `<div style="background:#fffbeb; padding:4px 8px; border-radius:4px; font-size:10.5px; color:#92400e; margin-bottom:6px;">💡 ` + spot.tip + `</div>` : '') + `
          <a class="popup-link" href="` + googleLink + `" target="_blank">🗺️ Google 지도에서 보기 →</a>
        `;
        marker.bindPopup(popupContent);
        spotMarkerMap.set(spot.id, marker);

        marker.on('click', () => {{
          highlightCard(spot.id);
          highlightCarouselCard(spot.id);
        }});
      }}

      if (spot.period !== currentPeriod) {{
        currentPeriod = spot.period;
        currentPeriodContainer = document.createElement('div');
        currentPeriodContainer.className = 'period-section';
        currentPeriodContainer.innerHTML = `<div class="period-title">` + currentPeriod + ` 일정</div>`;
        daySection.appendChild(currentPeriodContainer);
      }}

      const googleLink = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(spot.name + ' ' + (spot.nameDe || ''));
      
      // 1. 좌측 사이드바 카드
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

      // 2. 지도 하단 스와이프 캐러셀 카드
      if (carouselTrack) {{
        const cCard = document.createElement('div');
        cCard.className = 'carousel-card';
        cCard.id = `carousel-card-` + spot.id;
        cCard.innerHTML = `
          <div class="carousel-card-top">
            <span class="carousel-badge" style="background:` + dayData.color + `">#` + spot.num + ` ` + spot.time + `</span>
            <a class="carousel-google-link" href="` + googleLink + `" target="_blank">Google ↗</a>
          </div>
          <div class="carousel-card-title">` + spot.name + `</div>
          <div class="carousel-card-sub">` + (spot.nameDe || '') + `</div>
          <div class="carousel-card-desc">` + spot.desc.substring(0, 60) + `...</div>
        `;
        cCard.addEventListener('click', (e) => {{
          if (e.target.tagName && e.target.tagName.toLowerCase() === 'a') return;
          focusOnSpot(spot.id, spot.lat, spot.lng);
        }});
        carouselTrack.appendChild(cCard);
      }}
    }});

    timelineContainer.appendChild(daySection);
  }});

  if (map && latLngsToFit.length > 0) {{
    map.fitBounds(latLngsToFit, {{ padding: [30, 30], maxZoom: 15 }});
  }}
}}

function highlightCard(spotId) {{
  document.querySelectorAll('.spot-card').forEach(c => c.classList.remove('selected'));
  const targetCard = document.getElementById(`card-` + spotId);
  if (targetCard) {{
    targetCard.classList.add('selected');
    targetCard.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
  }}
}}

function highlightCarouselCard(spotId) {{
  currentActiveSpotId = spotId;
  document.querySelectorAll('.carousel-card').forEach(c => c.classList.remove('active'));
  const targetCard = document.getElementById(`carousel-card-` + spotId);
  if (targetCard) {{
    targetCard.classList.add('active');
    targetCard.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
  }}
}}

function focusOnSpot(spotId, lat, lng) {{
  highlightCard(spotId);
  highlightCarouselCard(spotId);

  if (window.innerWidth <= 900 && currentMobileView !== 'map') {{
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
  const carouselDayTitle = document.getElementById('carouselDayTitle');

  if (currentDayFilter === 'all') {{
    if (titleEl) titleEl.textContent = '전체 4일 일정 개요 (20일 ~ 23일)';
    const totalSpots = ITINERARY_DATA.reduce((acc, cur) => acc + cur.spots.length, 0);
    if (countBadge) countBadge.textContent = `총 ` + totalSpots + `개 방문지`;
    if (transitTipEl) transitTipEl.innerHTML = `💡 날짜 탭을 누르면 렌트카 코스 및 일자별 세부 동선을 확인할 수 있습니다.`;
    if (carouselDayTitle) carouselDayTitle.textContent = '전체 코스 스팟 둘러보기';
    if (googleHeaderBtn) {{
      googleHeaderBtn.href = ITINERARY_DATA[1].googleRouteUrl;
      googleHeaderBtn.textContent = '🚗 2일차 렌트카 경로';
    }}
  }} else {{
    const d = targetDays[0];
    if (titleEl) titleEl.textContent = d.title;
    if (countBadge) countBadge.textContent = d.spots.length + `개 방문지`;
    if (transitTipEl) transitTipEl.innerHTML = d.transitTip;
    if (carouselDayTitle) carouselDayTitle.textContent = d.dayLabel + ` 코스 스팟 (` + d.spots.length + `곳)`;
    if (googleHeaderBtn) {{
      googleHeaderBtn.href = d.googleRouteUrl || 'https://www.google.com/maps';
      googleHeaderBtn.textContent = `🗺️ ` + d.dayLabel + ` Google 경로`;
    }}
  }}
}}

// 날짜 필터 탭
document.querySelectorAll('.tab-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentDayFilter = btn.getAttribute('data-day');
    renderView();
    setTimeout(fixMapSize, 150);
  }});
}});

// 모바일 뷰 스위처
document.querySelectorAll('.mobile-switch-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    const targetView = btn.getAttribute('data-view');
    setMobileView(targetView);
  }});
}});

// 지도 맞춤 버튼
const fitBtn = document.getElementById('btnFitBounds');
if (fitBtn) {{
  fitBtn.addEventListener('click', () => {{
    const targetDays = currentDayFilter === 'all' 
      ? ITINERARY_DATA 
      : ITINERARY_DATA.filter(d => d.day === parseInt(currentDayFilter));
    
    const coords = [[HOTEL_DATA.lat, HOTEL_DATA.lng]];
    targetDays.forEach(d => d.spots.forEach(s => coords.push([s.lat, s.lng])));
    if (map && coords.length > 0) {{
      map.fitBounds(coords, {{ padding: [30, 30] }});
    }}
  }});
}}

// 지도 타일 전환
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

// 범례 최소화 토글
const legendBox = document.getElementById('mapLegend');
const legendHeader = document.getElementById('legendHeader');
if (legendHeader && legendBox) {{
  legendHeader.addEventListener('click', () => {{
    legendBox.classList.toggle('collapsed');
  }});
}}

// 하단 캐러셀 접기/펼치기 토글
const carouselBox = document.getElementById('bottomCarousel');
const carouselToggleBtn = document.getElementById('carouselToggleBtn');
if (carouselToggleBtn && carouselBox) {{
  carouselToggleBtn.addEventListener('click', () => {{
    carouselBox.classList.toggle('collapsed');
    const isCollapsed = carouselBox.classList.contains('collapsed');
    carouselToggleBtn.innerHTML = isCollapsed 
      ? '▲ 코스 카드 보기' 
      : '▼ 접기';
  }});
}}

// 하단 캐러셀 좌우 이동 버튼
const carouselPrevBtn = document.getElementById('carouselPrevBtn');
const carouselNextBtn = document.getElementById('carouselNextBtn');
const carouselTrackEl = document.getElementById('carouselTrack');
if (carouselPrevBtn && carouselTrackEl) {{
  carouselPrevBtn.addEventListener('click', () => {{
    carouselTrackEl.scrollBy({{ left: -260, behavior: 'smooth' }});
  }});
}}
if (carouselNextBtn && carouselTrackEl) {{
  carouselNextBtn.addEventListener('click', () => {{
    carouselTrackEl.scrollBy({{ left: 260, behavior: 'smooth' }});
  }});
}}

// 모달 창
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

const hotelBanner = document.getElementById('hotelBannerCard');
if (hotelBanner) {{
  hotelBanner.addEventListener('click', (e) => {{
    if (e.target.tagName && e.target.tagName.toLowerCase() === 'a') return;
    focusOnHotel();
  }});
}}

window.addEventListener('DOMContentLoaded', () => {{
  if (window.innerWidth <= 900) {{
    setMobileView('list');
    // 모바일에서는 범례를 기본적으로 접어둠
    if (legendBox) legendBox.classList.add('collapsed');
  }}
  initMap();
}});
"""

# HTML 템플릿 작성
full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>뮌헨 & 바이에른 4일 여행 가이드 (모바일 최적화)</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Leaflet Core CSS (100% 인라인 내장) -->
  <style>
{leaflet_css}
  </style>

  <!-- 애플리케이션 반응형 스타일 -->
  <style>
    :root {{
      --font-main: 'Pretendard', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --bg-main: #f8fafc;
      --bg-card: #ffffff;
      --border-color: #e2e8f0;
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-muted: #94a3b8;
      
      --color-day1: #2563eb;
      --color-day2: #059669;
      --color-day3: #7c3aed;
      --color-day4: #d97706;
      
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      width: 100%;
      height: 100%;
      margin: 0;
      padding: 0;
      overflow: hidden;
      font-family: var(--font-main);
      background-color: var(--bg-main);
      color: var(--text-primary);
    }}

    body {{
      display: flex;
      flex-direction: column;
    }}

    /* 상단 헤더 */
    header {{
      flex-shrink: 0;
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 8px 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      z-index: 1000;
      box-shadow: var(--shadow-sm);
    }}

    .header-top-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .brand-badge {{
      background: linear-gradient(135deg, #1e3a8a, #2563eb);
      color: white;
      padding: 5px 9px;
      border-radius: 7px;
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      box-shadow: 0 2px 4px rgba(37, 99, 235, 0.25);
      white-space: nowrap;
    }}

    .header-title-group h1 {{
      font-size: 16px;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .header-title-group p {{
      font-size: 11px;
      color: var(--text-secondary);
      margin-top: 1px;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .action-btn {{
      background: white;
      border: 1px solid var(--border-color);
      padding: 5px 9px;
      border-radius: 7px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      color: var(--text-secondary);
      transition: all 0.15s ease;
      text-decoration: none;
      white-space: nowrap;
    }}

    .action-btn:hover {{
      background: #f8fafc;
      border-color: #cbd5e1;
      color: var(--text-primary);
    }}

    .action-btn.primary {{
      background: #10b981;
      color: white;
      border-color: #059669;
      font-weight: 800;
      box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);
    }}

    /* 모바일 뷰 전환 세그먼트 (모바일 전용) */
    .mobile-view-switcher {{
      display: none;
      background: #e2e8f0;
      padding: 3px;
      border-radius: 9px;
      width: 100%;
    }}
    .mobile-switch-btn {{
      flex: 1;
      border: none;
      background: transparent;
      padding: 7px 10px;
      border-radius: 7px;
      font-size: 12px;
      font-weight: 700;
      color: var(--text-secondary);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .mobile-switch-btn.active {{
      background: #ffffff;
      color: #0f172a;
      box-shadow: var(--shadow-sm);
    }}

    /* 일자별 필터 탭 (가로 스와이프 지원) */
    .day-tabs {{
      display: flex;
      background: #f1f5f9;
      padding: 3px;
      border-radius: 9px;
      gap: 3px;
      overflow-x: auto;
      white-space: nowrap;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }}
    .day-tabs::-webkit-scrollbar {{
      display: none;
    }}

    .tab-btn {{
      border: none;
      background: transparent;
      padding: 6px 10px;
      border-radius: 7px;
      font-size: 11.5px;
      font-weight: 600;
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 5px;
      white-space: nowrap;
      flex-shrink: 0;
    }}

    .tab-btn:hover {{
      background: rgba(255, 255, 255, 0.7);
      color: var(--text-primary);
    }}

    .tab-btn.active {{
      background: #ffffff;
      color: #0f172a;
      box-shadow: var(--shadow-sm);
      font-weight: 800;
    }}

    .tab-btn .tab-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      display: inline-block;
    }}

    /* 메인 레이아웃 */
    .main-layout {{
      flex: 1;
      display: flex;
      overflow: hidden;
      position: relative;
      width: 100%;
      height: calc(100vh - 110px);
    }}

    /* 좌측 사이드바 */
    .sidebar {{
      width: 480px;
      min-width: 420px;
      background: #ffffff;
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      height: 100%;
      flex-shrink: 0;
      z-index: 10;
    }}

    .sidebar-header {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-color);
      background: #fafafa;
    }}

    .sidebar-title {{
      font-size: 14.5px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .transit-badge {{
      font-size: 11px;
      padding: 5px 8px;
      border-radius: 6px;
      background: #eff6ff;
      color: #1d4ed8;
      font-weight: 600;
      margin-top: 6px;
      display: block;
      line-height: 1.4;
      border: 1px solid #bfdbfe;
    }}

    /* 숙소 배너 카드 스타일 */
    .hotel-banner-card {{
      background: linear-gradient(135deg, #fff1f2, #ffe4e6);
      border: 1.5px solid #fecdd3;
      border-radius: 12px;
      padding: 10px 12px;
      margin-bottom: 12px;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }}
    .hotel-banner-card:hover {{
      border-color: #f43f5e;
      box-shadow: var(--shadow-md);
      transform: translateY(-1px);
    }}
    .hotel-banner-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 3px;
    }}
    .hotel-badge {{
      background: #e11d48;
      color: white;
      font-size: 10.5px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 5px;
      letter-spacing: 0.5px;
    }}
    .hotel-map-link {{
      font-size: 11px;
      color: #be123c;
      text-decoration: none;
      font-weight: 800;
    }}
    .hotel-name {{
      font-size: 14px;
      font-weight: 800;
      color: #881337;
      line-height: 1.3;
    }}
    .hotel-name-de {{
      font-size: 11px;
      color: #9f1239;
      font-style: italic;
      margin-bottom: 3px;
    }}
    .hotel-desc {{
      font-size: 11px;
      color: #4c0519;
      line-height: 1.4;
    }}
    .hotel-action-hint {{
      font-size: 10px;
      color: #e11d48;
      font-weight: 700;
      margin-top: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .timeline-container {{
      flex: 1;
      overflow-y: auto;
      padding: 12px 14px 40px;
      scroll-behavior: smooth;
      -webkit-overflow-scrolling: touch;
    }}

    .period-section {{
      margin-bottom: 18px;
    }}

    .period-title {{
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--text-muted);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .period-title::after {{
      content: '';
      flex: 1;
      height: 1px;
      background: var(--border-color);
    }}

    .spot-card {{
      position: relative;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 11px;
      padding: 11px 13px;
      margin-bottom: 9px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .spot-card:hover {{
      border-color: #94a3b8;
      box-shadow: var(--shadow-md);
    }}

    .spot-card.selected {{
      border-color: #2563eb;
      background: #eff6ff;
      box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.25);
    }}

    .card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .badge-wrap {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .spot-num-badge {{
      width: 20px;
      height: 20px;
      border-radius: 50%;
      color: white;
      font-size: 10.5px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .time-badge {{
      font-size: 11px;
      font-weight: 700;
      color: #334155;
      background: #f1f5f9;
      padding: 2px 7px;
      border-radius: 5px;
    }}

    .category-badge {{
      font-size: 10.5px;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .spot-name {{
      font-size: 14px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.3;
    }}

    .spot-name-de {{
      font-size: 11px;
      color: var(--text-secondary);
      font-style: italic;
    }}

    .spot-desc {{
      font-size: 11.5px;
      color: var(--text-secondary);
      line-height: 1.45;
      margin-top: 2px;
    }}

    .spot-tip {{
      margin-top: 5px;
      background: #fffbeb;
      border-left: 3px solid #f59e0b;
      padding: 4px 8px;
      border-radius: 0 5px 5px 0;
      font-size: 10.5px;
      color: #92400e;
      line-height: 1.4;
      display: flex;
      align-items: flex-start;
      gap: 4px;
    }}

    .spot-tip.highlight {{
      background: #fef2f2;
      border-left-color: #ef4444;
      color: #991b1b;
      font-weight: 600;
    }}

    .card-actions {{
      display: flex;
      justify-content: flex-end;
      gap: 6px;
      margin-top: 5px;
    }}

    .mini-action-link {{
      font-size: 11px;
      color: #0369a1;
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      padding: 4px 7px;
      border-radius: 5px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 3px;
      font-weight: 700;
      transition: all 0.15s;
    }}

    /* 우측 맵 컨테이너 */
    .map-container {{
      flex: 1;
      height: 100%;
      position: relative;
      background: #e2e8f0;
    }}

    #map {{
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      width: 100% !important;
      height: 100% !important;
      z-index: 1;
    }}

    /* 지도 상단 컨트롤 */
    .map-overlay-controls {{
      position: absolute;
      top: 10px;
      right: 50px;
      z-index: 500;
      display: flex;
      gap: 6px;
    }}

    .map-ctrl-btn {{
      background: white;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 6px 9px;
      font-size: 11px;
      font-weight: 700;
      color: var(--text-primary);
      box-shadow: var(--shadow-md);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    /* ★★★ 접기/최소화 가능한 범례(Legend) ★★★ */
    .map-legend {{
      position: absolute;
      top: 10px;
      left: 10px;
      z-index: 500;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-color);
      border-radius: 9px;
      padding: 8px 10px;
      box-shadow: var(--shadow-md);
      font-size: 11px;
      max-width: 260px;
      transition: all 0.2s ease;
    }}

    .legend-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      cursor: pointer;
      user-select: none;
    }}

    .legend-title {{
      font-weight: 800;
      font-size: 11px;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 4px;
      margin: 0;
    }}

    .legend-toggle-btn {{
      font-size: 10px;
      color: #64748b;
      background: #f1f5f9;
      border-radius: 4px;
      padding: 1px 5px;
      font-weight: 600;
    }}

    .legend-body {{
      margin-top: 6px;
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}

    .map-legend.collapsed .legend-body {{
      display: none;
    }}

    .legend-item {{
      display: flex;
      align-items: center;
      gap: 5px;
      color: var(--text-secondary);
      font-size: 10px;
    }}

    .legend-color {{
      width: 9px;
      height: 9px;
      border-radius: 2px;
      flex-shrink: 0;
    }}

    /* ★★★ 지도 보기 모드 하단 스팟 캐러셀 (Mobile-First) ★★★ */
    .bottom-carousel-container {{
      position: absolute;
      bottom: 12px;
      left: 10px;
      right: 10px;
      z-index: 500;
      display: flex;
      flex-direction: column;
      gap: 5px;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .bottom-carousel-container.collapsed {{
      transform: translateY(calc(100% - 28px));
    }}

    .carousel-top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 4px;
    }}

    .carousel-day-title {{
      font-size: 11px;
      font-weight: 800;
      color: #ffffff;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(6px);
      padding: 3px 8px;
      border-radius: 12px;
      box-shadow: var(--shadow-sm);
    }}

    .carousel-actions {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .carousel-toggle-btn {{
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(6px);
      color: white;
      border: none;
      border-radius: 12px;
      padding: 3px 8px;
      font-size: 10.5px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 3px;
    }}

    .carousel-nav-btn {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: white;
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: bold;
      cursor: pointer;
      color: #0f172a;
    }}

    .carousel-track {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      -webkit-overflow-scrolling: touch;
      padding: 4px 2px;
      scrollbar-width: none;
    }}
    .carousel-track::-webkit-scrollbar {{
      display: none;
    }}

    .carousel-card {{
      flex: 0 0 250px;
      scroll-snap-align: center;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(10px);
      border: 1.5px solid var(--border-color);
      border-radius: 12px;
      padding: 9px 12px;
      box-shadow: var(--shadow-lg);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 3px;
      transition: all 0.2s;
    }}

    .carousel-card.active {{
      border-color: #2563eb;
      background: #ffffff;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
      transform: translateY(-2px);
    }}

    .carousel-card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .carousel-badge {{
      font-size: 10px;
      font-weight: 800;
      color: white;
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .carousel-google-link {{
      font-size: 10.5px;
      color: #0369a1;
      font-weight: 700;
      text-decoration: none;
    }}

    .carousel-card-title {{
      font-size: 13px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.25;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .carousel-card-sub {{
      font-size: 10.5px;
      color: var(--text-secondary);
      font-style: italic;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .carousel-card-desc {{
      font-size: 10.5px;
      color: #475569;
      line-height: 1.35;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .custom-div-icon {{
      background: transparent !important;
      border: none !important;
    }}

    .marker-pin {{
      width: 32px;
      height: 38px;
      position: relative;
      cursor: pointer;
      transition: transform 0.15s ease;
    }}

    .marker-pin:hover {{
      transform: scale(1.15) translateY(-3px);
    }}

    .hotel-pin {{
      width: 36px;
      height: 44px;
    }}

    .marker-svg {{
      filter: drop-shadow(0 3px 4px rgba(0,0,0,0.35));
    }}

    .leaflet-popup-content-wrapper {{
      border-radius: 12px;
      box-shadow: var(--shadow-lg);
      padding: 2px;
    }}

    .leaflet-popup-content {{
      margin: 10px 12px;
      font-family: var(--font-main);
      min-width: 210px;
    }}

    .popup-badge {{
      font-size: 10px;
      font-weight: 800;
      color: white;
      padding: 2px 6px;
      border-radius: 4px;
      display: inline-block;
      margin-bottom: 3px;
    }}

    .popup-title {{
      font-size: 14px;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 2px;
    }}

    .popup-time {{
      font-size: 11px;
      color: #2563eb;
      font-weight: 700;
      margin-bottom: 4px;
    }}

    .popup-desc {{
      font-size: 11px;
      color: var(--text-secondary);
      line-height: 1.4;
      margin-bottom: 5px;
    }}

    .popup-link {{
      display: inline-block;
      font-size: 10.5px;
      color: #0284c7;
      font-weight: 800;
      text-decoration: none;
    }}

    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.5);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
      backdrop-filter: blur(4px);
    }}

    .modal-backdrop.open {{
      display: flex;
    }}

    .modal-window {{
      background: white;
      border-radius: 16px;
      width: 100%;
      max-width: 840px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-lg);
      overflow: hidden;
      animation: modalFadeIn 0.2s ease-out;
    }}

    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: translateY(12px) scale(0.98); }}
      to {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    .modal-header {{
      padding: 12px 18px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .modal-header h3 {{
      font-size: 15px;
      font-weight: 800;
    }}

    .modal-close {{
      border: none;
      background: none;
      font-size: 20px;
      cursor: pointer;
      color: var(--text-muted);
    }}

    .modal-body {{
      padding: 14px 18px;
      overflow-y: auto;
    }}

    .original-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
      text-align: left;
    }}

    .original-table th {{
      background: #f1f5f9;
      padding: 7px 10px;
      border: 1px solid #cbd5e1;
      font-weight: 700;
      color: #1e293b;
    }}

    .original-table td {{
      padding: 8px 10px;
      border: 1px solid #cbd5e1;
      vertical-align: top;
      line-height: 1.5;
    }}

    /* ★★★ 모바일 화면 분기 (< 900px) ★★★ */
    @media (max-width: 900px) {{
      header {{
        padding: 6px 10px;
        gap: 5px;
      }}
      .header-title-group h1 {{
        font-size: 14.5px;
      }}
      .header-title-group p {{
        display: none;
      }}
      .mobile-view-switcher {{
        display: flex;
      }}
      
      .main-layout {{
        height: calc(100vh - 128px);
      }}

      body.mobile-mode-list .sidebar {{
        display: flex;
        width: 100%;
        min-width: 100%;
        height: 100%;
        border-right: none;
      }}
      body.mobile-mode-list .map-container {{
        display: none !important;
      }}

      body.mobile-mode-map .sidebar {{
        display: none !important;
      }}
      body.mobile-mode-map .map-container {{
        display: block !important;
        width: 100%;
        height: 100%;
      }}
    }}

    /* 데스크톱에서는 하단 캐러셀 숨김 (좌측 사이드바가 있으므로) */
    @media (min-width: 901px) {{
      .bottom-carousel-container {{
        display: none;
      }}
    }}
  </style>
</head>
<body class="mobile-mode-list">

  <!-- 상단 헤더 -->
  <header>
    <div class="header-top-row">
      <div class="header-left">
        <div class="brand-badge">München</div>
        <div class="header-title-group">
          <h1>🇩🇪 뮌헨 여행 일정</h1>
          <p>4일간의 핵심 경로 및 알프스 렌트카 가이드</p>
        </div>
      </div>

      <!-- 액션 버튼 -->
      <div class="header-actions">
        <a class="action-btn primary" id="googleRouteHeaderBtn" href="https://www.google.com/maps/dir/%EB%AE%8C%ED%97%A8+%EB%8F%85%EC%9D%BC/%EB%A7%88%EB%A6%AC%EC%97%94+%EB%8B%A4%EB%A6%AC+%EB%8F%85%EC%9D%BC/%EB%85%B8%EC%9D%B4%EC%8A%88%EB%B0%94%EC%9D%B8%EC%8A%88%ED%83%80%EC%9D%B8+%EC%84%B1+%EB%8F%85%EC%9D%BC/%EC%B6%94%ED%81%AC%EC%8A%88%ED%94%BC%EC%B2%B4+%EC%82%B0+%EB%8F%85%EC%9D%BC/%EB%AE%8C%ED%97%A8+%EB%8F%85%EC%9D%BC" target="_blank" title="Google Maps 길찾기">
          🚗 2일차 Google 경로
        </a>
        <button class="action-btn" id="btnOriginalPdf" title="일정표 확인">
          📋 일정표
        </button>
      </div>
    </div>

    <!-- 모바일 뷰 전환 세그먼트 버튼 (모바일 전용) -->
    <div class="mobile-view-switcher">
      <button class="mobile-switch-btn active" data-view="list">📋 일정 목록</button>
      <button class="mobile-switch-btn" data-view="map">🗺️ 지도 전체 보기</button>
    </div>

    <!-- 일자별 필터 탭 (가로 스크롤) -->
    <div class="day-tabs" id="dayTabs">
      <button class="tab-btn active" data-day="all">
        <span class="tab-dot" style="background: #64748b;"></span>
        전체 4일
      </button>
      <button class="tab-btn" data-day="1">
        <span class="tab-dot" style="background: var(--color-day1);"></span>
        20일 (시내)
      </button>
      <button class="tab-btn" data-day="2">
        <span class="tab-dot" style="background: var(--color-day2);"></span>
        🚗 21일 (렌트카)
      </button>
      <button class="tab-btn" data-day="3">
        <span class="tab-dot" style="background: var(--color-day3);"></span>
        22일 (과학·궁전)
      </button>
      <button class="tab-btn" data-day="4">
        <span class="tab-dot" style="background: var(--color-day4);"></span>
        23일 (아레나)
      </button>
    </div>
  </header>

  <!-- 메인 뷰: 좌측 타임라인 + 우측 지도 -->
  <main class="main-layout">
    
    <!-- 좌측 타임라인 패널 -->
    <aside class="sidebar">
      <div class="sidebar-header" id="sidebarHeader">
        <div class="sidebar-title">
          <span id="dayTitleText">전체 4일 일정 개요</span>
          <span id="spotCountBadge" style="font-size:11px; color:var(--text-muted); font-weight:500;">총 26개 스팟</span>
        </div>
        <div class="transit-badge" id="transitTipText">
          💡 각 날짜 탭을 클릭하거나 좌측 카드를 누르면 지도가 해당 장소로 자동 이동합니다.
        </div>
      </div>

      <div class="timeline-container" id="timelineList">
        <!-- 🏨 고정 우리 숙소 배너 카드 -->
        <div class="hotel-banner-card" id="hotelBannerCard" title="클릭 시 지도가 숙소 위치로 이동합니다">
          <div class="hotel-banner-top">
            <span class="hotel-badge">🏨 우리 숙소 (Basecamp)</span>
            <a class="hotel-map-link" href="https://maps.app.goo.gl/LNwTawdtw64NZc248" target="_blank">Google 지도 ↗</a>
          </div>
          <div class="hotel-name">노보텔 뮌헨 시티 아르눌프파크</div>
          <div class="hotel-name-de">Novotel München City Arnulfpark</div>
          <div class="hotel-desc">Arnulfstraße 57 • S-Bahn 및 트램(16/17번) 인접 • 중앙역·시내·궁전 이동 편리</div>
          <div class="hotel-action-hint">👆 터치 시 지도가 숙소로 이동합니다</div>
        </div>
      </div>
    </aside>

    <!-- 우측 인터랙티브 지도 패널 -->
    <section class="map-container">
      <div id="map"></div>

      <!-- 지도 상단 우측 컨트롤 -->
      <div class="map-overlay-controls">
        <button class="map-ctrl-btn" id="btnFitBounds" title="현재 일정 전체 한눈에 보기">
          🔍 맞춤
        </button>
        <button class="map-ctrl-btn" id="btnToggleTile" title="지도 스타일 전환">
          🗺️ 스타일
        </button>
      </div>

      <!-- ★★★ 최소화 가능한 접이식 범례 (모바일 시야 방해 제로) ★★★ -->
      <div class="map-legend" id="mapLegend">
        <div class="legend-header" id="legendHeader" title="클릭하여 범례 열기/닫기">
          <div class="legend-title">📍 경로 & 숙소</div>
          <span class="legend-toggle-btn">접기/열기</span>
        </div>
        <div class="legend-body">
          <div class="legend-item" style="margin-bottom: 3px; padding-bottom: 3px; border-bottom: 1px dashed #e2e8f0;">
            <span style="font-size: 11.5px;">🏨</span>
            <span><strong>우리 숙소</strong>: 노보텔 아르눌프파크</span>
          </div>
          <div class="legend-item">
            <div class="legend-color" style="background: var(--color-day1);"></div>
            <span><strong>20일</strong> : BMW, 구시가지, 디너</span>
          </div>
          <div class="legend-item">
            <div class="legend-color" style="background: var(--color-day2);"></div>
            <span><strong>21일</strong> : 🚗 렌트카 (마리엔다리-성-추크슈피체)</span>
          </div>
          <div class="legend-item">
            <div class="legend-color" style="background: var(--color-day3);"></div>
            <span><strong>22일</strong> : 독일박물관, 피나코테크, 궁전</span>
          </div>
          <div class="legend-item">
            <div class="legend-color" style="background: var(--color-day4);"></div>
            <span><strong>23일</strong> : 알리안츠아레나, 영국정원, 슈바빙</span>
          </div>
        </div>
      </div>

      <!-- ★★★ 모바일 지도 하단 스팟 캐러셀 바텀 슬라이더 ★★★ -->
      <div class="bottom-carousel-container" id="bottomCarousel">
        <div class="carousel-top-bar">
          <span class="carousel-day-title" id="carouselDayTitle">코스 스팟 둘러보기</span>
          <div class="carousel-actions">
            <button class="carousel-toggle-btn" id="carouselToggleBtn">▼ 접기</button>
            <button class="carousel-nav-btn" id="carouselPrevBtn" title="이전">‹</button>
            <button class="carousel-nav-btn" id="carouselNextBtn" title="다음">›</button>
          </div>
        </div>
        <div class="carousel-track" id="carouselTrack">
          <!-- JS 동적 생성 -->
        </div>
      </div>

    </section>

  </main>

  <!-- 일정표 모달 -->
  <div class="modal-backdrop" id="originalModal">
    <div class="modal-window">
      <div class="modal-header">
        <h3>📋 뮌헨 & 바이에른 4일 일정표</h3>
        <button class="modal-close" id="modalCloseBtn">&times;</button>
      </div>
      <div class="modal-body">
        <table class="original-table">
          <thead>
            <tr>
              <th style="width: 14%;">일자</th>
              <th style="width: 28%;">오전</th>
              <th style="width: 34%;">오후</th>
              <th style="width: 24%;">저녁</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background: #fff1f2;">
              <td><strong>숙소<br><span style="color:#e11d48; font-weight:800;">[Base]</span></strong></td>
              <td colspan="3">
                🏨 <strong>노보텔 뮌헨 시티 아르눌프파크</strong> (Novotel München City Arnulfpark)<br>
                <span style="font-size: 11px; color: #475569;">주소: Arnulfstraße 57, 80636 München • 트램 16/17번 및 Donnersbergerbrücke S-Bahn 역 바로 앞</span>
              </td>
            </tr>
            <tr>
              <td><strong>20일</strong></td>
              <td>
                • BMW Welt (9시~10시)<br>
                • BMW 뮤지엄 (10시~11시)<br>
                • 올림피아 파크<br>
                • 학생 부부 기숙사
              </td>
              <td>
                • 호프브로이하우스 뮌헨 (점심)<br>
                • 마리엔 광장<br>
                • 빅투알리엔 마켓<br>
                • 뮌헨 프라우엔키르헤<br>
                • 막스마라<br>
                • <strong>신시청 인형극 (17시)</strong>
              </td>
              <td>
                • Schwarzreiter Tagesbar & Restaurant
              </td>
            </tr>
            <tr style="background: #f0fdf4;">
              <td><strong>21일<br><span style="color:#059669; font-weight:700;">[렌트카]</span></strong></td>
              <td>
                • <strong>뮌헨 출발</strong> (렌트카 드라이브)<br>
                • <strong>마리엔 다리</strong> (Marienbrücke)
              </td>
              <td>
                • <strong>노이슈바인슈타인 성</strong> 내부 관람<br>
                • 호엔슈방가우/알프제 점심<br>
                • <strong>추크슈피체 산 (2,962m)</strong> 케이블카
              </td>
              <td>
                • 아이브제 호수 산책 후<br>
                • <strong>뮌헨 복귀 드라이브</strong> (A95 고속도로)
              </td>
            </tr>
            <tr>
              <td><strong>22일</strong></td>
              <td>
                • 국립 독일 박물관
              </td>
              <td>
                • <strong>TU MENSA (점심, 2시 30분까지)</strong><br>
                • 알테 피나코테크<br>
                • 님펜부르크 궁전
              </td>
              <td style="color: #94a3b8;">(자유 일정 / 석양 및 비어가든)</td>
            </tr>
            <tr>
              <td><strong>23일</strong></td>
              <td>
                • 알리안츠 아레나 투어
              </td>
              <td>
                • 오데온광장 + 뮌헨 레지덴츠<br>
                • 영국정원<br>
                • 슈바빙(Schwabing) 지구
              </td>
              <td style="color: #94a3b8;">(자유 일정 / 슈바빙 다이닝 & 펍)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- Leaflet JS -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>

  <!-- 자바스크립트 -->
  <script>
{js_code}
  </script>
</body>
</html>
"""

# 파일 3곳에 모두 저장
paths = [
    '/Users/min/orca/workspaces/trip/여행/index.html',
    '/Users/min/orca/workspaces/trip/여행/munich_itinerary.html',
    '/Users/min/orca/workspaces/trip/여행/뮌헨_여행_일정_지도.html'
]

for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(full_html)

print("Generated all files with UX optimization (Collapsible legend & bottom carousel)!")
