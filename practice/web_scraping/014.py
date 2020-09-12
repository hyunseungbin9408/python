from selenium import webdriver
import time

## 100대 통계지표 엑셀 다운로드
def download_bok_statistics(): ## 100대 통계지표를 엑셀 파일로 다운로드하는 함수를 정의한다.

    driver = webdriver.Chrome("/usr/bin/chromedriver") ## 크롬 웹드라이버를 실행하고 한국은행 경제통계시스템 웹 페이지를 불러온다.
    driver.implicitly_wait(3)
    driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")


    excel_download = driver.find_element_by_css_selector('img[alt="download"]') \
        ## 크롬 웹 브라우저를 새로운 윈도우 창에 별도로 실행하고, 개발자 도구를 실행한다. 파일 다운로드 버튼의 CSS 속성을 확인한다.
        ## alt 속성value이 'download'인 <img>이므로, find_element_by_css_selector메소드를 이용하여 찾는다. 변수 excel_download에 저장한다.

    driver.implicitly_wait(5) ## excel_download 객체에 click() 메소드를 적용하면 크롬 웹드라이버 실행 창에서 다운로드 버튼을 클릭하는 동작을 처리한다.

    excel_download.click()
    time.sleep(5)

    driver.close() ## 크롬 웹 드라이버를 종료한다.
    print("파일 다운로드 실행...")

    return None ## 이 함수는 리턴 value을 가지지않는것으로 설정한다.

# gkatntlfgod
download_bok_statistics() ## 함수를 실행하여 다운로드 받는다.