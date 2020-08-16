from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

redraft_txt = requests('https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php').text
dynasty_txt = requests('https://www.fantasypros.com/nfl/rankings/dynasty-overall.php').text

