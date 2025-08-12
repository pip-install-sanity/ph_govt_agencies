import requests
from bs4 import BeautifulSoup
import json


url = "https://www.foi.gov.ph/agencies/"

# send http get request  to the webpage
response = requests.get(url)

# parse the html
soup = BeautifulSoup(response.text,'html.parser') # '.text' gets the full HTML content of the page as a plain string

# use beautifulsoup to locate the info we want to extract
# as checked, the information has the <script> tag with id=typesearch and type=application/json
script_tag = soup.find("script", {"id": "typesearch", "type": "application/json"})


agencies = json.loads(script_tag.string)
# "script_tag.string" gets the raw json text inside the script tag
# "json.loads" parses that string into a Python object (usually a list or dict)

import csv

with open('d:\Home\Documents\Data Analytics\ph_govt_agencies\ph_govt_agencies.csv', 'w', encoding='utf-8') as file:
    # Write header
    file.write("List of Agency\n")

    for agency in agencies:
        name = agency.get("name","").replace(",","")
        file.write(f"{name}\n")