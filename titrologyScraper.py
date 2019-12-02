#! python3
# Scraper.py - Scrap data from abidjan.net/titrologie

import requests as re
import bs4
from config import get_newspapers, listToText, recap_data, img_dwd
import os 

#Scrape data from abidjan.net
url = 'https://news.abidjan.net/titrologie/'
res = re.get(url)
res.raise_for_status()
res_soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Get today
def get_date(obj_soup):
    data = obj_soup.select('.FontTabTitro b')
    return data[0].getText()
today = get_date(res_soup)

#Set a new directory and change for it
path = os.getcwd()+'/assets/'+'_'.join(today.split(' '))
os.makedirs(path)
os.chdir(path)

def main():
    dirpath = os.getcwd()
    print('Waiting for robot to scrap Titrologie...')

    #Get data of the day
    newspapers = get_newspapers(res_soup)

    #Generate the daily recap
    title_list = [listToText(obj) for obj in newspapers]
    recap_data(title_list, today, dirpath)

    #Download covers of newspapers
    url_list = [obj['cover'] for obj in newspapers]
    img_dwd(url_list, today, dirpath)
    print("Well it's done now.")

if __name__ == "__main__":
    main()