from flask import Flask, render_template
from bs4 import BeautifulSoup as bs
import requests

redraft_url = 'https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php'
dynasty_url = 'https://www.fantasypros.com/nfl/rankings/dynasty-overall.php'
rookie_url = 'https://www.fantasypros.com/nfl/rankings/rookies.php'
kicker_url = 'https://www.fantasypros.com/nfl/rankings/k-cheatsheets.php'
dst_url = 'https://www.fantasypros.com/nfl/rankings/dst-cheatsheets.php'

redraft_resp = requests.get(redraft_url)
dynasty_resp = requests.get(dynasty_url)
rookie_resp = requests.get(rookie_url)
kicker_resp = requests.get(kicker_url)
dst_resp = requests.get(dst_url)

redraft_soup = bs(redraft_resp.text, 'html.parser')
dynasty_soup = bs(dynasty_resp.text, 'html.parser')
rookie_soup = bs(rookie_resp.text, 'html.parser')
kicker_soup = bs(kicker_resp.text, 'html.parser')
dst_soup = bs(dst_resp.text, 'html.parser')

redraft_ranks = []
dynasty_ranks = []
rookie_ranks = []
kickers = []
dsts = []

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

for tr in kicker_soup.find_all('tr'):
    td = tr.find_all(class_="full-name")
    if(td != []):
        kickers.append(td[0].string)

for tr in dst_soup.find_all('tr'):
    td = tr.find_all(class_="full-name")
    if(td != []):
        dsts.append(td[0].string)

for kicker in kickers:
    if(kicker in redraft_ranks):
        redraft_ranks.remove(kicker)
    if(kicker in dynasty_ranks):
        dynasty_ranks.remove(kicker)

for dst in dsts:
    if(dst in redraft_ranks):
        redraft_ranks.remove(dst)
    if(dst in dynasty_ranks):
        dynasty_ranks.remove(dst)

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

def get_redraft_no_rookies():
    return redraft_ranks_without_rookies

def get_redraft_rookies():
    return redraft_ranks_with_rookies

def get_dynasty_no_rookies():
    return dynasty_ranks_without_rookies

def get_dynasty_rookies():
    return dynasty_ranks_with_rookies

def get_rookies():
    return rookie_ranks