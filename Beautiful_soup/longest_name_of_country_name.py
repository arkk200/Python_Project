from requests import get
from bs4 import BeautifulSoup

url = "https://en.wiktionary.org/wiki/Appendix:Countries_and_territories_of_the_world"
response = get(url)

if response.status_code != 200:
    print("Can't scrapping", response.status_code)
    exit(0)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_="wikitable")
tbody = table.find('tbody')
table_rows = tbody.find_all('tr')
table_rows.pop(0)
countries = []
for table_row in table_rows:
    countries.append(table_row.find('td'))
longest_country = ''
for country in countries:
    country_name = country.find('a').string
    if len(longest_country) < len(country_name):
        longest_country = country_name
print(len(longest_country))