from  bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

file = open("scraped_quotes.csv", "w")
write = csv.writer(file)
write.writerow(["QUOTES", "AUTHORS"])

for quotes, authors in zip(quotes, authors):
    print(quotes.text + "-" + authors.text)
    write.writerow([quotes.text, authors.text])
file.close()