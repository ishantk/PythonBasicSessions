# import urllib.request
# req = urllib.request.urlopen("http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2")
# req = urllib.request.urlopen("https://stackoverflow.com/")
# data = req.read()
# print(data)
import requests
import threading

class FetchDataTask(threading.Thread):

    def run(self):
        response = requests.get("http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2")
        print(response)
        print(response.text)

        print("====================")

        json = response.json()
        books = json["bookstore"]

        # print(books)

        for book in books:
            print(book)


print("This is Statement1")
print("This is Statement2")



"""def getDataFromWebService():
    response = requests.get("http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2")
    print(response)
    print(response.text)

    print("====================")

    json = response.json()
    books = json["bookstore"]

    #print(books)

    for book in books:
        print(book)


getDataFromWebService()"""

task = FetchDataTask()
task.start()


print("This is Statement3")
print("This is Statement4")