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

    log("Transform start")
    
    df_gdp = pd.read_json(json)
    df_gdp.columns = ['country', 'gdp']
    df_gdp['gdp'] = df_gdp['gdp'].apply(lambda x : int(x.replace(",","")) if x != '—' else None)
    df_gdp['gdp'] = round(df_gdp['gdp']/1000, 2)
    df_gdp = df_gdp.sort_values('gdp', ascending = False)

    log("Transform finish")

    return df_gdp

def load_gdp(df_gdp) :

    import datetime as datetime
    import pandas as pd
    import pycountry_convert as pc
    
    log("Load start")
    
    df_100B = df_gdp[df_gdp['gdp'] >= 100]
    print(df_100B)

    def country_to_continent(x) :
        try : continent = pc.country_alpha2_to_continent_code(pc.country_name_to_country_alpha2(x))
        except :
            exception_region_dict = {'DR Congo' : 'AF', 'Kosovo' : 'EU', 'Sint Maarten' : 'EU', 'Zanzibar' : 'AF', 'East Timor' : 'AS'}
            continent = exception_region_dict[x]
        return continent

    df_gdp['continent'] = df_gdp['country'].apply(lambda x : country_to_continent(x))
    df_region_top5 = df_gdp.groupby('continent').head(5).groupby('continent').mean('gdp').sort_values('gdp', ascending = False)
    print(df_region_top5)
    
    log("Load finish")

def ETL_gdp() :
    json = extract_gdp()
    df_gdp = transform_gdp(json)
    load_gdp(df_gdp)