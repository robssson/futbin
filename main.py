import urllib
import re
import json
from urllib import request
from bs4 import BeautifulSoup


def get_data_from_url():
    url = 'https://www.futbin.com/'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    text = res.read()
    get_totw_players(text)


def get_totw_players(text):
    """ Scrape players TOTW with their OVERALL from this week """
    soup = BeautifulSoup(text, 'html.parser')
    totw_raw = str(soup.find('div', attrs={'id': 'totw'}))
    soup = BeautifulSoup(totw_raw, 'html.parser')
    players = soup.find_all('a', attrs={'target': ''})
    totw = {}
    for idx, player in enumerate(players):
        regex = '\/19\/player\/\d+\/(.*?)\"'
        name = re.search(regex, str(player))
        rating = player.find('div', attrs={'class': 'pcdisplay-rat'})
        if name is not None:
            player_idx = f"player_{idx}"
            player_totw = {}
            player_totw[player_idx] = {"name:": name.group(1), 
                                       "rating": rating.text}
            totw.update(player_totw)


if __name__ == '__main__':
    get_data_from_url()

