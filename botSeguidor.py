import pyautogui
import cv2
import keyboard
import schedule
import time


EARNFREEPOINTS=(1319,234)
FOLLOW=(1093,534)
LIKE=(1140,415)
VOLTAR=(885,89)



# Função que contém o código a ser executado
def executar_codigo1():
    pyautogui.sleep(2)
    pyautogui.click(EARNFREEPOINTS)
    pyautogui.sleep(2)
    pyautogui.click(FOLLOW)
    pyautogui.sleep(2)
    pyautogui.click(VOLTAR)
    pyautogui.sleep(2)
    pyautogui.click(EARNFREEPOINTS)
    pyautogui.sleep(2)
    pyautogui.click(LIKE)
    pyautogui.sleep(2)
    pyautogui.click(VOLTAR)

    imagem = 'img/FollowClick.png'

    voltar = (849, 55, 66, 66)

    limiteA = pyautogui.locateOnScreen('img/limite.png', region=(888, 288, 488, 500))

    while keyboard.is_pressed('c') == False:
        sc = pyautogui.screenshot(region=(1000, 633, 400, 110))
        whidht, heidht = sc.size
        sc.save('img/FollowClick.png')

        for x in range(0, whidht, 5):
            for y in range(0, heidht, 5):
                r, g, b = sc.getpixel((x, y))

                if r == 255 and g == 64 and b == 129:
                    pyautogui.click(1000 + x, 633 + y)

def executar_codigo2():
    pyautogui.sleep(2)
    pyautogui.click(EARNFREEPOINTS)
    pyautogui.sleep(2)
    pyautogui.click(FOLLOW)
    pyautogui.sleep(2)
    pyautogui.click(VOLTAR)
    pyautogui.sleep(2)
    pyautogui.click(EARNFREEPOINTS)
    pyautogui.sleep(2)
    pyautogui.click(LIKE)
    pyautogui.sleep(2)
    pyautogui.click(VOLTAR)

    imagem = 'img/FollowClick.png'

    voltar = (849, 55, 66, 66)

    limiteA = pyautogui.locateOnScreen('img/limite.png', region=(888, 288, 488, 500))

    while keyboard.is_pressed('c') == False:
        sc = pyautogui.screenshot(region=(1000, 633, 400, 110))
        whidht, heidht = sc.size
        sc.save('img/FollowClick.png')

        for x in range(0, whidht, 5):
            for y in range(0, heidht, 5):
                r, g, b = sc.getpixel((x, y))

                if r == 255 and g == 64 and b == 129:
                    pyautogui.click(1000 + x, 633 + y)



horarios = [
    "01:10", "02:10", "03:10", "04:10", "05:10", "06:10", "07:10", "08:10", "09:10", "10:10",
    "11:10", "12:10", "13:10", "14:10", "15:10", "16:10", "17:10", "18:10", "19:10", "20:10",
    "21:10", "22:10", "23:10", "00:10"
]

for horario in horarios:
    schedule.every().day.at(horario).do(executar_codigo1)

    horarios = [
    "01:35", "02:35", "03:35", "04:35", "05:35", "06:35", "07:35", "08:35", "09:35", "10:10",
    "11:35", "12:35", "13:35", "14:35", "15:35", "16:35", "17:35", "18:35", "19:35", "20:10",
    "21:35", "22:35", "23:35", "00:35"
]

for horario in horarios:
    schedule.every().day.at(horario).do(executar_codigo2)

# Loop principal
while True:
    schedule.run_pending()
    time.sleep(1)
