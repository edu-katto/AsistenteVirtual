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

    for i in [0, 1]:
        press('TAB')

    time.sleep(2)
    press('ENTER')

    time.sleep(2)
    driver.quit()

def menu():
    os.system('cls')
    print('Selecionar una opcion')
    print('\topcion 1 usar el computador')
    print('\topcion 2 redes sociales')
    print('\topcion 3 salir')

while True:
    menu()

    opcionMenu = input("Inserta un numero valor >>")

    if opcionMenu == '1':
        os.system('cls')
        print('Usar el computador')
        print('\topcion 1 trabajar')
        print('\topcion 2 entretenimiento')
        print('\topcion 3 jugar')

        opcionComputador = input("Inserta un numero valor >>")

        if opcionComputador == "1":
            listaProgramas = []
            listaProgramas = os.listdir(ruta + "\programas")

            print("¿Qué programa decea abrir?")
            print(listaProgramas)
            programaSeleccionada = input('>>')

            os.system(ruta + "\programas\\" + programaSeleccionada)

        elif opcionComputador == "2":
            listaMusica = []
            listaMusica = os.listdir(ruta + "\entretenimiento")

            print("¿Qué archivo decea reproducir?")
            print(listaMusica)
            musicaSeleccionada = input('>>')

            os.system(ruta + "\entretenimiento\\" + musicaSeleccionada)

        elif opcionComputador == "3":
            listaJuegos = []
            listaJuegos = os.listdir(ruta + "\juegos")

            print("¿Qué juego quiere abrir?")
            print(listaJuegos)
            juegoSeleccionado = input('>>')

            os.system(ruta + "\juegos\\" + juegoSeleccionado)

        else:
            print("Opcion Invalida")
            input("\npulsa una tecla para continuar >>")

    elif opcionMenu == "2":
        redSocial()

    elif opcionMenu == "3":
        break

    else:
        input("\npulsa una tecla para continuar")
