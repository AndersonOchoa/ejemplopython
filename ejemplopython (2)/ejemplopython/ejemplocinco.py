peso = float(input ("ingrese el peso: "))
altura = float(input ("ingrese la altura: "))
imc = peso /  altura ** 2




if imc<=18.0:
    print ("Peso demasiado bajo")
elif imc<=24.9:
    print ("Su peso es normal")
elif imc<=29.9:
    print ("Tiene sobrepeso")
elif imc>29.9:
    print ("Obesidad")
