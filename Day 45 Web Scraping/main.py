from bs4 import BeautifulSoup

file_path = "Day 45 Web Scraping/website.html"

with open(file_path, encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)