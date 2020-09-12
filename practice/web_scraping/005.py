import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway" ## 응답 객체의 text 속성에서 HTML 소스코드를 추출하여 변수 html_src에 할당한다.
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, "html.parser") ## HTML 소스코드를 파싱하여 BeautifulSoup 객체를 생성하고 변수 soup에 할당한다.

first_img = soup.find(name='img') ## BeautifulSoup 클래스의 find() 메소드에 찾고자 하는 태그 이름('img')을 name 매개변수에 지정한다. 가장 처음으로 나타나느 <img> 태그 부분을 찾아서 출력한다.
print(first_img)
print("\n")

target_img = soup.find(name='img', attrs={'alt':'Seoul-Metro-2004-20070722.jpg'}) ## find() 메소드의 attrs 매개변수에 {'속성 이름': '속성 value'}의 딕셔너리 구조로 태그가 갖는 고유의 속성value를 지정한다.
print(target_img) ## 지정한 속성 value를 갖는 태그 중에서 가장 처음 나오는 태그를 찾는다.