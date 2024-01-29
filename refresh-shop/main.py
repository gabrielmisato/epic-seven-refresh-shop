import pyautogui as pg
import time

pg.PAUSE = 0.5

mystic_image = 'images/mystic.png'
buy_mystic_image = 'images/buy_mystic.png'

bm_image = 'images/bm.png'
buy_bm_image = 'images/buy_bm.png'

refresh_image = 'images/refresh.png'
confirm_image = 'images/confirm.png'


def find_mystic():
    while True:
        try:
            mystic = pg.locateOnScreen(mystic_image, confidence=0.8)
            if mystic is not None:
                pg.moveTo(mystic)
                pg.moveRel(700, 30)
                pg.click()
                buy_mystic = pg.locateOnScreen(buy_mystic_image, confidence=0.8)
                pg.click(buy_mystic)
                time.sleep(1)
                break
        except pg.ImageNotFoundException:
            break


def find_bm():
    while True:
        try:
            bm = pg.locateOnScreen(bm_image, confidence=0.8)
            if bm is not None:
                pg.moveTo(bm)
                pg.moveRel(700, 30)
                pg.click()
                buy_bm = pg.locateOnScreen(buy_bm_image, confidence=0.8)
                pg.click(buy_bm)
                time.sleep(1)
                break
        except pg.ImageNotFoundException:
            find_mystic()
            break


def refresh_shop():
    time.sleep(3)
    print('Procurando BM e Mystic')
    while True:
        find_bm()
        pg.scroll(-250)
        
        time.sleep(0.5)
        find_bm()

        refresh = pg.locateOnScreen(refresh_image, confidence=0.8)
        pg.click(refresh)

        confirm = pg.locateOnScreen(confirm_image, confidence=0.7)
        pg.click(confirm)
        time.sleep(2)


refresh_shop()