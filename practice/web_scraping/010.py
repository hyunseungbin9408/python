import requests
from bs4 import BeautifulSoup

## 구글 뉴스 검색(검색어: 아이유)
base_url = "https://news.google.com" ## 구글뉴스 웹페이지의 루트 디렉터리 URL을 base_url에 저장한다.
search_url = base_url + '/search?q=아이유&hl=ko&gl=KR&ceid=KR%3Ako' \
     ## 웹 브라우저 주소창에서 검색처 "아이유"에 대한 검색결과 페이지의 웹주소를 확인한다. 웹주소를 복사한다. base_url을 뒤에서 사용하기 위해 편의상 웹 주소에서 "/search?" 이하 부분을 구분하여 정리한다.
resp = requests.get(search_url)
html_src = resp.text ## 웹서버로부터 응답 받은 웹페이지 객체의 text 속성에서 HTML 소스코드를 추출한다. BeautifulSoup함수에 파서를 적용하여 HTML을 파싱하고 변수 soup에 저장한다.
soup = BeautifulSoup(html_src, "html.parser")

## 뉴스 아이템 블록을 선택
news_items = soup.select('div[class="xrnccd"]')
    ## 웹페이지에서 뉴스콘텐츠 요소를 검색하기 위해, soup 객체에 select()메소드를 적용한다. <div>태그중에서 class속성이 "xrnccd"인 태그를 모두 찾아서 리스트에 담는다. news_items 변수에 저장한다.
print(len(news_items))
print(news_items[0])
print("\n")

## 뉴스 아이템에서 "링크, 제목, 내용, 출처, 등록일시" 데이터 파싱
for item in news_items[:3]:  ## news_items에 들어있는 <div>태그를 하나씩 파싱하기 위해서 for 문을 이용했다. 출력량을 제한하기 위해 3개의 원소까지만 대상으로 적용한다.
    link = item.find('a', attrs={'class':'VDXfz'}).get('href') ## 개별 뉴스의 링크는 class 속성이 "VDXfz"인 <a> 태그에 들어있다. <a> 태그의 "href" 속성을 따로 추출하기 위해 get메소드를 이용한다.
    news_link = base_url + link[1:] \
        ## base_url과 결합하여 출력 내용을 확인한다. link 변수의 문자열은 "./articles/~~" 처럼 "."으로 시작하기 때문에 첫 번째 문자(".")를 제거하기 위해 link[1:] 형식으로 문자열의 두번째 문자부터 슬라이싱하여 선택한다.
    print(news_link)

    news_title = item.find('a', attrs={'class':'DY5T1d'}).getText() \
        ## 개별 뉴스의 제목은 <a> 태그중에서 class속성이 'DY5T1d' 인 경우에 들어있다 find()명령으로 찾은 <a>태그요소에 getText() 메소드를 적용하여 텍스트부분을 적용한다.
    print(news_title)

    news_content = item.find('span', attrs={'class':'xBbh9'}).text \
        ## 개별 뉴스의 요약내용은 <span> 태그 중에서 class 속성이 'xBbh9'인 경우에 들어있다. find()명령으로 찾은 <span>태그 요소의 text 메소스를 이용해서 텍스트부분을 출력한다.
    print(news_content)

    new_agency = item.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text \
        ## 개별 뉴스의 출처는 <a> 태그중에서 class속성이 'wEwyrc AVN2gc uQIVzc Sksgp'인 경우다. find() 명령으로 찾은 <태그>요소를 text메소스를 이용해서 텍스트부분을 출력한다.
    print(new_agency)

    news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'}) \
        ## 개별 뉴스를 등록한 time을 추출한다. <time> 태그중에서 class 속성이 'WW6dff uQIVzc Sksgp' 인 경우고 find()로 찾고 get()함수로 datetime 속성value를 확인한다. split()메소드로 문자열의 날짜와 time 부분을 나눈다.
    news_reporting_datetime = news_reporting.get('datetime').split('T')
    news_reporting_date = news_reporting_datetime[0]
    news_reporting_time = news_reporting_datetime[1][:-1]
    print(news_reporting_date, news_reporting_time)
    print("\n")

## 앞의 코드를 이용하여 구글 뉴스 클리핑 함수 정의
def google_news_clipping(url, limit=5): ## 앞 부분 코드를 이용하여 google_news_clipping 함수를 정의한다. 검색결과 페이지주소와 추출할 뉴스 콘텐츠의 개수를 매개변수로 입력받는다.


    resp = requests.get(url) 
    html_src = resp.text
    soup = BeautifulSoup(html_src, 'html.parser')

    news_items = soup.select('div[class="xrnccd"]')

    links=[]; titles=[]; contents=[]; agencies=[]; reporting_dates=[]; reporting_times=[]; \
        ## 뒷 라인에서 추출할 뉴스링크, 제목, 내용, 출처, 등록일, 등록time 정보를 담을비어있는 리스트 객체를 정의한다.

    for item in news_items[:limit]: ## for문을 정의하여 개별 뉴스 콘텐츠의 링크, 제목, 내용, 출처, 등록일, 등록time 정보를 추출하고, 49번 라인에서 정의한 리스트 객체에 append() 명령으로 추가한다.
        link = item.find('a', attrs={'class':'VDXfz'}).get('href')
        news_link = base_url + link[1:]
        links.append(news_link)

        news_title = item.find('a', attrs={'class':'DY5T1d'}).getText
        titles.append(news_title)

        news_content = item.find('span', attrs={'class':'xBbh9'}).text
        contents.append(news_content)
    
        news_agency = item.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
        agencies.append(news_agency)

        news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})
        news_reporting_datetime = news_reporting.get('datetime').split('T')
        news_reporting_date = news_reporting_datetime[0]
        news_reporting_time = news_reporting_datetime[1][:-1]
        reporting_dates.append(news_reporting_date)
        reporting_times.append(news_reporting_time)

        result = {'link':links, 'title':titles, 'contents':contents, 'agency':agencies, \
            ## 뉴스 링크, 제목, 내용, 출처, 등록일, 등록시간 정보를 담은 리스트를 value로 가지는 딕셔너리를 정의하고, result 변수에 저장한다.
                 'date':reporting_dates, 'time':reporting_times}
        return result ## 이 함수는 result 변수에 저장되는 딕셔너리 객체를 리턴한다.

news = google_news_clipping(search_url, 2) ## 5~6번에서 정리한 search_url 변수의 value를 google_news_clipping로 전달하고 그 결과를 출력한다. limit 매개변수를 정의하여 최대 2개까지만 출력되도록한다.
print(news)