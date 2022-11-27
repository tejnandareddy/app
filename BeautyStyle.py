import time
import utils
import xmltojson as xmltojson

import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import json

driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
driver.get("https://github.com/")
driver.find_element('xpath',
                    ("/html/body/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")).send_keys(
    "security")

print("Title of the page :", driver.title)

time.sleep(5)
driver.find_element('xpath', ("//*[@id='jump-to-suggestion-search-global']/a/div[3]/span[2]")).click()

keys = ["title", "description", "tags", "starts", "languages", "licensed_by", "updated_time"]

# jsonSource = driver.find_element('xpath', '/html/body/div[4]/main/div/div[3]/div/ul')

print(driver.page_source)

# with open('data.html', 'wb') as file:
#     file.write(driver.page_source)

# print("hello")
soup = BeautifulSoup(driver.page_source, 'html.parser')
#print(soup)
'''
repo_details = soup.findAll("ul", class_="repo_list")
print((len(repo_details)))
for i in page(1,6):
    if:
        print("acesss")
     else:
         print("done")

# data = soup.find('h3')
# uls = []
# for nextSibling in data.findNextSiblings():
#     if nextSibling.name == 'h2':
#         break
#     if nextSibling.name == 'ul':
#         uls.append(nextSibling)
#
# print(uls)

data = soup.find_all("ul", {"id": "repo_list"})

# print(data)

# print(len(data))
# exit()
# get all list elements
# lis = data.find_all('li')

# add a helper lambda, just for readability
# find_ul = lambda x: x.find_all('ul')
# uls = [find_ul(elem) for elem in lis if find_ul(elem) != []]
# print(uls)
# dddd=driver.page_source
# file = open("data.html", "w")
# file.write(str(dddd))

# db=pd.read_html("data.html")
# db.to_json('SecurityResultGitHub_TinmeStamp.json')
'''
with open("sample.html", "r") as html_file:
    html = html_file.read()
    json_ = xmltojson.parse(html)
'''
'''
table_data = [[cell.text for cell in row("td")]
              for row in BeautifulSoup(driver.page_source)("tr")]
print(json.dumps(dict(table_data)))
json_ = xmltojson.parse(table_data)
