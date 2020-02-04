from selenium import webdriver
from keyboard import press
import keyboard

import os
import time

os.system("pause")
os.system("cls")

ruta = os.getcwd() + "\menu"

def redSocial():
    driver = webdriver.Firefox(executable_path=r'C:\webdrivers\geckodriver.exe')

    driver.get('https://twitter.com/login')
    time.sleep(2)

    driver.find_element_by_name("session[username_or_email]").send_keys("3023084384")
    time.sleep(1)

    driver.find_element_by_name("session[password]").send_keys("moises99")
    time.sleep(1)

    driver.find_element_by_xpath("//div[@dir='auto'][contains(.,'Iniciar sesión')]").click()
    time.sleep(2)

    driver.get("https://twitter.com/messages/828818614513958912-1220748337516896256?text=")
    time.sleep(2)

    mensaje = driver.find_element_by_xpath(
        "//div[contains(@class,'public-DraftStyleDefault-block public-DraftStyleDefault-ltr')]").click()

    keyboard.write('HOLA MENSAJE AUTOMATIZADO')
