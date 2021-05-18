import pyautogui
import time


def chem(meet_id, password):

    pyautogui.press('esc',interval=0.1)

    time.sleep(0.2)

    pyautogui.press('win',interval=0.1)
    pyautogui.write('zoom')
    pyautogui.press('enter',interval=0.5)


    time.sleep(10)


    x,y = pyautogui.locateCenterOnScreen('Capture.png')
    pyautogui.click(x,y)


    pyautogui.press('enter',interval=1)
    pyautogui.write(meet_id)
    pyautogui.press('enter',interval=1)


    time.sleep(3)
    pyautogui.press('enter',interval=1)
    pyautogui.write(password)
    pyautogui.press('enter',interval = 1)


def physics(meet_id, password):
    pyautogui.press('esc', interval=0.1)

    time.sleep(0.2)

    pyautogui.press('win', interval=0.1)
    pyautogui.write('zoom')
    pyautogui.press('enter', interval=0.5)

    time.sleep(10)

    x, y = pyautogui.locateCenterOnScreen('Capture.png')
    pyautogui.click(x, y)

    pyautogui.press('enter', interval=1)
    pyautogui.write(meet_id)
    pyautogui.press('enter', interval=1)

    time.sleep(3)
    pyautogui.press('enter', interval=1)
    pyautogui.write(password)
    pyautogui.press('enter', interval=1)


def maths(meet_id, password):
    pyautogui.press('esc', interval=0.1)

    time.sleep(0.2)

    pyautogui.press('win', interval=0.1)
    pyautogui.write('zoom')
    pyautogui.press('enter', interval=0.5)

    time.sleep(10)

    x, y = pyautogui.locateCenterOnScreen('Capture.png')
    pyautogui.click(x, y)

    pyautogui.press('enter', interval=1)
    pyautogui.write(meet_id)
    pyautogui.press('enter', interval=1)

    time.sleep(3)
    pyautogui.press('enter', interval=1)
    pyautogui.write(password)
    pyautogui.press('enter', interval=1)


def cs(meet_id, password):
    pyautogui.press('esc', interval=0.1)

    time.sleep(0.2)

    pyautogui.press('win', interval=0.1)
    pyautogui.write('zoom')
    pyautogui.press('enter', interval=0.5)

    time.sleep(10)

    x, y = pyautogui.locateCenterOnScreen('Capture.png')
    pyautogui.click(x, y)

    pyautogui.press('enter', interval=1)
    pyautogui.write(meet_id)
    pyautogui.press('enter', interval=1)

    time.sleep(3)
    pyautogui.press('enter', interval=1)
    pyautogui.write(password)
    pyautogui.press('enter', interval=1)


def english(meet_id, password):
    pyautogui.press('esc', interval=0.1)

    time.sleep(0.2)

    pyautogui.press('win', interval=0.1)
    pyautogui.write('zoom')
    pyautogui.press('enter', interval=0.5)

    time.sleep(10)

    x, y = pyautogui.locateCenterOnScreen('Capture.png')
    pyautogui.click(x, y)

    pyautogui.press('enter', interval=1)
    pyautogui.write(meet_id)
    pyautogui.press('enter', interval=1)

    time.sleep(3)
    pyautogui.press('enter', interval=1)
    pyautogui.write(password)
    pyautogui.press('enter', interval=1)

# 820 - 920
# english("878 528 377","6bJwS8")
# time.sleep(6840)
# 1010 - 1110
# cs("766 5421 8158", "7aGNbj")
# time.sleep(6840)
# 1200 - 0100
# cs("766 5421 8158", "7aGNbj")
# time.sleep(6840)
# 0100 - 0210
# english("878 528 377","6bJwS8")
# cs("766 5421 8158", "7aGNbj")
maths("332 187 5104", "464500")
# chem("790 147 4619","chem123")
#physics("","")a



# time.sleep(1020)
# maths("332 187 5104", "464500")
# chem()
# english()

# physics()

