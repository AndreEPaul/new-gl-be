from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

redraft_url = 'https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php'
dynasty_url = 'https://www.fantasypros.com/nfl/rankings/dynasty-overall.php'

redraft_txt = requests.get(redraft_url).text
dynasty_txt = requests.get(dynasty_url).text

redraft_soup = BeautifulSoup.(redraft_txt, 'html.parser')
dynasty_soup = BeautifulSoup.(dynasty_txt, 'html.parser')


