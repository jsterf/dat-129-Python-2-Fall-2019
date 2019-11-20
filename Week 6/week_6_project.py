
from bs4 import BeautifulSoup
import urllib.request

#set URL equal to the term we want to search
def getSearchURL (term):
  url ='https://www.goodreads.com/search?q=%s' % (str(term))
  return url

#open URL and set it to response variable
def getHTMLPageText(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        return response.read()
 
#main program area
        
#get URL for a specific search term
pageText = getHTMLPageText(getSearchURL('milo'))
#use BeautifulSoup to open webpage and set equal to soup variabl
soup = BeautifulSoup(pageText, 'html.parser')
#print BeautifulSoup object
print(soup.prettify())

#only bring back certain attributes
#sets all links with a bookTitle class to eles
eles = soup.find_all('a', 'bookTitle')
or\\#iterrates thru all book Title items and brings back the text (actual book title) in the link element
for item in eles:
    tag = item.find('span').string
    print(tag)