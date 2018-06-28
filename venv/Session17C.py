import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in_7")
soup = BeautifulSoup(response.text,"html.parser")

print("=============================")
print("Movie Source",soup.title.text)
print("=============================")

tdTags = soup.find_all('td', class_="titleColumn")
# print(tdTags[0])
# print("****************")
# print(tdTags[0].text)

movies = []

for tag in tdTags:
    print(tag.text)
    movies.append(tag.text.strip())
    print("*************************************")


print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#
# for movie in movies:
#     print(movie)

tdTags = soup.find_all('td', class_="ratingColumn")
print(tdTags[0].find("strong").text)


for tag in tdTags:
    # print(tag.text)
    if tag.find("strong") is not None:
        print(tag.find("strong").text)