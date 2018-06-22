jsonData = """
    {
      "bookstore": [
        {
          "price": "100 INR", 
          "name": "Objective C", 
          "author": "Steve Jobs"
        }, 
        {
          "price": "200 INR", 
          "name": "Android Programming", 
          "author": "Aaron Brooks"
        }, 
        {
          "price": "300 INR", 
          "name": "Advance Java", 
          "author": "David Smith"
        }
    ]
}

"""

print(jsonData)

# JSON Parsing
# Convert JSON Data into Objects of class Book


# XML Parsing
# Convert XML Data into Objects of class Note
xmlData = """
    <note>
      <to>Tove</to>
      <from>Jani</from>
      <heading>Reminder</heading>
      <body>Don't forget me this weekend!</body>
    </note>
"""

# CSV Parsing
# Convert CSV Data into Objects of class Person
csvData = """
    Sally Whittaker,2018,McCarren House,312,3.75
    Belinda Jameson,2017,Cushing House,148,3.52
    Jeff Smith,2018,Prescott House,17-D,3.20
    Sandy Allen,2019,Oliver House,108,3.48
"""
from urllib import request