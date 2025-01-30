# import requests
# from bs4 import BeautifulSoup

# response=requests.get('https://kbtrip.in/')
# # print(response.json)
# soup = BeautifulSoup(response.content, 'html.parser')
# # print(soup.prettify())
# s = soup.find('div', class_='entry-content')
# content = soup.find_all('p')

# print(content)

import pyautogui


# moves to (519,1060) in 1 sec
pyautogui.moveTo(519, 1060, duration = 1)

# simulates a click at the present 
# mouse position 
pyautogui.click()

# moves to (1717,352) in 1 sec
pyautogui.moveTo(1717, 352, duration = 1) 

# simulates a click at the present 
# mouse position
pyautogui.click()