from flask import Flask, render_template
from bs4 import BeautifulSoup as bs
import requests

redraft_url = 'https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php'
dynasty_url = 'https://www.fantasypros.com/nfl/rankings/dynasty-overall.php'
rookie_url = 'https://www.fantasypros.com/nfl/rankings/rookies.php'

redraft_resp = requests.get(redraft_url)
dynasty_resp = requests.get(dynasty_url)
rookie_resp = requests.get(rookie_url)

redraft_soup = bs(redraft_resp.text, 'html.parser')
dynasty_soup = bs(dynasty_resp.text, 'html.parser')
rookie_soup = bs(rookie_resp.text, 'html.parser')

redraft_ranks = []
dynasty_ranks = []
rookie_ranks = []

for tr in redraft_soup.find_all('tr'):
    td = tr.find_all(class_="full-name")
    if(td != []):
        redraft_ranks.append(td[0].text)

for tr in dynasty_soup.find_all('tr'):
    td = tr.find_all(class_="full-name")
    if(td != []):
        dynasty_ranks.append(td[0].text)

for tr in rookie_soup.find_all('tr'):
    td = tr.find_all(class_="full-name")
    if(td != []):
        rookie_ranks.append(td[0].text)

# for elt in redraft_ranks[:10]:
#     print(elt)

# for elt in dynasty_ranks[:10]:
#     print(elt)

# for elt in rookie_ranks[:10]:
#     print(elt)

