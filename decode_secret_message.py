from bs4 import BeautifulSoup
import requests

def decode(doc_url):
    #Send get request to google doc
    doc = requests.get(doc_url)
    soup = BeautifulSoup(doc.text, 'html.parser')

    #Get max_x and max_y to determine size of grid
    max_x, max_y = 0, 0

    for information in soup.find_all("span", "c1"):
        print(information)
    print(soup.get_text())

if __name__ == '__main__':
    document_url = input("Enter website name: ")
    decode(document_url)
    