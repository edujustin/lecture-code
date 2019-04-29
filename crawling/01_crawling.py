from bs4 import BeautifulSoup as bs
import requests

#1. requests야 네이버 실시간 검색 정보좀 가져와줘! 그리고 그거 글로 좀 바꿔줘!

url = 'https://www.naver.com'
response = requests.get(url).text
# print(type(response))

#2. Beautifulsoup 객체에서 response라고 하는 변수안에 담긴 객체를 파싱하고, 그 결과를 
# 다시 Beautifulsoup 객체로 반환한다.
soup = bs(response, 'html.parser')
# print(type(soup))

#3. Beautifulsoup 객체에 담긴 변수에서 CSS selector를 활용해 특정 정보를 가져온다. 
keywords = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div span[class*=ah_k]')

for index, keyword in enumerate(keywords):
    print(index, keyword.text)