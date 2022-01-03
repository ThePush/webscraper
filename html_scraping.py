# the requests package contains the get() function used to get the
# website's HTML code
import requests
import csv

# BeautifulSoup package contains useful HTML parsing tools
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# here we convert the HTML page into a soup object
soup = BeautifulSoup(page.content, 'html.parser')

# all the titles are tagged <a> and class "gem-c-document-list__item-title"
# we store them in a variable
titles_bs = soup.find_all("a", class_="gem-c-document-list__item-title")

# we create a new liste in which each element is one title as a string
titles = []
for title in titles_bs:
    titles.append(title.string)
    
# same process with the descriptions
descriptions_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []
for desc in descriptions_bs:
    descriptions.append(desc.string)
    
# we store these lists into a .csv file
# the header declares the keys of our dict
header = ["title", "description"]
with open('datas.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    
# we use zip to go through multiples lists in a row
    for title, description in zip(titles, descriptions):
        line = [title, description]
        writer.writerow(line)

