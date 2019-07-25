edad = int(input("digite su edad"))
genero = input("digite sexo, H:hombres / M:mujeres: ")

if edad>=18 and genero == "h":
   print("Hombre - usted es mayor de edad")
elif edad <=18 and genero == "h":
    print("Niño - usted es menor de edad")
if edad>=18 and genero == "m":
    print("Mujer  - usted es mayor de edad")
elif edad<=18 and genero == "m":
    print("Niña - es menor de edad")
    

