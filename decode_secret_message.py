from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re

def decode(doc_url):
    #Send get request to google doc
    doc = requests.get(doc_url)

    '''
    Pull table tag from the document to avoid reading in the whole document and wasting memory, and pass soup strainer in Beautiful Soup
    constructor
    ''' 
    only_table_tag = SoupStrainer('table')
    soup = BeautifulSoup(doc.text, 'html.parser', parse_only=only_table_tag)

    '''Next, find all numbers in the table and create the coordinates'''
    coordinates = []
    characters = []
    max_x, max_y, type = 0, 0, 0

    for string in soup.strings:
        if re.search('[0-9][0-9]*', string):
            coordinates.append(int(string))
        elif len(coordinates) > 0 and len(string) == 1:
            characters.append(string)

    print(coordinates)
    print(characters)














if __name__ == '__main__':
    document_url = input("Enter website name: ")
    decode(document_url)
    