import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway" ## 웹페이지 문서의 html 소스코드를 추출하고 파싱하여 BeautifulSoup 객체를 생성한다.
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, "html.parser")

target_img = soup.find(name='img', attrs={'alt':'Seoul-Metro-2004-20070722.jpg'}) ## 이 객체에 find() 메소드를 적용하여 지하철 차량 사진을 나타내는 <img> 태그 부분을 찾아 변수 target_img에 저장
print('HTML 요소:', target_img)
print("\n")

target_img_src = target_img.get('src') ## <img> 태그 정보를 가지고 있는 target_img 변수에 get('속성이름') 메소드를 적용하면 속성이 가지는 속성 value를 추출 할 수 있다.
print('이미지 파일 경로:', target_img_src)
print("\n")

target_img_resp = requests.get('http:' + target_img_src) ## 앞에서 추출한 이미지 파일 경로에 'http:'를 보완하고, requests 모듈의 get() 함수를 적용한다. 이미지 파일 경로에 GET요청을 보낸다. 그리고 이미지 파일을 담은 응답 객체를 target_img_resp 변수에 저장한다.
out_file_path = "./output/download_image.jpg" ## 이미지 파일을 저장할 PC의 폴더 경로와 파일 이름을 out_file_path 변수에 지정한다.

with open(out_file_path, 'wb') as out_file: ## target_img_resp 변수에 저장된 requests 응답객체의 content 속성에는 이미지 파일이 바이너리 형태로 저장되어있다.
    out_file.write(target_img_resp.content) ## write() 명령으로 저장 위치를 지정하여 외부 파일로 저장 할 수 있다.
    print("이미지 파일로 저장하였습니다.")