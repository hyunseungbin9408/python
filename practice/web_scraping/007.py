import requests, re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway" ## 웹페이지 문서의 HTML 소스코드를 추출, 파싱하여 BeautifulSoup 객체를 생성하고 변수 soup에 저장한다.
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src,"html.parser")

links = soup.find_all("a") ## soup 객체에 a에 해당하는 모든태그를 links로 넣는다.
print("하이퍼링크의 개수", len(links)) ## links변수에 총 원소 개수를 출력한다.
print("\n")
print("첫 3개의 원소", links[:3]) ## 처음부터 3번째까지의 원소를 출력한다.
print("\n")

wiki_links = soup.find_all(name="a", href=re.compile("/wiki/"),limit=3) ## a 태그에 href 속성이 지정된 문자열을 따로지정하면 해당 문자열이 포함된 태그만 찾아서 최대 3개까지만 변수에 넣는다.
print("/wiki/ 문자열이 포함된 하이퍼링크:", wiki_links) ## wiki 가 포함된 a 태그 3개를 출력한다.
print("\n")

external_links = soup.find_all(name="a", attrs={"class":"external text"},limit=3) ## find_all 메소드의 attrs 매개변수{속성이름:속성value}의 딕셔너리 형태로 찾으려는 태그의 value를 지정할 수 있다.
print("class 속성으로 추출한 하이퍼링크:", external_links)