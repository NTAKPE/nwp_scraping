#! python3
import requests as re
import os 

#Main functions of the scraper
def get_newspapers(obj_soup):
    data = obj_soup.select('div .col-xs-8')
    titro_list = []
    for items in data :
        title = items.select('p')[0].getText()
        cover = items.select('.imgTitro')[0].attrs['src']
        titro_list.append({'title': title, 'cover': cover})
    return titro_list

def listToText(obj):
    return "{}\nURL = {}\n\n".format(obj['title'], obj['cover'])

def recap_data(ls, today, path):
    filename = path+'/'+'_'.join(today.split(' '))+'.txt'
    with open(filename, 'w') as myfile:
        myfile.write('Titres du {}\n\n'.format(today))
        for item in ls :
            myfile.write(item)
    return

def img_dwd(ls, today, path):
    for index, url in enumerate(ls):
        img_data = re.get(url).content
        img_name = path+'/'+'img'+str(index)+'.jpg'
        with open (img_name, 'wb') as handler:
            handler.write(img_data)
    return
