import pyautogui
import cv2
import keyboard


imagem = 'img/FollowClick.png'

voltar = (849,55,66,66)

limiteA = pyautogui.locateOnScreen('img/limite.png',region=(888,288,488,500))

while keyboard.is_pressed('c')==False:
       
       
       
        sc = pyautogui.screenshot(region=(1000,633,400,110))
        whidht,heidht = sc.size
        sc.save('img/FollowClick.png')
        
        for x in range(0,whidht,5):
                for y in range(0,heidht,5):
                        r,g,b = sc.getpixel((x,y))

                        if r == 255 and g == 64 and  b == 129:
                                pyautogui.click(1000+x,633+y)
                      
                                    