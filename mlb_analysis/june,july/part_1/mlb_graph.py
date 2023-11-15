import pandas as pd
import datetime
from datetime import datetime as dt
import matplotlib.pyplot as plt

#2022
#df = pd.read_csv("data/mlb_2022_season_data.csv", index_col=0)
#date1 = dt(2022, 3, 30)
#date2 = dt(2022, 7, 10)

#2021
#df = pd.read_csv("data/mlb_2021_season_data.csv", index_col=0)
#date1 = dt(2021, 4, 1)
#date2 = dt(2021, 7, 10)

#2019
#df = pd.read_csv("data/mlb_2019_season_data.csv", index_col=0)
#date1 = dt(2019, 3, 28)
#date2 = dt(2019, 7, 10)

#2018
#df = pd.read_csv("data/mlb_2018_season_data.csv", index_col=0)
#date1 = dt(2018, 3, 29)
#date2 = dt(2018, 7, 10)

#2017
df = pd.read_csv("data/mlb_2017_season_data.csv", index_col=0)
date1 = dt(2017, 4, 2)
date2 = dt(2017, 7, 10)

df1 = pd.DataFrame()

# isolate win/loss data
while True:
    sDate = date1.strftime('%Y-%m-%d')
    df1[f'+/- ({sDate})'] = df[f'+/- ({sDate})']
    date1 = date1 + datetime.timedelta(days = 1)
    if (date1 == date2):
        break
df1.index.name = 'team'

#cummulative sum of dataframe
df2 = pd.DataFrame()
df2 = df1.cumsum(axis=1)


df3 = df2.T

df3.plot()
plt.show()