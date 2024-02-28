import sys
import os
sys.path.append(os.getcwd())
import pyautogui
import pyperclip
import random
import time

pyautogui.PAUSE = 1

username = 'U708047'
password = '###'

text_startRemoteWork = 'テレワーク始めます。'


def initTeams():
    # proxy
    inputTeamsProxy()
    inputTeamsProxy()

    pyautogui.sleep(7)
    pyautogui.hotkey('alt','tab')

    clickOnScreenByPic('./resource/screenPic/TeamsNSWContactGroupMessageInput.png',120,530)

    # type start remote work
    pyperclip.copy(text_startRemoteWork)
    pyautogui.hotkey('ctrl','v')


def kintai():
    # proxy
    clickOnScreenByPic('./resource/screenPic/chromeProxyLoginDialog.png',320,170)
    # kindai login
    clickOnScreenByPic('./resource/screenPic/ccbizLoginPage.png',260,220)
    # click start working button
    clickOnScreenByPic('./resource/screenPic/ccbizStartWorkBtn.png',160,120)
    # confirm alert
    clickOnScreenByPic('./resource/screenPic/ccbizAlertOKBtn.png',280,120)
    # close chrome
    clickOnScreenByPic('./resource/screenPic/chromeWindowControl.png',550,10)

    
def inputTeamsProxy():
    clickOnScreenByPic('./resource/screenPic/proxyDialog.png',0,0)

    # username
    pyautogui.typewrite(username,0.02)

    pyautogui.press('tab')
    # password
    pyautogui.typewrite(password,0.02)

    #OK
    pyautogui.press('enter')

def clickOnScreenByPic(picPath,adjustX,adjustY):
    left, top, width, height = pyautogui.locateOnScreen(picPath,confidence=.7)

    left += adjustX
    top += adjustY  
    center = pyautogui.center((left, top, width, height))
    
    # pyautogui.moveTo(center.x,center.y)
    pyautogui.click(center)

def keepAlive():
    latestMousePosition = [0,0]

    while True:
        mousePoint = pyautogui.position()
        if(latestMousePosition[0] == mousePoint[0] and latestMousePosition[1] == mousePoint[1] ):
            pyautogui.move(random.randint(-20,20),random.randint(-20,20))
        
        mousePoint = pyautogui.position()
        latestMousePosition[0] = mousePoint[0]
        latestMousePosition[1] = mousePoint[1]

        pyautogui.sleep(5)
