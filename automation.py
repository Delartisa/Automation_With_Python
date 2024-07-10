# Automation project - Registering products

# 1. Open the browser
# 2. Write the page link
# 3. Login to your account
# 4. Register products

import pyautogui # python automation library
import time # to establish a waiting time between commands

# pyautogui.write -> write a text
# pyautogui.press -> press a key
# pyautogui.click -> click somewhere on the screen
# pyautogui.hotkey -> key combination

pyautogui.PAUSE = 0.3

# 1. Open the browser
pyautogui.press("win") # open the apps panel
pyautogui.write("opera") # select a browser
pyautogui.press("enter") # confirm

# 2. Write the page link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # page link
pyautogui.press("enter") # confirm
time.sleep(3) # safe time to load the page

# 3. Login to your account
pyautogui.click(x=913, y=385) # click on the email field on the website (assistant print(pyautogui.position()))
pyautogui.write("teste@gmail.com") # write your email
pyautogui.press("tab") # moves to the password field
pyautogui.write("1234") # write the password 
pyautogui.click(x=980, y=553) # click on the login buttom

# 4. Register products
import pandas as pd # library to read different files 

tabela = pd.read_csv("produtos.csv") # create a variable to store the data | pd import the data base called "produtos" with .csv extension

print(tabela) # show the date table in the terminal

for linha in tabela.index: # looping structure to automate product registration
    pyautogui.click(x=870, y=274) # click on the "codigo" field 


    # str to transform data into string | tabela.loc to localize the line and then the header within array 
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab") # move on to the next field 
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"] # within the table "produtos.csv", the "obs" category has empty spaces. for the program to work correctly, it is nescessary to add an if not pd.isna(NaNs locator), so if it is empty, skip the field observation, otherwise, fill it with the observation menssages
    
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter") # item registration confirmation
    pyautogui.scroll(5000) # takes the page view to the top, so that pyautogui.click workd correctly




