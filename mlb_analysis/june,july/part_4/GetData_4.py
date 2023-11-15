import selenium 
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import datetime
from datetime import datetime as dt
import re
import json


def GetPageData(page):
    #initialize webdriver
    browser = webdriver.Chrome()
    link = "https://www.oddsportal.com/baseball/usa/mlb-2022/results/#/page/{}".format(page)
    browser.get(link)

    # load full page by scrolling down
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

    # get a list of all game codes
    gameCodes = list()
    ids = browser.find_elements(By.XPATH, '//*[@id]')
    for id in ids:
        if (id.get_attribute('class') == "eventRow flex w-full flex-col text-xs"):
            gameCodes.append(id.get_attribute('id'))

    # get a list of all game urls
    gamePages = list()
    for game in gameCodes:
        gamePages.append(browser.find_element(By.XPATH, f'//*[@id="{game}"]/div/div/div[1]/div[2]/div/div/a[1]').get_attribute('href'))

    browser.quit()
    gamNum = 0
    # for each URL
    for gPage in gamePages:
        gamNum += 1
        IndividualGameData(gPage, gamNum, page)

    browser.quit()

def IndividualGameData(gPage, gamNum, page):
    check = True
    # initialize webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get(gPage)

    # find game stats
    try:
        team1Name = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/main/div[2]/div[3]/div[1]/div[1]/div/div[1]/p').text
        team1Score = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/main/div[2]/div[3]/div[1]/div[1]/div/div[2]/div').text
        team2Name = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/main/div[2]/div[3]/div[1]/div[3]/div[1]/p').text
        team2Score = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/main/div[2]/div[3]/div[1]/div[3]/div[2]/div').text
    # find all table rows
    except:
        print(f'data not found, page: {page}, game: {gamNum}')
        check = False

    if(check == True):
            
        x = 2

        booky = list()
        odds1 = list()
        odds2 = list()
        
        while x < 14:
            try:
                book = driver.find_element(By.CSS_SELECTOR, f'#app > div > div.w-full.min-h-screen.flex-center.bg-gray-med_light > div > main > div.relative.w-full.flex-grow-1.min-w-\[320px\].bg-white-main > div.min-md\:px-\[10px\] > div.relative.flex.flex-col > div > div:nth-child({x}) > div.flex.items-center.justify-start.w-full.max-ms\:justify-center.max-sm\:flex-wrap.max-sm\:gap-1.border-\[\#E0E0E0\] > a:nth-child(2) > p')
                booky.append(book.text)
                odd1 = driver.find_element(By.CSS_SELECTOR, f'#app > div > div.w-full.min-h-screen.flex-center.bg-gray-med_light > div > main > div.relative.w-full.flex-grow-1.min-w-\[320px\].bg-white-main > div.min-md\:px-\[10px\] > div.relative.flex.flex-col > div > div:nth-child({x}) > div:nth-child(2) > div > div > p')
                odds1.append(odd1.text)
                odd2 = driver.find_element(By.CSS_SELECTOR, f'#app > div > div.w-full.min-h-screen.flex-center.bg-gray-med_light > div > main > div.relative.w-full.flex-grow-1.min-w-\[320px\].bg-white-main > div.min-md\:px-\[10px\] > div.relative.flex.flex-col > div > div:nth-child({x}) > div:nth-child(3) > div > div > p')
                odds2.append(odd2.text)
            except:
                print("data not found\n")
            x += 1
        


    driver.quit()

    # initialize dictionary
    thisDict = {}
    thisDict['team1Name'] = team1Name
    thisDict['team1Score'] = team1Score
    thisDict['team2Name'] = team2Name
    thisDict['team2Score'] = team2Score

    for b, o1, o2 in zip(booky, odds1, odds2):
        thisDict[b] = o1, o2
    
    l = [str(page), str(gamNum)]
    s = '-'.join(l)
    write_json(thisDict, s)

    

# function to add to JSON
def write_json(new_data, iteration_data, filename='allData.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[iteration_data] = new_data
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 

if __name__ == "__main__":
    page = 44

    while page > 0:
        GetPageData(page)
        page -= 1

