import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup

# global headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    # 맑음, 어제보다 1˚ 낮아요
    cast = soup.find("p",attrs={"class":"cast_txt"}).get_text()
    # 현재 -3℃  (최저 -13˚ 최고 -2˚)
    curr_temp = soup.find("p",attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp = soup.find("span",attrs={"class":"min"}).get_text()
    max_temp = soup.find("span",attrs={"class":"max"}).get_text()
    # 오전 강수확률 0% 오후 강수확률 0%
    morning_rain_rate = soup.find("span",attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span",attrs={"class":"point_time afternoon"}).get_text().strip()

    # 미세먼지 정보
    # 미세먼지 32㎍/㎥보통
    # 초미세먼지 17㎍/㎥보통
    dust = soup.find("dl",attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text() #미세먼지
    pm25 = dust.find_all("dd")[1].get_text() #초미세먼지


    # 출력
    print(cast)
    print("현재 {} (최저 {} 최고 {})".format(curr_temp,min_temp,max_temp))
    print("오전 {} 오후 {}".format(morning_rain_rate,afternoon_rain_rate))
    print("미세먼지 {}".format(pm10))
    print("미세먼지 {}".format(pm25))
    print()

    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

def creat_soup(url,headers):
    res = requests.get(url,headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index+1,title))
    print("  (링크) : {}".format(link))

def scrape_news():
    print("[헤드라인 뉴스]")
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    url = "https://news.naver.com"
    soup = creat_soup(url,headers)
    news_list = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li", limit = 3)
    for idx, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(idx, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
    soup = creat_soup(url,headers)
    news_list = soup.find("div",attrs={"id":"main_content"}).find_all("div",attrs={"class":"cluster_group _cluster_content"},limit = 3)
    for idx, news in enumerate(news_list):
        title = news.find("li",attrs={"class":"cluster_item"}).find("a",attrs={"class":"cluster_text_headline nclicks(cls_sci.clsart)"}).get_text().strip()
        link = news.find("li",attrs={"class":"cluster_item"}).find("div",attrs={"class":"cluster_text"}).find("a")["href"]
        # title = news.find("a").get_text().strip()
        # link = news.find("a")["href"]
        print_news(idx, title, link)
    print()

if __name__ == "__main__":
    scrape_weather() # 오늘 날씨 정보 정보가져오기
    scrape_news()
    scrape_it_news()
