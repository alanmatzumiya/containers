from bs4 import BeautifulSoup
import requests
get = requests.get(url)
data = get.content
soup = BeautifulSoup(data, "html.parser")
list_tags = soup.find_all(class_="js-navigation-open link-gray-dark")
element = list_tags[0]
link = element.get("href")
print(link)
