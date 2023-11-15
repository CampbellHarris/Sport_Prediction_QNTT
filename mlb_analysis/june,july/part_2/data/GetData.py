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

df = pd.DataFrame()

driver = webdriver.Chrome()
link = "https://www.oddsportal.com/baseball/usa/mlb-2022/results/#/page/55"
driver.get(link)

#soup = BeautifulSoup(driver.page_source, "html.parser")
#texts = []
#rows = soup.find('div', {'data-mlb-test': 'individualGamesContainer'}).find_all('a')