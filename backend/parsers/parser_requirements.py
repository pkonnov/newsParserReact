import requests
import lxml.html
from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
# import hashlib
import dateutil.parser as parser
import random

headers={'User-Agent': 'Mozilla/5.0'}
conn = sqlite3.connect('../db.sqlite3', check_same_thread=False)
