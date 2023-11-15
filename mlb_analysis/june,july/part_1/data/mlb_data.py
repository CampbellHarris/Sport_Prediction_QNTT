import pandas as pd
import numpy as np
import selenium 
from selenium.webdriver.chrome import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import datetime
from datetime import datetime as dt
import re


current = dt(2017, 4, 2)

end = dt(2017, 7, 11)


teams = ['WSH', 'TEX', 'BOS', 'OAK', 'CHC', 'NYY', 'KC', 'CLE', 'TOR', 'DET', 'TB', 'ATL', 'MIA', 'PHI', 'SEA', 'HOU', 'BAL', 'MIN', 'STL', 'CWS', 'MIL', 'CIN', 'SF', 'COL', 'PIT', 'AZ', 'SD', 'NYM', 'NL', 'AL', 'LAA', 'LAD']

df = pd.DataFrame(index = teams)

driver = webdriver.Chrome()
date = current.strftime("%Y-%m-%d")
link = "https://www.mlb.com/schedule/{}".format(date)
driver.get(link)

# loop through pages
while (current < end):



    # navigate to page of current date

    



    # get strings on page

    soup = BeautifulSoup(driver.page_source, "html.parser")
    texts = []
    rows = soup.find('div', {'data-mlb-test': 'individualGamesContainer'}).find_all('a')
    for x in rows:
        texts.append(x.get_text())
    



    # filter strings

    stats = []
    all_team_names_with_space = ['WSH ', 'TEX ', 'BOS ', 'OAK ', 'CHC ', 'NYY ', 'KC ', 'CLE ', 'TOR ', 'DET ', 'TB ', 'ATL ', 'MIA ', 'PHI ', 'SEA ', 'HOU ', 'BAL ', 'MIN ', 'STL ', 'CWS ', 'MIL ', 'CIN ', 'SF ', 'COL ', 'PIT ', 'AZ ', 'SD ', 'NYM ', 'LAA ', 'LAD ']
    print(len(all_team_names_with_space))
    for x in texts:
        for y in all_team_names_with_space:
            if (x.startswith(y)):
                stats.append(x)
    print(len(stats))
    print(stats)



    # split data

    tW = []
    sW = []
    tL = []
    sL = []
    for x in stats:
        z = re.sub(",", "", x)
        y = z.split()
        tW.append(y[0])
        sW.append(int(y[1]))
        tL.append(y[2])
        sL.append(int(y[3]))



    # initialize dataframe 

    data = pd.DataFrame( 
        {
            f"opponent ({date})": None,
            f"points scored ({date})": 0,
            f"+/- ({date})": 0
        }, index = teams)


    for x, y, z, s in zip(tW, sW, tL, sL):
        data.loc[x] = [z, y, +1]

    for x, y, z, s in zip(tW, sW, tL, sL):
        data.loc[z] = [x, y, -1]


    # add to right of dataframe
    df = pd.concat([df, data], axis=1, join='inner')

    # navigate to next page
    current = current + datetime.timedelta(days = 1)
    date = current.strftime("%Y-%m-%d")
    link = "https://www.mlb.com/schedule/{}".format(date)
    print(link)
    driver.get(link)

driver.quit()

df.to_csv("mlb_2017_season_data.csv")

print(df)