import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 섹션 URL (정치 뉴스 예시)
url = "https://news.naver.com/section/100"

# 1. User-Agent 및 추가 헤더 설정 (⭐추가 정보 포함⭐)
headers = {
    # 기존 User-Agent는 유지
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    
    # 💡 추가: 브라우저가 어떤 종류의 응답을 원하는지 명시
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    
    # 💡 추가: 브라우저 언어 설정 (한국어로 설정)
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    
    # 💡 연결을 끊지 않고 계속 유지하겠다는 의미
    'Connection': 'keep-alive'
}

# 2. 웹페이지 요청
response = requests.get(url, headers=headers) # 강화된 헤더를 사용하여 요청
response.raise_for_status() 
html = response.text

# 3. HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 4. 뉴스 제목 가져오기 (클래스 이름은 그대로 사용)
titles = soup.find_all("a", class_="sa_item_title")

# 5. 결과 출력
print("📰 네이버 뉴스 섹션 (정치) 제목과 링크 10개")
print("---------------------------------------------")
if not titles:
    # 제목이 추출되지 않았을 경우 사용자에게 알림
    print("⚠️ 경고: 제목을 추출하지 못했습니다. .")
else:
    for i, title_tag in enumerate(titles[:10], 1):
        title_text = title_tag.get_text().strip()
        link_url = title_tag.get('href')
        
        print(f"[{i}] {title_text}")
        print(f"    ➡️ 링크: {link_url}")
print("---------------------------------------------")