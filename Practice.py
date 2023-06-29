from datetime import datetime

name = input("Ingrese su nombre: ")

def get_greeting():
    
    time = datetime.now().strftime("%H:%M")
    time = int(time.replace(':',''))

    if time < 1200:
        return 'Buenos días'
    elif 1200 <= time < 1800:
        return 'Buenas tardes'
    else: 
        return 'Buenas noches'
    

#greeting = get_greeting()
    



#print(f'Hola {name}! {greeting}!')