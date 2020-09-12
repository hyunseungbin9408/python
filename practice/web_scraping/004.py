import requests
from bs4 import BeautifulSoup ## bs4 라이브러리에서 BeautifulSoup 클래스를 불러온다.

url = "https://en.wikipedia.org/wiki/Kernel" ## 위키피디아 홈페이지 주소 URL를 변수 url에 할당한다.
resp = requests.get(url) ## 웹서버에 GET 요청을 보내고, 웹서버가 응답한 객체를 변수 resp에 저장한다.
html_src = resp.text ## 응답 객체의 text속성에서 HTML 소스코드를 추출하여 변수 html_src에 할당한다.

soup = BeautifulSoup(html_src, 'html.parser') ## BeautifulSoup 함수는 매개변수로 전달받은 HTML 소스코드를 해석하여 BeautifulSoup 객체를 생선한다. HTML을 파싱하는 적적한 구문해석기(.paser)를 함께 입력해야한다.
print(type(soup)) ## 변수 soup이 저장하고 있는 BeautifulSoup 객체의 자료형을 출력한다. bs4 라이브러리에서 불러온 BeautifulSoup 클래스라는 것을 확인 할 수 있다.
print("\n")

print(soup.head) ## HTML 웹 문서의 "head" 태그에 해당하는 내용이 출력된다.
print("\n")
print(soup.body) ## HTML 웹 문서의 "body" 태그에 해당하는 내용이 출력된다.
print("\n")

print('title 태그요소:', soup.title) ## HTML 웹 문서의 "title" 태그에 해당하는 내용이 출력된다. 웹 브라우저 탭에 표시되는 부분이다.
print('title 태그 이름: ',  soup.title.name) ## name 속성을 지정하여 HTML 태그의 이름을 따로 추출한다.
print('title 태그 문자열: ',  soup.title.string) ## string 속성을 지정하여 HTML 태그를 제외하고 태그 안에 표시되는 문자열만 따로 추출한다.