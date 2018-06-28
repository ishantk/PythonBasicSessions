import requests
from bs4 import BeautifulSoup

response = requests.get("http://zeenews.india.com/")
soup = BeautifulSoup(response.text,"html.parser")

print("=============================")
print("News Source",soup.title.text)
print("=============================")

divTags = soup.find_all('div', class_="mini-con")
# print(divTags[0])
# print("****************")
# print(divTags[0].text)
for tag in divTags:
    print(tag.text)
    print("*************************************")