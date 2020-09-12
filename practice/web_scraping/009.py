import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/IU_(singer)" \
    ## 웹페이지 문서의 HTML 소스코드를 추출, 파싱하여 BeautifulSoup 객체를 생성하고 변수 soup로 저장한다.
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, "html.parser")

links = soup.select('i') ## select로 조건에 맞는 태그를 모두 찾아서 변수 links에 리스트형태로 넣는다.
print(len(links))
print("\n")

external_links = soup.select('a[class="external text"]') ## <i> 태그중에서 class 속성을 가지고 그 value가 "external text"인 태그들을 찾아 리스트로 리턴한다.
print(external_links[:3]) ## 최대 3개까지만 출력한다.
print("\n")

id_selector = soup.select('#siteNotice') \
    ## CSS의 id 선택자를 활용하는 방법이다.CSS 스타일 시트에서 id는 고유한 value를 가지기 때문에 select() 메소드에 id 선택지를 사용하면 오직 한 개의 태그만을 찾는다. id 선택자는 "#속성value"로 표현한다.
print(id_selector)
print("\n")

id_selector2 = soup.select('div#siteNotice') \
    ## CSS의 id 선택자를 사용 할때, 특정 태그안에서만 id 선택자를 찾는 방법이다. 'div#siteNotice'는 div태그 중에서 id 속성value이 "siteNotice"인 div태그를 뜻한다.
print(id_selector2)
print("\n")

id_selector3 = soup.select('p#siteNotice') \
    ## 'p#siteNotice'는 p 태그 중에서 id 속성value가 "sitevalue"인 p 태그를 말한다. 현재 웹 문서에서 id 속성value가 "siteNotice"인 태그는 앞서 확인한 div가 유일하기 때문에 빈리스트가 출력된다.
print(id_selector3)
print("\n")

class_selector = soup.select('.mw-headline') \
     ## CSS의 클래스 선택자를 활용하는 방법이고 CSS 스타일시트에서 서로 다른 요소에 동일한 스타일을 지정할 때 클래스 선택자를 사용한다.
print(class_selector)
print("\n")

class_selector2 = soup.select('span.mw-headline')
print(class_selector2)