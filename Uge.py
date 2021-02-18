import requests
from bs4 import BeautifulSoup
import time
import schedule

global soup
global new
global old

old = 0

req = requests.get("https://bbs.ruliweb.com/community/board/300143")

html = req.text

soup = BeautifulSoup(html,"html.parser")

#계속 값을 새로 불러오는 함수
def saerogochim():

    global soup

    req = requests.get("https://bbs.ruliweb.com/community/board/300143")

    html = req.text

    soup = BeautifulSoup(html,"html.parser")

    update(16,5)


#업데이트
def update(x,list):
    global old
    new = soup.select(".board_main .board_list_table .id")[list].get_text()
    if old < new:
        update(x+3,list+1)
    else:
        return
    print(soup.select(".board_main.theme_default td a, .board_main.theme_default .table_body_td a")[x].get_text())
    if x == 16:
        old = new

def init_update():
    global old
    new = soup.select(".board_main.theme_default td a, .board_main.theme_default .table_body_td a")[16].get_text()
    print(new)
    old = soup.select(".board_main .board_list_table .id")[5].get_text()

#init

init_update()

#schedule
schedule.every(10).seconds.do(saerogochim)

while True:
    schedule.run_pending()
    time.sleep(1)
