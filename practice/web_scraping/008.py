import requests 
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/IU_(singer)" \
    ## 웹페이지 문서의 HTML 소스코드를 추출, 파싱하여 BeautifulSoup 객체를 생성하고 변수 soup로 저장한다.
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, "html.parser")

iu_image = soup.select('') \
     ## 크롬개발자 도구에서 복사한 CSS선택자를 selec() 메소드에 전달한다. select() 메소드가 리턴하는 객체 변수 iu_image에 저장한다.
print(iu_image) ## select() 메소드가 리턴하는 객체는 파이썬 리스트이다. iu_image 변수를 출력하면 원소 1개 value만을 가진다.
print("\n")
print(iu_image[0]) ## select() 메소드가 리턴한 파이썬 리스트에 iu_image 변수에 원소가 1개 이기때문에 출력value가 동일하다.0