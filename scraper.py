#Requirements
#makesure you have install bs4(beautifulSoup)
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#URL to be scraped
my_url = 'http://www.bathandbodyworks.com/c/body-care/new-body-care'

#Opens up connection, and grabs html from page, then close content
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parsing the HTML data
# remember soup is refering to beautifulSoup 
page_soup = soup(page_html, "html.parser")

#Grabs each product description container
containers = page_soup.findAll("div", {"class":"product-tile"})
    
#check to see if anything is scraping and if its the correct info
#print(containers)

#Makes a CSV file with the name of products    
filename = "products.csv"
f = open(filename, "w")

#Writes the headers into the products.csv file
headers = "product_name,product_type, price, promotion\n"
f.write(headers)

#Loops through each product        
for container in containers:
    
    #getting the name of the product
    name_container= container.findAll("div", {"class":"product-name"})
    product_name = name_container[0].text
    print(product_name)

