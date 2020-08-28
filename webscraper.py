from flask import Flask, render_template
from bs4 import BeautifulSoup as bs
import requests

rd_url = 'https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php'
dy_url = 'https://www.fantasypros.com/nfl/rankings/dynasty-overall.php'

rd_resp = requests.get(rd_url)
dy_resp = requests.get(dy_url)

rd_soup = bs(rd_resp.text, 'html.parser')
dy_soup = bs(dy_resp.text, 'html.parser')

rd_ranks = []
dy_ranks = []

for tr in rd_soup.find_all('tr'):
    td = tr.find_all(class_="full-name")
    if(td != []):
        rd_ranks.append(td[0].text)

for tr in dy_soup.find_all('tr'):
    td = tr.find_all(class_="full-name")
    if(td != []):
        dy_ranks.append(td[0].text)

for elt in rd_ranks[:10]:
    print(elt)

for elt in dy_ranks[:10]:
    print(elt)