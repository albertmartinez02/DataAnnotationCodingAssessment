from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re

def decode(doc_url):
    #Send get request to google doc
    doc = requests.get(doc_url)
    soup = BeautifulSoup(doc.text, 'html.parser')

    #Get max_x and max_y to determine size of grid
    max_x, max_y = 0, 0

    for information in soup.find_all("span"):
        print(information.string)
    information = soup.find_all("span")
    print(information[0] , "This is the first info found by find all")


if __name__ == '__main__':
    document_url = input("Enter website name: ")
    decode(document_url)
    