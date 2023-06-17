import requests
from requests import request
from bs4 import BeautifulSoup as bs

page = 1
open('text.txt', 'w').close()
while page != 6:
    r = requests.get('https://stopgame.ru/articles/p' + str(page))
    html = bs(r.content, 'html.parser')

    sring = html.select('._default-grid_1f00f_215 ')

    if len(sring):
        for i in sring:
            ti = i.select('._card__content_givrd_398 > a')
            for j in ti:
                with open('text.txt' ,'a',encoding='utf-8') as we:
                    we.write(f'{str(j.text)} \n')
        page +=1
    else:
        break