import pyautogui
import time

time.sleep(5) # para posicionar o mouse
print(pyautogui.position()) # oferece a posicao da tela no prompt

pyautogui.scroll(1000) # numero positivo - scroll pra cima | numero negativo - scroll pra baixo
