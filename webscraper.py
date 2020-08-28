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
        redraft_ranks.append(td[0].string)

for tr in dynasty_soup.find_all('tr'):
    td = tr.find_all(class_="full-name")
    if(td != []):
        dynasty_ranks.append(td[0].string)

for tr in rookie_soup.find_all('tr'):
    td = tr.find_all(class_="full-name")
    if(td != []):
        rookie_ranks.append(td[0].string)

redraft_ranks_with_rookies = redraft_ranks
dynasty_ranks_with_rookies = dynasty_ranks

redraft_ranks_without_rookies = []
dynasty_ranks_without_rookies = []

for player in redraft_ranks:
    if(player not in rookie_ranks):
        redraft_ranks_without_rookies.append(player)

for player in dynasty_ranks:
    if(player not in rookie_ranks):
        dynasty_ranks_without_rookies.append(player)