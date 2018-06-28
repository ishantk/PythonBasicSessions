import requests
from bs4 import BeautifulSoup

response = requests.get("https://twitter.com/dna")

# HTML Response
# print(response.text)

soup = BeautifulSoup(response.text,"html.parser")

"""print(soup)
print(type(soup))
print("====================")
print(soup.prettify())
print("====================")"""

print("We are Going to Fetch Data for:")
print(soup.title.text)

"""
print("====================")
children = soup.children

for child in children:
    print(child)
    print("****************")
"""

"""
pTags = soup.find_all('p')
for tag in pTags:
    print(tag)
    print("****************")
"""

# divTags = soup.find_all('div')
# print(divTags[0])
# print("****************")
# print(divTags[0].text)
# for tag in divTags:
#     print(tag)
#     print("****************")

# divTagOnZerothIndex = soup.find('div')
# print(divTagOnZerothIndex.text)

divTags = soup.find_all('div', class_="js-tweet-text-container")
print(divTags[0])
print("****************")
print(divTags[0].text)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

for tag in divTags:
    # print(tag)
    print(tag.text)
    print("****************")