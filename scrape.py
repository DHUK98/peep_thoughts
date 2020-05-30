from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import csv


def scrap_thoughts(url):
    html = BeautifulSoup()
