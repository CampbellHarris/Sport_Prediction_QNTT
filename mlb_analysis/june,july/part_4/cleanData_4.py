import pandas as pd
import numpy as np
import time
import datetime
from datetime import datetime as dt
import re
import json


def CleanData(df):

    result = []

    for tm1, tm2, sc1, sc2 in zip(df['team1Name'], df['team2Name'], df['team1Score'], df['team2Score']):
        if (sc1 > sc2):
            result.append(tm1)
        else:
            result.append(tm2)
            
    df['result'] = result

    ten1 = []
    ten2 = []
    xb1 = [] 
    xb2 = []
    bah1 = []
    bah2 = []
    b3651 = []
    b3652 = []
    bw1 = []
    bw2 = []
    cb1 = []
    cb2 = []
    gg1 = []
    gg2 = []
    iwe1 = []
    iwe2 = []
    lb1 = []
    lb2 = []
    mb1 = []
    mb2 = []
    pnn1 = []
    pnn2 = []
    wh1 = []
    wh2 = []
    ub1 = []
    ub2 = []
    vo1 = []
    vo2 = []
    vb1 = []
    vb2 = []




    for ten, xb, bah, b365, bw, cb, gg, iwe, lb, mb, pnn, wh, ub, vo, vb in zip(df['10x10bet'], df['1xBet'], df['bet-at-home'], df['bet365'], df['bwin'], df['Curebet'], df['GGBET'], df['Interwetten'], df['Lasbet'], df['Marathonbet'], df['Pinnacle'], df['William Hill'], df['Unibet'], df['VOBET'], df['Vulkan Bet']):
        try:
            x, y = ten
            ten1.append(x)
            ten2.append(y)
        except:
            ten1.append(0.00)
            ten2.append(0.00)
        try:
            x, y = xb
            xb1.append(x)
            xb2.append(y)
        except:
            xb1.append(0.00)
            xb2.append(0.00)
        try:
            x, y = bah
            bah1.append(x)
            bah2.append(y)
        except:
            bah1.append(0.00)
            bah2.append(0.00)
        try:
            x, y = b365
            b3651.append(x)
            b3652.append(y)
        except:
            b3651.append(0.00)
            b3652.append(0.00)
        try:
            x, y = bw
            bw1.append(x)
            bw2.append(y)
        except:
            bw1.append(0.00)
            bw2.append(0.00)
        try:
            x, y = cb
            cb1.append(x)
            cb2.append(y)
        except:
            cb1.append(0.00)
            cb2.append(0.00)
        try:
            x, y = gg
            gg1.append(x)
            gg2.append(y)
        except:
            gg1.append(0.00)
            gg2.append(0.00)
        try:
            x, y = iwe
            iwe1.append(x)
            iwe2.append(y)
        except:
            iwe1.append(0.00)
            iwe2.append(0.00)
        try:
            x, y = lb
            lb1.append(x)
            lb2.append(y)
        except:
            lb1.append(0.00)
            lb2.append(0.00)
        try:
            x, y = mb
            mb1.append(x)
            mb2.append(y)
        except:
            mb1.append(0.00)
            mb2.append(0.00)
        try:
            x, y = pnn
            pnn1.append(x)
            pnn2.append(y)
        except:
            pnn1.append(0.00)
            pnn2.append(0.00)
        try:
            x, y = wh
            wh1.append(x)
            wh2.append(y)
        except:
            wh1.append(0.00)
            wh2.append(0.00)
        try:
            x, y = ub
            ub1.append(x)
            ub2.append(y)
        except:
            ub1.append(0.00)
            ub2.append(0.00)
        try:
            x, y = vo
            vo1.append(x)
            vo2.append(y)
        except:
            vo1.append(0.00)
            vo2.append(0.00)
        try:
            x, y = vb
            vb1.append(x)
            vb2.append(y)
        except:
            vb1.append(0.00)
            vb2.append(0.00)

    df['ten1'] = ten1
    df['ten2'] = ten2
    df['xB1'] = xb1
    df['xB2'] = xb2
    df['bah1'] = bah1
    df['bah2'] = bah2
    df['b365-1'] = b3651
    df['b365-2'] = b3652
    df['bw1'] = bw1
    df['bw2'] = bw2
    df['Cb1'] = cb1
    df['Cb2'] = cb2
    df['GG1'] = gg1
    df['GG2'] = gg2
    df['Iwe1'] = iwe1
    df['Iwe2'] = iwe2
    df['Lb1'] = lb1
    df['Lb2'] = lb2
    df['Mb1'] = mb1
    df['Mb2'] = mb2
    df['Pnn1'] = pnn1
    df['Pnn2'] = pnn2
    df['VO1'] = vo1
    df['VO2'] = vo2
    df['VB1'] = vb1
    df['VB2'] = vb2
    return df

def FocusOnBestOdds(df):
    ddf = pd.DataFrame()
    ddf['team1Name'] = df['team1Name']
    ddf['team1Score'] = df['team1Score']
    ddf['team2Name'] = df['team2Name']
    ddf['team2Score'] = df['team2Score']
    ddf['result'] = df['result']
    
    winOd1 = []
    winOd2 = []

    for TEN1, TEN2, XB1, XB2, BAH1, BAH2, B3651, B3652, BW1, BW2, CB1, CB2, GG1, GG2, IWE1, IWE2, LB1, LB2, MB1, MB2, PNN1, PNN2, VO1, VO2, VB1, VB2 in zip(df['ten1'], df['ten2'], df['xB1'], df['xB2'], df['bah1'], df['bah2'], df['b365-1'], df['b365-2'], df['bw1'], df['bw2'], df['Cb1'], df['Cb2'], df['GG1'], df['GG2'], df['Iwe1'], df['Iwe2'], df['Lb1'], df['Lb2'], df['Mb1'], df['Mb2'], df['Pnn1'], df['Pnn2'], df['VO1'], df['VO2'], df['VB1'], df['VB2']):
        winOd1.append(max(float(TEN1), float(XB1), float(BAH1), float(B3651), float(BW1), float(CB1), float(GG1), float(IWE1), float(LB1), float(MB1), float(PNN1), float(VO1), float(VB1)))
        winOd2.append(max(float(TEN2), float(XB2), float(BAH2), float(B3652), float(BW2), float(CB2), float(GG2), float(IWE2), float(LB2), float(MB2), float(PNN2), float(VO2), float(VB2)))

    ddf['winningOdds_team1'] = winOd1
    ddf['winningOdds_team2'] = winOd2

    return ddf

if __name__ == "__main__":
    df = pd.read_json("allData.json")
    df = df.T
    df = CleanData(df)
    df = FocusOnBestOdds(df)
    df.to_csv("allData.csv")