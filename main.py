import requests
from bs4 import BeautifulSoup

url = "http://news.ycombinator.com"

#Step 1:Get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

#Step 2:Parse the HTML


soup = BeautifulSoup(htmlContent,'html.parser')

print(soup.prettify)
#Step 3:HTML Tree Traversal
#1.Tag
#2.NavigableString
#3.Beautiful Soup
#4.Comment
#get the title of the HTML page

title = soup.title

#get all paragraphs(or any other data piece from the page)

paras = soup.find_all('p')
print(paras)

#get headings

headings = soup.find_all('h1')
print(headings)

#find all elemets with class lead 
#print(soup.find_all("p"))

#getting text from elements
# print(soup.find('p').get_text())
# print(soup.get_text())



#get table data

tableData = soup.find_all('tr')
print(tableData)
