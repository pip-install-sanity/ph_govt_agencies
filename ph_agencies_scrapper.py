import requests
from bs4 import BeautifulSoup
import json


url = "https://www.foi.gov.ph/agencies/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser') # '.text' gets the full HTML content of the page as a plain string

script_tag = soup.find("script", {"id": "typesearch", "type": "application/json"})

agencies = json.loads(script_tag.string)

import csv

with open('d:\Home\Documents\Data Analytics\ph_govt_agencies\ph_govt_agencies.csv', 'w', encoding='utf-8') as file:
    # Write header
    file.write("List of Agency\n")

    for agency in agencies:
        name = agency.get("name","").replace(",","")
        file.write(f"{name}\n")