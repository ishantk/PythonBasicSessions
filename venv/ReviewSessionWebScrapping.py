import requests
from bs4 import BeautifulSoup

"""
response = requests.get("https://twitter.com/dna")
print(response.text)

soup = BeautifulSoup(response.text,"html.parser")

print("=================")
print(type(soup))
print(soup.title.text)
print("=================")

pTag = soup.find("p")

print(pTag.text)

print("=================")

# divTags = soup.find_all("div",class_="js-tweet-text-container")

response = requests.get("http://zeenews.india.com/")
print(response.text)

soup = BeautifulSoup(response.text,"html.parser")

print("========ZEE NEWS=========")

divTags = soup.find_all("div",class_="mini-con")
for tag in divTags:
    # print(tag)
    print(tag.text)
    print("******************")

"""

"""
movies = []
ratings = []

response = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in_7")
soup = BeautifulSoup(response.text,"html.parser")
tdTags = soup.find_all("td",class_="titleColumn")
for tag in tdTags:
    print(tag.text)
    movies.append(tag.text)
    print("******************")

tdTags = soup.find_all("td",class_="ratingColumn")
for tag in tdTags:
    sTag = tag.find("strong")
    if sTag is not None:
        print(sTag.text)
        ratings.append(sTag.text)

    print("******************")

"""

"""
1. WebScrap IMDB
2. Dump the data in CSV File
3. Read teh CSV file using Pandas
4. Draw a Plot
5. Compare Indian and US Move Trends on Plots
6. Give the result who has the most ratings in current year
7. Predict Indian Movies Trends in 2020
8. Predict US Movies Trends in 2020
9. Draw the predictions together in Graphs
"""

data = {"inputdigit":64,"sno":2,"party":"Rahul","pyear":2018}
response = requests.post("http://delhihighcourt.nic.in/dhc_case_status_list_new.asp",data=data)
print(response.text)
