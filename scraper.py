from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import pandas as pd
from bs4 import BeautifulSoup
import gspread

google_url = "https://www.google.com"

driver = webdriver.Chrome()
driver.get(google_url)

google_serarch = driver.find_element(By.NAME, "q")
google_serarch.send_keys("amazon.in")
google_serarch.send_keys(Keys.RETURN)

first_result = driver.find_element(By.XPATH, "(//h3)[1]")  # XPath to select the first result's title
first_result.click()

search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_key = "coffee"
search_bar.clear()
search_bar.send_keys(search_key)
search_bar.send_keys(Keys.RETURN)

response = driver.page_source
soup = BeautifulSoup(response, 'html.parser')
result = []
time = str(datetime.datetime.now())
result.append(time)
result.append(search_key)

# first add sb banner

sb_banner = soup.find('div', class_="s-result-item s-widget s-widget-spacing-large AdHolder s-flex-full-width").text
result.append(sb_banner)

# SBVideo ad Name 

sbv = soup.find('div',class_="sg-col-0-of-12 sg-col-4-of-16 sbv-product-container sg-col sg-col-12-of-24 sg-col-8-of-20").find('h2').text
result.append(sbv)

# SBVideo ad ASIN
sbv_asin = soup.find('div',class_="sg-col-0-of-12 sg-col-4-of-16 sbv-product-container sg-col sg-col-12-of-24 sg-col-8-of-20").find('div',{"data-cy":"asin-faceout-container"}).get("data-dib-asin")
result.append(sbv_asin)

# SBVideo ad Price
sbv_price = "₹"+ soup.find('div',class_="sg-col-0-of-12 sg-col-4-of-16 sbv-product-container sg-col sg-col-12-of-24 sg-col-8-of-20").find('span',class_="a-price").text.split("₹")[1]
result.append(sbv_price)

# when 4 ads are in line
ads = soup.find_all('div',class_="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20")
if len(ads)==0:
    # when adds are in landscape
    ads = soup.find_all('div',class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16")

# sp ad 1 to 4
sp_ad = []
for i in range(len(ads)):
    if i==4:
        break
    ad = ads[i].h2.text
    ad_price ="₹" +ads[i].find('span',class_="a-price").text.split("₹")[1]
    ad_asin = ads[i].find('div',{"data-cy":"asin-faceout-container"}).get("data-dib-asin")
    result.append(ad)
    result.append(ad_asin)
    result.append(ad_price)

# Google Sheet Update

gc = gspread.service_account(filename="cred_file.json")
sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1wKzdScL4OsW58cm9g2hBNpocfp6yXXVCV9WRyf1sOIc/edit?gid=0#gid=0")
worksheet = sheet.get_worksheet(index=0)
data = pd.DataFrame(worksheet.get_all_records())
data.loc[len(data)] = result
worksheet.update([data.columns.values.tolist()] + data.values.tolist())
