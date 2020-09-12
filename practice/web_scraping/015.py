from selenium import webdriver
from bs4 import BeautifulSoup
import time

## 통계지표 검색어를 입력하여, CSV 파일로 저장하기
def download_bok_statistic_by_keyword():
    ## 100대 통계지표 중에서 키워드 검색을 통해 상세정보를 가져오는 작업을 처리할 함수를 정의한다.

    item_found = 0 ## 키워드 검색여부를 나타내기 위해 변수(item_found) value를 0으로 초기화한다. 이후 코드 실행 과정에서 키워드를 찾으면 1(true)변경한다.
    while not item_found: 
        ## item_found value가 0이면, 계속 while 반복문을 수행한다. 즉 키워드에 해당하는 아이템을 찾을때까지 계속 반복문을 수행한다.

        ## 검색어 초기화
        keyword = "" ## 검색어 keyword를 초기화한다.
        while len(keyword) == 0: ## keyword의 문자열의 길이가 0이면, 14번 라인을 계속 반복 처리한다. 즉, 검색 키워드를 키보드 입력방식으로 입력받는다.
            Keyword = str(input("검색할 항목을 입력하세요")) ## input함수로 키워드를 입력받아서 변수 keyword에 저장한다.

        ## 웹 드라이버 실행
        driver = webdriver.Chrome("/usr/bin/chromedriver") ## 크롬 웹드라이버를 실행하고 한국은행 경제통계시스템 웹 페이지를 불러온다.
        driver.implicitly_wait(3)
        driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")
        time.sleep(5)

        item1 = driver.find_elements_by_css_selector('a[class="ng-binding"]') ## 100대 통계지표 항목을 나타내는 요소들을 CSS속성을 이용하여 선택한다.
        item2 = driver.find_elements_by_css_selector('a[class="a-c1-list ng-binding"]') ## 요소들을 크롬 개발자 도구로 선택해서 분류하면, 총 3가지 유형의 CSS 속성을 가지고있다.
        item3 = driver.find_elements_by_css_selector('a[class="a-c4-list ng-binging"]')
        driver.implicitly_wait(3) 

        items = items1[1:] + items2 + items3 ## 3가지 유형의 속성을 가지는 요소들을 하나의 리스트로 통합한다. items1 의 첫번째 원소는 웹 페이지 왼쪽위에 있는 버튼을 나타내기 때문에 items1[1:]처럼 제외한다.

        for idx, item in enumerate(items): ## items 리스트에 들어 있는 HTML 요소를 하나씩 꺼내어 처리한다.

            if keyword in item.text: ## item 객체의 text value에 keyword 문자열이 포함되어 있으면 참이므로 다음 문장을 수행한다. 참이 아니라면, 36번 라인의 elif문과 40번 라인의 else 문을 순차적으로 처리한다.
                print("검색어 '%s'에 매칭되는 '%s' 통계지표를 검색 중..." % (keyword, item.text))
                    ## keyword value에 해당하는 item을 찾은 것이므로, click() 메소드를 이용하여 item 요소를 마우스로 클릭하는 동작을 수행한다.
                item.click()
                item_found = 1 ## item_found value를 1(True)로 변경하고, break 문을 이용하여 while 문밖으로 벗어난다. 따라서, 44번 라인으로 이동하여 프로그램을 처리한다.
                time.sleep(5)
                break
            elif idx == (len(items) - 1): ## items에 들어있는 마지막 item가지 keyword value가 포함되는 item을 찾지 못한경우. close() 메소드를 이용하여 크롬 웹드라이브를 종료한다.
                print("검색어 '%s'에 대한 통계지표가 존재하지 않습니다..." % keyword)
                driver.close()
                continue ## continue 명령어로 다시 처음 while 문으로 return
            else:
                pass


    ## 검색결과 로딩 HTML 웹페이지를 파싱 - 통계지표 테이블(표) 양식 정리
    html_src = driver.page_source ## 구글 웹드라이버가 꺼지지않고 33번 라인의 if문을 통과한경우 while문을 빠져나와서 해당 페이지 소스를 html_src로 저장한다.
    soup = BeautifulSoup(html_src, "html.parser") ## BeautifulSoup 객체를 생성해서 변수 soup로 넣고 구글 웹 드라이버를 종료시킨다.
    driver.close()

    table_items = soup.find_all('td', {'class':'ng-binding'}) ## soup 변수에 class 에서 맞는 속성 value를 모두 찾아서 table_item으로 넣는다.
    date = [t.text for i, t in enumerate(table_items) if i % 3 == 0]  ## table_items value를 date,value,change 순서대로 넣는다.
    value = [t.text for i, t in enumerate(table_items) if i % 3 == 1]
    change = [t.text for i, t in enumerate(table_items) if i % 3 == 2]

    ## CSV 파일로 저장
    result_file = open('./data/bok_statistics_%s.csv' % ketword, 'w') ## 결과 value들을 CSV 파일로 저장한다.

    for  i in range(len(date)):
        result_file.write("%s, %s, %s" % (date[i], value[i], change[i]))
        result_file.write('\n')

    result_file.close()
    print("키워드 '%s'에 대한 통계지표를 저장하였습니다." % keyword)

    return date, value, change ## 리턴 value를 value를 날짜, 통계value, 변화율로 나누어서 리턴한다.

## 함수 실행 - 'CD수익률' 통계지표를 별도로 검색, CSV 파일로 저장
result = download_bok_statistic_by_keyword() 
print(result)