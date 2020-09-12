import requests
from bs4 import BeautifulSoup
import urllib

## 구글 뉴스 검색어를 URL 코드 형식으로 인코딩
keyword_input = '아이유'
keyword = urllib.parse.quote(keyword_input) \
    ## urllib.parse 모듈의 quote()메소드를 이용하면, 문자열을 URL주소 형식에 맞도록 인코딩 할 수 있다. '아이유'이라는 한글 문자열을  URL주소형식으로 변환한 value를 변수 keyword에 저장한다.
print('아이유 문자열을 URL코드로 변환', keyword)

base_url = "https://news.google.com/" ## 먼저 구글 뉴스 웹페이지의 루트 디렉토리를 base_url에 저장한다.
search_url = "/search?q=" + keyword + "&hl=ko&gl=KR&ceid=KR%3Ako" ## 위에서 정의한 keyword변수를 '/search?q="와 조합하여 변수에 저장한다.
print('검색어와 조합한 URL:', search_url)

## 구글 뉴스 클리핑 함수 정의
def google_news_clipping_keyword(keyword_input, limit=5): ## 위에서 정의한 한글검색어 URL로 변환하는 코드를 사용하여, 구글 뉴스검색어를 입력받아 그결과를 리턴하는 함수를 정의한다.

    keyword = urllib.parse.quote(keyword_input) ## 함수의 매개변수로 입력되는 문자열을 URL 주소형식에 맞도록 변환한다.

    url = base_url + "/search?q=" + keyword + "&hl=ko&gl=KR&ceid=KR%3Ako" ## 검색결과 페이지의 URL을 조합하여 완성한다.

    resp = requests.get(url)
    html_src = resp.text
    soup = BeautifulSoup(html_src, "html.parser")

    news_items = soup.select('div[class="xrnccd"]')

    links=[]; titles=[]; contents=[]; agencies=[]; reporting_dates=[]; reporting_times=[];

    for item in news_items[:limit]:
        link = item.find('a', attrs={'class':'VDXfz'}).get('href')
        news_link = base_url + link[1:]
        links.append(news_link)

        news_title = item.find('a', attrs={'class':'DY5T1d'}).getText()
        titles.append(news_title)
다
        news_content = item.find('span', attrs={'class':'xBbh9'}).text
        contents.append(news_content)

        news_agency = item.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'})
        agencies.append(news_agency)

        news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})
        news_reporting_datetime = news_reporting.get('datetime').split('T')
        news_reporting_date = news_reporting_datetime[0]
        news_reporting_time = news_reporting_datetime[1][:-1]
        reporting_dates.append(news_reporting_date)
        reporting_times.append(news_reporting_time)

    result = {'link':links, 'title':titles, 'contents':contents, 'agency':agencies,\
        'date':reporting_dates, 'time':reporting_times}

    return result

## 함수를 실행하여 뉴스목록 정리
search_word = input("검색어를 입력하세요: ") ## input() 함수를 이용하여 검색어를 키보드로 입력받는다.
news = google_news_clipping_keyword(search_word, 2) ## 키보드로 입력받는 검색어와 검색하려는 뉴스의 최대 개수를 2개로 설정한다.
print(news['link'])
print(news['agency'])