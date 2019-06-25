import os
import requests
from bs4 import BeautifulSoup

def get_data():
   #obtain the content of the URL in HTML
   url = "https://cpe.calpoly.edu/faculty/foaad/"
   myRequest = requests.get(url)
   
   #Create a soup object that parses the HTML
   soup = BeautifulSoup(myRequest.text,"html.parser")

   professor = {}
   
   table = soup.find('table', attrs={'id': 'blankTable'})
   info = table.find_all('tr')[1].find_all('td')

   professor['days'] = info[0].get_text()
   professor['time'] = info[1].get_text()
   professor['description'] = info[2].get_text()

if __name__ == "__main__":
   get_data()
