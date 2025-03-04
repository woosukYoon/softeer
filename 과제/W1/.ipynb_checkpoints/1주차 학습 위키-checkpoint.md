## M1

#### 팀 활동 요구사항

Q1. 이런 데이터셋을 분석해서 얻을 수 있는 경제적 가치는 무엇일까요? 어떤 비즈니스 상황에서 이런 데이터셋을 분석해서 어떤 경제적 가치를 얻을 수 있을까요?

1. 우선, 상관관계 분석은 인과관계 분석에 비해 원인과 결과를 파악하기는 어렵지만, 분석과 실험 설계 난이도가 낮고 변수들 간의 관계 파악은 가능하기에, 인과관계 분석에 비해 시간과 비용 측면에서의 절약이 있을 것이다.

2. 데이터 분석의 결과를 토대로 비즈니스 문제를 정의하고 이와 연관된 요인을 파악하여, 개선이 이루어질 수 있는 조치를 취함으로써 비즈니스적 경제적 가치를 이룰 수 있을 것이다.

3. 자동차를 잘 모르는 고객들에게 부품과 스펙을 설명할 때, 연비나 고성능 등에 영향을 줄 수 있는 요인과의 상관관계를 보여주면서 적시적으로 설명할 수 있도록 하여 고객의 제품 접근성에 영향을 줄 수 있을 것이다.

4. 고객의 타겟층을 설정하고 제품을 설계할 때, 고객의 요구사항과 생산 비용에 관련한 요인들을 파악하여 부품을 조정하는 방식으로 경제적 가치를 만들 수 있을 것이다.

5. 품질 관리시, 기초 통계량과 산점도 등을 이용해서 모니터링을 하고, 품질 수준에 맞는 관리가 이루어지는지 확인할 수 있다. 또한, 품질에 영향을 주고 있는 요인을 파악하여 이를 조치함으로써 경제적 가치를 만들 수 있을 것이다.

Q2. 변수들 간의 상관 관계가 높은 조합을 임의로 2개 선택해서 해당 데이터 간의 상관 관계를 그래프로 그리고 어떤 결론을 내릴 수 있는지를 토의하세요.

    import numpy as np

    #추세선 생성
    coefficents = np.polyfit(df['carb'], df['hp'], 1)
    linear_fit = np.poly1d(coefficents)
    trend_line = linear_fit(df['carb'])

    plt.scatter(df['carb'], df['hp'], color = 'green')
    plt.plot(df['carb'], trend_line, color = 'blue')
    plt.title("carb vs Horse Power")
    plt.xlabel("carb")
    plt.ylabel("Horse Power")

carb는 카뷰레터의 수를 나타내고 horse power은 마력을 나타낸다.<br>
이 둘은 상관계수가 약 0.7498로 높은 양의 상관계수를 가지고 있다. 이와 추세선을 통해서 카뷰레터 수의 증가가 차량의 성능 향상과 관련이 있음을 알 수 있다.<br>
실제로 카뷰레터는 연료와 공기를 혼합하는 역할을 하며, 이 수가 많아짐으로써 연료 공급이 원활하여 성능이 향상될 수 있다고 한다.

#### 추가 진행 사항

자동차에 대한 사전 지식이 부족하여 기본 변수들을 중점으로 구글링 해보았다.</br>
공부하며 느낀 점은 자동차는 설계 목적에 따라 크게 효율성(연비)과 고성능(마력)으로 나뉘어진다고 생각했다.</br>
따라서 타겟 고객의 요구사항을 정확히 정의해야지만, 제품 설계 과정에서부터 목적에 따라 부품 수 조절, 구동 방식 선택 등을 결정할 수 있을 것이고, 무엇보다도 설계 전체가 경제적 측면에서도 수익성이 나올 수 있을지 판단할 수 있을 것이다.</br>

앞선 데이터의 변수들을 정리한 결과는 다음과 같다.</br>
cyl : 엔진의 실린더 개수. 실린더가 많을수록 출력이 높아지기에 고성능 차량에서 실린더 개수가 많음. 하지만 연료 소비가 증가하기에 연비가 좋지 않아질 수 있음.</br>
disp : 엔진의 배기량(실린더에서 이동하는 공기와 연료 혼합물의 총 부피). 부피가 클수록 엔진 출력이 높아질 수 있지만, 연료 소비량도 증가할 수 있음.</br>
drat : 리어 액슬의 기어 비율. 엔진의 회전수가 바퀴 회전에 비례하는 비율. 높은 값일수록 속도 성능이 좋을 수 있지만 연료 효율은 낮을 수 있음.</br>
wt : 차량의 무게. 무게가 낮을수록 연비가 높아짐.</br>
qsec : 차량이 0.25마일을 주행하는 데 걸리는 시간. 값이 낮을수록 고성능.</br>
vs : 엔진의 구조. V형 엔진은 고출력 차량. 직렬형 엔진은 연료 효율성에 좋은 경향이 있음.</br>
am : 차량의 변속기 유형. 수동 변속기는 일반적으로 고성능 및 연비 효율이 좋음. 자동 변속기는 운전이 편리함이 제공되는 장점이 있음.</br>
gear : 전진 기어의 개수. 전진 기어 개수의 증가는 효율적인 동력 전달로 인해 고성능이며, 엔진 회전수도 최적화하기 쉬워 연비에서도 좋은 경향이 있음.</br>
carb : 카뷰레터의 개수. 카뷰레터가 많을수록 연료 공급이 원활해져 성능이 향상될 수 있음.

이를 일반적인 개념을 통해서 mpg(연비)와 hp(마력) 관점으로 상관관계를 가지는 변수는 다음과 같다.</br>
mpg : cyl, disp, drat, wt, vs, gear, am</br>
hp : cyl, disp, drat, qsec, vs, am, gear, carb</br>

추가적으로 마력과 연비가 다른 변수들과의 상관 관계를 시각화해보았다.</br>

    #'hp'와 다른 열들의 scatter plot 생성
    columns = [col for col in df_features.columns if col not in ('hp','mpg')]

    plt.figure(figsize=(10, 8))
    for i, col in enumerate(columns, start=1):
        plt.subplot(3, 3, i)
        plt.scatter(df_features[col], df_features['hp'], color='skyblue', alpha=0.7)
        # 추세선 생성
        coefficents = np.polyfit(df_features[col], df_features['hp'], 1)
        linear_fit = np.poly1d(coefficents)
        trend_line = linear_fit(df_features[col])
        plt.plot(df_features[col], trend_line, color = 'black')
        plt.title(f"hp vs {col}")
        plt.xlabel('hp')
        plt.ylabel(col)

    plt.suptitle("Horse power vs Other Variables", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

    #'mpg'와 다른 열들의 scatter plot 생성
    columns = [col for col in df_features.columns if col not in ('hp','mpg')]

</br>

    plt.figure(figsize=(10, 8))
    for i, col in enumerate(columns, start=1):

        plt.subplot(3, 3, i)
        plt.scatter(df_features[col], df_features['mpg'], color='green', alpha=0.7)
        # 추세선 생성
        coefficents = np.polyfit(df_features[col], df_features['mpg'], 1)
        linear_fit = np.poly1d(coefficents)
        trend_line = linear_fit(df_features[col])
        plt.plot(df_features[col], trend_line, color = 'black')
        plt.title(f"mpg vs {col}")
        plt.xlabel('mpg')
        plt.ylabel(col)

    plt.suptitle("Miles Per Gallon vs Other Variables", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

hp와 gear와의 산점도와 같이 일반적인 개념과는 다른 부호의 상관관계나 약한 상관 관계가 나타나는 경우가 존재한다.</br>
예상한 결과와 다른 이유에는 데이터 개수 부족이나 일반적인 상식을 깨는 기술의 발전 등이 있을 것이다.</br>
하지만 이 분석에서 더 큰 한계점으로서 생각되는 것은 데이터의 수가 32개로 매우 적기 때문에 일반화하기에는 어렵다는 것이다.</br>
또한 상관 분석의 한계점처럼 인과 관계가 직관적으로 보이지 않는다. 예를 들어 qsec은 마력이 높은 자동차일수록 적은 시간이 소요될 것이지만, 그래프를 확인해보면 그 인과 관계를 파악하기 어렵다.

#### 새롭게 알 된 내용

size를 사용해서 각 열의 결측치를 포함한 데이터의 수를 알 수 있다.

데이터 프레임의 stack을 이용해서 행과 열의 인덱스 값을 묶어 튜플로 사용할 수 있다.

suptitle을 통해 다수의 그래프를 통합하는 제목을 지정할 수 있다.

자동차 설계 방향에는 연비 중심과 성능 중심이 있다.

다양한 자동차 변수들을 알게 되었다.

## M2

#### 팀 활동 요구사항

팀원들과 토의한 결과, EXISTS, CASE, HAVING keyword의 사용 빈도가 높지 않아, 공통적으로 생소했던 키워드였다. 위 키워드를 이해하고 적용해보기 위해, 팀원 1명씩 각 키워드와 관련한 문제를 만들고 이를 푸는 시간을 가졌다.

###### CASE 예제 </br>
Q1. 이름에 따라 고객 그룹을 설정하여라. 고객 그룹 설정 규칙은 다음과 같다.</br>
● Group 1 : A ~ I로 시작하는 이름을 가지고 있는 고객.</br>
● Group 2 : J ~ O로 시작하는 이름을 가지고 있는 고객.</br>
● Group 3 : P ~ T로 시작하는 이름을 가지고 있는 고객.</br>
● Group 4 : U ~ Z로 시작하는 이름을 가지고 있는 고객.</br>
이후, 각 그룹에 고객들의 수를 구하여 이를 출력하라.

    pd.read_sql(
        """SELECT COUNT(CUSTOMERNAME) AS [GROUP MEMBER COUNT], CASE 
        WHEN CUSTOMERNAME BETWEEN 'A' AND 'J' THEN 'GROUP 1'
        WHEN CUSTOMERNAME BETWEEN 'J' AND 'P' THEN 'GROUP 2'
        WHEN CUSTOMERNAME BETWEEN 'P' AND 'U' THEN 'GROUP 3'
        ELSE 'GROUP 4' END AS CUSTOMERGROUP
        FROM CUSTOMERS
        GROUP BY CUSTOMERGROUP""" ,conn)

###### GROUP BY, HAVING 예제</br>
Q. Orders 테이블과 Employees 테이블 이용하여, 주문을 10개 이상 받은 Employee 중에서 LastName이 D나 C로 시작하는 사원들 LastName 정보 출력하라.

    pd.read_sql(
        """SELECT E.LASTNAME, O.*
        FROM (SELECT COUNT(ORDERID) AS [AMOUNT OF ORDERS], EMPLOYEEID 
        FROM ORDERS GROUP BY EMPLOYEEID HAVING COUNT(ORDERID) >= 10) O
        LEFT JOIN EMPLOYEES E
        ON E.EMPLOYEEID = O.EMPLOYEEID
        WHERE E.LASTNAME LIKE 'C%' OR E.LASTNAME LIKE 'D%'
        ORDER BY LASTNAME""",conn)

###### EXIST 예제</br>
Q. Employees와 Orders Table을 사용하여, 1997년 1월 1일 이전에 발생한 주문을 담당하는 Employee의 LastName을 출력하라.(DISTINCT 사용하기)

    pd.read_sql(
        """SELECT DISTINCT(LASTNAME) FROM EMPLOYEES E
        WHERE EXISTS (SELECT * FROM ORDERS O
        WHERE E.EMPLOYEEID = O.EMPLOYEEID AND ORDERDATE < '1997-01-01')""", conn)

#### 새롭게 알게 된 내용

DDL은 일반적으로 자동 commit이 수행된다.

Sql 언어에 따라 상위 몇 개의 레코드를 추출하는 방식이 다르다.

COUNT 집계 함수 안에 DISTINCT를 넣는다면 열의 값을 중복없이 셀 수 있다.

Sql은 테이블명과 컬럼명에서도 대소문자를 구분하지 않는다.

조건에서 평균보다 큰 값을 갖는 조건을 갖게 하려면 평균을 select 구문의 avg를 통해서 select와 From이 있는 상태로 추출해야한다.

LIKE문에서 한글자를 표현하는 경우에는 _를 사용해야한다.

완전히 똑같은 텍스트를 찾는 경우에는 조건절에 like ‘text’로 표현해야한다.

Sqlite3에서는 like 구문 뒤에 오는 [ ]를 단순히 문자열로 판단하지만, 다른 데이터베이스에서는 [ ]안에 있는 문자가 모두 해당된다는 조건으로 쓰일 수 있다. 예를 들어 [bsp]는 b,s,p가 해당 자리에 나오는 문자열을 찾는 것이고, [a-f]의 경우에는 a,b,c,d,e,f가 해당 자리에 있는 문자열을 찾는 것이다.

열 이름에 띄어쓰기를 넣으려면 [ ]나 “ “에 열 이름을 넣어야한다.

having은 필터링에만 사용되지 집계 함수에 영향을 미칠 수 없다. 그렇기에 where을 이용해서 미리 필요한 데이터만 추출한 후 집계 함수를 사용해야될 때가 존재한다.

case를 통해 조건문을 작성할 수 있고, when, then, else, end를 구조에 맞게 사용해야한다.

## M3

#### 기본 개념
ETL은 데이터 처리와 통합을 위한 데이터 파이프라인 아키텍처. 데이터 웨어하우스나 데이터 레이크와 같은 중앙 저장소에 데이터를 통합하고 분석하기 위해 사용됨.

데이터 웨어하우스
데이터를 구조화된 형식으로 저장. 분석 및 비즈니스 인텔리전스를 위한 사전 처리된 데이터의 중앙 리포지토리.

데이터 마트
회사의 금융, 마케팅 또는 영업 부서와 같은 특정 사업부의 요구 사항을 지원하는 데이터 웨어하우스

데이터 레이크
원시 데이터 및 비정형 데이터의 중앙 리포지토리. 먼저 데이터를 저장하고 나중에 처리.

계층적으로 데이터 웨어 하우스 밑에 데이터 마트를 놓으면서 특정 분야에 특화된 데이터 저장소를 가지게 할 수 있다.

요새 데이터 저장소의 성능이 증가함에 따라 변환을 먼지 진행하지 않고, 저장을 진행하는 ELT 프로세스로 변환되고 있고, 비정형 데이터를 저장하는 저장소가 데이터 레이크이다.
ELT 프로세스는 빅데이터와 클라우드 환경 효율적이며, 다양한 데이터 형식과 유스 케이스를 처리하기에 적합하다.
ELT는 데이터 웨어하우스 내부에서 Transform이 진행된다고 생각하면 된다. 

#### 실습 후 새로 알게 된 점

웹 스크랩핑 과정시 Extract 단계에서 테이블 추출할 때, raw data는 테이블의 구조와 내용을 변경하지 않는 것을 의미하며, 저장 방식을 변경하는 것은 raw data 정의에 위배되는 것은 아니다.

ELT 과정에서도 데이터 웨어하우스를 설계하는 사람들이 직접적으로 룰을 정의해주어야 변환이 이루어질 수 있다. 

BeautifulSoup4는 html과 xml을 스크래핑할 때, 좋은 패키지이며, json을 스크래핑할 때는 json 패키지를 사용해야 한다.

로그를 찍는 과정을 진행하였는데, 로그를 찍는 방법은 logging 모듈과 print 방식이 있다.

txt 파일을 열고, 추가적인 내용을 넣기 위해서는 ‘a’(append) 모드를 사용해야 한다.


#### 팀 활동 요구사항

Q1. wikipeida 페이지가 아닌, IMF 홈페이지에서 직접 데이터를 가져오는 방법은 없을까요? 어떻게 하면 될까요?

IMF 홈페이지를 살펴본 결과, IMF에서 제공하는 api인 'https://www.imf.org/external/datamapper/api/v1/NGDPD'에 접근하여 테이블을 가져와야 한다.</br>
또한, 이 api는 html이 아닌 json 구조의 데이터를 제공하기에 beautilfulsoup4 패키지보다는 json 패키지를 이용해서 웹 스크래핑을 시도해야 한다.</br>
실습한 결과, html 방식에 비해 계층적 구조에서의 평탄화 작업이 필요하며 from_dict를 통해 딕셔너리를 데이터프레임으로 변경해주어야 한다.

    import requests
    import json

    file = requests.get('https://www.imf.org/external/datamapper/api/v1/NGDPD', stream=True)
    data = file.json()

    #데이터 평탄화 과정
    ngdpd_data = data["values"]["NGDPD"]
    df_hompage_gdp = pd.DataFrame.from_dict(ngdpd_data, orient="index")

    #JSON 파일로 저장
    df_hompage_gdp.to_json("IMF_homepage_gdp.json", indent=4)

    pd.read_json("IMF_homepage_gdp.json")

Q2. 만약 데이터가 갱신되면 과거의 데이터는 어떻게 되어야 할까요? 과거의 데이터를 조회하는 게 필요하다면 ETL 프로세스를 어떻게 변경해야 할까요?

과거 데이터가 추후에 필요한 상황이라면 갱신되기 전 과거 데이터가 저장되어 있어야한다. 과거 데이터를 저장하는 방법으로 생각한 방법은 다음과 같다.
1. Extract 과정을 진행할 때마다, raw data를 다른 파일명으로 저장한다.
2. 갱신 주기를 알고 있는 상황이라면, 로그를 확인하여 Extract 과정에서 그 주기를 초과했을 때, 새로운 파일을 저장한다.
3. 갱신이 수시로 진행된다면, 바로 이전에 추출한 raw data와 현재 추출한 raw data를 비교하여 변경점이 있는 경우에만 다른 파일로 저장한다.
4. 데이터를 데이터 베이스에 Load하며 갱신하는 과정에서 변경점이 존재할 때, 이력 테이블을 생성할 수 있도록 하는 과정을 추가한다.

방법 1은 저장 공간 측면에서는 손해이지만, 데이터 갱신 주기가 짧고 데이터 추출을 많이 하지 않을 때 유리한 방법일 것이다.</br>
방법 2는 갱신 주기가 지켜지지 않았을 때 잘못된 데이터를 추출할 수 있는 가능성은 있지만, 저장 공간 측면에서 유리한 방법일 것이다.</br>
방법 3은 raw data의 크기가 클 때 두 데이터를 비교하는 시간이 오래걸릴 수 있지만, 저장 공간 측면에서도 유리하고 과거 데이터 갱신을 무조건적으로 찾을 수 있는 방법일 것이다.</br>
방법 4는 적재하는 과정에서 과거 데이터를 관리하는 방법인데, 방법 1~3에서의 추출 조건과 결합하여 이력 테이블을 생성하는 조건으로써 활용될 수 있을 것이다.</br>

Q3. raw 데이터의 양이 압도적으로 많다면?

1. 코드적으로는 requests.get() 함수에서 매개변수 stream의 값을 True로 설정한다. stream 값이 False라면 응답 데이터 전체를 메모리에 올려놓고, True라면 데이터를 부분적인 청크로 읽어드리면서 대용량 데이터를 불러오는데 유리할 수 있다.
2. 하둡을 이용해서 데이터를 분산 처리하고, 이를 디스크에 데이터를 복제하는 과정을 갖추면서 대용량 데이터를 다루고, ETL 과정에서의 안정성을 확보한다.
3. 스크래핑한 테이블 데이터를 판다스를 이용하지 않고, 기본 파이썬 도구를 통해서 json으로 변환시킨다.
4. 판다스는 메모리 내에서 데이터를 처리하기에, 데이터가 머신 메모리보다 크다면 Out of Memory 오류 메시지로 인해 데이터 처리가 가능하지 않다. 그렇기에 인메모리 방식인 아파치 스파크를 사용한다면 판다스보다 대규모의 데이터를 처리를 할 수 있을 것이다.

(추가) Extract와 Transpose의 단계를 세분화하여 오류에 대비하도록 한다.

Q4. raw 데이터를 Transform 하는데 시간이 아주 오래 걸린다면?

1. 코드적으로는 pool 라이브러리를 활용해서 병렬 처리를 시도한다. 개인 pc 프로세서를 효율적으로 이용할 수 있도록 하여, Transform 과정을 빠르게 할 수 있도록 한다. 실험을 진행해본 결과는 M3에서 사용했던 GDP 데이터에서는 병렬 처리를 한 것이 시간이 더 많이 소요 되었다. 원인으로는 실험 진행한 데이터의 레코드 수가 209개로 적기 때문이라고 판단하였다.

#다중 코어로 병렬 처리 시도

    def parallel_dataframe(df, func, num_cores = 8):
        df_split = np.array_split(df, num_cores)
        pool = Pool(num_cores)
        df = pd.concat(pool.map(func, df_split))
        pool.close()
        pool.join()
        return df

2. 분산 처리를 할 수 있는 환경을 만든다. 우선, 분산 처리 환경에서 스파크와 하둡을 사용할 수 있도록 자체 분산 컴퓨터 노드를 구성하거나, 클라우드 컴퓨터 노드를 구성하여 효율성을 증대할 수 있을 것이다.
3. Transform 과정에서는 하둡보다는 스파크를 이용하는 것이 디스크의 접근을 줄여 I/O 명령을 줄일 수 있기에 대용량의 데이터를 빠르게 처리할 수 있을 것이다.
4. ELT 프로세스로 전환을 생각하여, 데이터 웨어하우스나 데이터 레이크를 통해서 병렬적으로 데이터를 처리하도록 하여 효율을 높인다.

Q5. 한가지 더, 고민해 볼 것은 Extract한 데이터를 바로 처리 (Transform)하지 않고 저장하는 이유가 뭘까? 어떤 경우에 그렇게 해야 할까?

팀원들과 토의해본 결과 여러 이유가 있을 것이라고 생각했는데, 생각한 이유는 다음과 같다.
1. 데이터베이스의 저장 규칙이 제대로 정해지지 않았을 때
2. 데이터의 사용 목적이 불분명할 때
3. 데이터 품질 검증이 필요할 때
4. 다양한 데이터 소스에서 데이터를 추출할 때 이를 병합하기 위해서는 저장하여 스테이징 단계에서 병합해야 하기 때문에
5. 데이터 Transform 과정에서 오류가 발생할 때, 데이터 추출 단계부터 다시 시작하지 않도록 하기 위한 안전 장치
6. 과거 데이터가 필요할 때 



