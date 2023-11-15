import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
from datetime import datetime as dt
import re
import json

def PredictionModel1(df):
    account = 0
    for rslt, tm1, tm2, wo1, wo2 in zip(df['result'], df['team1Name'], df['team2Name'], df['winningOdds_team1'], df['winningOdds_team2']):
        wns1, wns2 = GetWinTally(tm1, tm2)
        if wns1 > wns2:
            predict = tm1
        else:
            predict = tm2
        if (predict == rslt) & (tm1 == rslt):
            account += wo1
        elif (predict == rslt) & (tm2 == rslt):
            account += wo2
        UpdateWinTally(rslt)
    print("break even amount: 2156")
    print("(Model 1) final account: ${}".format(account))


def UpdateWinTally(rslt):
    with open("winDict.json", "r") as jsonFile:
        winDict = json.load(jsonFile)
    winDict[rslt] += 1
    with open("winDict.json", "w") as jsonFile:
        json.dump(winDict, jsonFile)

# read first then write
def GetWinTally(tm1, tm2):
    with open("winDict.json", "r") as openfile:
        winDict = json.load(openfile)
    wns1 = winDict[tm1]
    wns2 = winDict[tm2]
    return wns1, wns2

def InitializeWinTally():
    teams = {
        "Chicago White Sox": 0,
        "Cleveland Guardians": 0,
        "Detroit Tigers": 0,
        "Kansas City Royals": 0,
        "Minnesota Twins": 0,
        "Baltimore Orioles": 0,
        "Boston Red Sox": 0,
        "New York Yankees": 0,
        "Tampa Bay Rays": 0,
        "Toronto Blue Jays": 0,
        "Houston Astros": 0,
        "Los Angeles Angels": 0,
        "Oakland Athletics": 0,
        "Seattle Mariners": 0,
        "Texas Rangers": 0,
        "Chicago Cubs": 0,
        "Cincinnati Reds": 0,
        "Milwaukee Brewers": 0,
        "Pittsburgh Pirates": 0,
        "St.Louis Cardinals": 0,
        "Atlanta Braves": 0,
        "Miami Marlins": 0,
        "New York Mets": 0,
        "Philadelphia Phillies": 0,
        "Washington Nationals": 0,
        "Arizona Diamondbacks": 0,
        "Colorado Rockies": 0,
        "Los Angeles Dodgers": 0,
        "San Diego Padres": 0,
        "San Francisco Giants": 0
    }

    # Serializing json
    json_object = json.dumps(teams, indent=4)

    with open("winDict.json", "w") as outfile:
        outfile.write(json_object)


def PredictionModel2(df):
    # account is a list to track the changes
    account = [500,]
    # x is a number representing the current amount in the list
    x = 500
    for rslt, tm1, tm2, wo1, wo2 in zip(df['result'], df['team1Name'], df['team2Name'], df['winningOdds_team1'], df['winningOdds_team2']): 
        x -= 2 * 20
        if rslt == tm1:
            x += (wo1 * 20)
        else:
            x += (wo2 * 20)
        account.append(x)
    print(f'(Model 2) will turn $500 into {x}')
    AccountPlot(account)

def AccountPlot(account):
    plt.plot(account)
    plt.ylabel('account balance')
    plt.xlabel('games')
    plt.show()



if __name__ == "__main__":
    InitializeWinTally()
    df = pd.read_csv('allData.csv')
    data = df
    #InitializeWinTally()
    #PredictionModel1(df)

    InitializeWinTally()
    PredictionModel2(df)

