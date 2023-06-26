from datetime import datetime

name = input("Ingrese su numbre: ")
time = str(datetime.now().strftime("%H:%M"))

#actual_time = (if time )

print(f'Hola {name}! buena {time}')