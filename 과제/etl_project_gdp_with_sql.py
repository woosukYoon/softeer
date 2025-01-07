def log(describe) :
    import datetime as datetime
    log_txt = open('etl_project_log.txt','a')
    print(datetime.datetime.now(), describe, '\n', file = log_txt)
    log_txt.close()

def extract_gdp():
    import requests
    import datetime as datetime
    from bs4 import BeautifulSoup
    import pandas as pd

    log("Extract start")

    html = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29").text
    soup = BeautifulSoup(html, 'html.parser')
    gdp = soup.find("table", {"class": 'wikitable'}).find('tbody').find_all('tr')[3:]
    gdp_imf = [[gdp_row.find_all('td')[i].text.strip() for i in range(2)] for gdp_row in gdp]

    df_gdp = pd.DataFrame(gdp_imf)
    df_gdp.to_json('raw_data_gdp.json')

    log("Extract finish")

    return 'raw_data_gdp.json'

def transform_gdp(json):

    import datetime as datetime
    import pandas as pd
    import pycountry_convert as pc
    
    log("Transform start")
    
    df_gdp = pd.read_json(json)
    df_gdp.columns = ['country', 'GDP_USD_billion']
    df_gdp['GDP_USD_billion'] = df_gdp['GDP_USD_billion'].apply(lambda x : int(x.replace(",","")) if x != '—' else None)
    df_gdp['GDP_USD_billion'] = round(df_gdp['GDP_USD_billion']/1000, 2)
    df_gdp = df_gdp.sort_values('GDP_USD_billion', ascending = False)

    def country_to_continent(x) :
        try : continent = pc.country_alpha2_to_continent_code(pc.country_name_to_country_alpha2(x))
        except :
            exception_region_dict = {'DR Congo' : 'AF', 'Kosovo' : 'EU', 'Sint Maarten' : 'EU', 'Zanzibar' : 'AF', 'East Timor' : 'AS'}
            continent = exception_region_dict[x]
        return continent

    df_gdp['continent'] = df_gdp['country'].apply(lambda x : country_to_continent(x))

    log("Transform finish")

    return df_gdp

def load_gdp(df_gdp) :

    import datetime as datetime
    import pandas as pd
    import pycountry_convert as pc
    import sqlite3
    
    log("Load start")

    conn = sqlite3.connect('World_Economies.db')
    df_gdp.to_sql('Countries_by_GDP', conn, index = False, if_exists='replace')

    cur = conn.cursor()

    def exceed_100B() :
        conn = sqlite3.connect('World_Economies.db')
        cur = conn.cursor()
        df = pd.read_sql("SELECT * FROM Countries_by_GDP WHERE GDP_USD_billion > 100", conn)
        return df

    print(exceed_100B())

    def region_top5_average() :
        conn = sqlite3.connect('World_Economies.db')
        cur = conn.cursor()
        df = pd.read_sql(
            """SELECT AVG(GDP_USD_billion) [TOP5 AVERAGE], CONTINENT
            FROM (SELECT * FROM 
            (SELECT *, ROW_NUMBER() OVER (PARTITION BY CONTINENT ORDER BY GDP_USD_billion DESC) AS RANK 
            FROM Countries_by_GDP) 
            WHERE RANK <=5)
            GROUP BY CONTINENT
            ORDER BY [TOP5 AVERAGE] DESC
            """, conn)
        return df

    print(region_top5_average())

    log("Load finish")

def ETL_gdp() :
    json = extract_gdp()
    df_gdp = transform_gdp(json)
    load_gdp(df_gdp)