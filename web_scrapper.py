import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/home/heisenberg/Desktop/Projects/Dev/chromedriver'
service = Service(path)

driver = webdriver.Chrome(service=service)
driver.get(website)

all_matches_btn = driver.find_element(by=By.XPATH, value='//label[@analytics-event="All matches"]')
all_matches_btn.click()

matches = driver.find_elements(by=By.TAG_NAME, value='tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(by=By.XPATH, value='./td[1]').text)
    home_team.append(match.find_element(by=By.XPATH, value='./td[2]').text)
    score.append(match.find_element(by=By.XPATH, value='./td[3]').text)
    away_team.append(match.find_element(by=By.XPATH, value='./td[4]').text)

driver.quit()

df = pd.DataFrame({'Date': date, 'Home Team': home_team, 'Score': score, 'Away Team': away_team})
df.to_csv('football_data.csv', index=False)
print(df)
