import pyautogui
import time

# Configuración inicial
pyautogui.FAILSAFE = True  # Hacer que el bot detenga la ejecución si mueve el mouse a la esquina superior izquierda
sum  = 93

# Ciclo principal del bot
time.sleep(10)
while True:
    # Escribir el texto y presionar Enter

    pyautogui.typewrite(f" Sumo uno a uno hasta que conseguir llamar la atencion de Bromas, vamos por: {sum}")
    pyautogui.click()
    pyautogui.press('enter')

    # Actualizar los valores de a y b para obtener el siguiente número de la secuencia de Fibonacci
    sum += 1

    # Esperar un tiempo antes de repetir el ciclo
    time.sleep(18)