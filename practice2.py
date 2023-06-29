import calendar
import math

def greet(name):
    print(f'Hello {name}!')

print(greet('Santiago'))

def square(num1, num2):
    squarenum1 = num1**2
    squarenum2 = num2**2
    result = squarenum1 + squarenum2 
    print(f'The square of {num1} is {squarenum1} and for {num2} is {squarenum2}. The plus of the two results is {result}')

num1 = int(input('Enter the 1st number: '))

num2 = int(input('Enter the 2nd number: '))

    

#print(square(num1, num2))

cal = calendar.month(1887,6)
#print(cal)

result = math.sqrt(49)
#print(result)

def minimun(num1,num2):
    

    if num1 < num2:
        print(f'{num1} is less than {num2}')
    elif num1 == num2:
        print(f'{num2} and {num1} are equal')
    else:
        print(f'{num2} is less than {num1}')

num1=input('Enter the 1sr number: ')
num2=input('Enter the 2nd number: ')

result = minimun(num1,num2)
print(result)

def raining():
    input = print('is it raining? (yes or not)')
    if input == 'yes':
        print('Bring an umbrella')
    elif input == 'no':
        print("You don't need an umbrella today")
word = "Recuerda que el atajo de teclado puede variar según la configuración de tu editor o cualquier otro complemento que hayas instalado. Si el atajo predeterminado no funciona, puedes verificar la configuración de los atajos de teclado en Visual Studio Code y buscar la opción 'Toggle Line Comment' o similar para asignar o modificar un atajo personalizado."

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = 'bcdfghjklmnpqrstvwxyz'

vowel_count = 0
consonant_count = 0

for character in word.lower():
    if character in vowels:
        vowel_count += 1
    elif character in consonants:
        consonant_count += 1

print("Número de vocales:", vowel_count)
print("Número de consonantes:", consonant_count)


