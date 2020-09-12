import requests ## requests 모듈을 불러온다.

urls = ["https://www.daum.net/", "https://www.python.org/"] ## 2개의 URL를 리스트에 담고, 변수 urls에 넣는다.
filename = "robots.txt" ## 로본 배제 표준을 담고있는 파일명을 filename 변수에 넣는다.

for url in urls: ## 변수 urls에 들어있는 URL들을 대상으로 for 반복문을 정의한다.
    file_path = url + filename ## robots.txt 파일의 이름을 웹 사이트의 루트 URI와 결합하고, 결합한 파일 경로를 file_path에 저장한다.
    print(file_path)
    resp = requests.get(file_path) ## 웹 서버에 GET 요청을 보내고 웹 서버가 응답한 내용을 변수 resp에 저장한다.
    print(resp.text) ## 웹 서버 응답 객체 text 속성은 HTML소스를 저장하고 있다. print() 함수로 출력하면 사이트의 로봇 배제 표준의 내용을 볼 수 있다.
    print("\n")