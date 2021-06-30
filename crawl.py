import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

url = "http://sejong.korea.ac.kr/campuslife/facilities/dining/weeklymenu"

def get_bob_image():
    res = requests.get(url, verify=False)
    soup = bs(res.text, 'html.parser')

    for a in soup.select('a'):
        if a.text == "교직원식당 주간 메뉴":
            link = "https://sejong.korea.ac.kr/" + a['href']
            return link

def get_bob_period():
    res = requests.get(url, verify=False)
    soup = bs(res.text, 'html.parser')

    for st in soup.select('strong'):
        if st.text[:11] == "교직원식당 주간 메뉴":
            front, end = st.text \
                .replace("교직원식당 주간 메뉴", "") \
                .replace("안내", "") \
                .replace("(", "") \
                .replace(")", "") \
                .replace(" ", "") \
                .split('~')

            
            front = datetime.strptime(front, "%m월 %d일")
            end = datetime.strptime(end, "%m월 %d일")
            
            year = datetime.today().year
            front = front.replace(year=year)
            end = end.replace(year=year)
            return front, end