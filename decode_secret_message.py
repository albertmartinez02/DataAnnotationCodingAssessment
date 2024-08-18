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
    x_coordinates = []
    y_coordinates = []
    characters = []
    max_x, max_y, type = 0, 0, 0

    for string in soup.strings:
        if re.search('[0-9][0-9]*', string):
            if(type == 0):
                x_coordinates.append(int(string))
                type = 1
            else:
                y_coordinates.append(int(string))
                type = 0
        elif len(x_coordinates) > 0 and len(string) == 1:
            characters.append(string)

    #Find dimensions of grid by finding maxes(add 1 for zero index grid coordinates), and create 2d list to print the information
    max_x = max(x_coordinates) + 1
    max_y = max(y_coordinates) + 1
    print(max_x, max_y)

    secret_message = [None] * max_y
    for i in range(max_y):
        secret_message[i] = [None] * max_x
    
    for i in range(max_y):
        print(secret_message[i])















if __name__ == '__main__':
    document_url = input("Enter website name: ")
    decode(document_url)
    