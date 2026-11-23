a = int(input("ingresa el primer numero para calcular un promedio"))
b = int(input("ingresa el segundo numero para calcular un promedio"))
c = int(input("ingresa el tercer numero para calcular un promedio"))
promedio = (a+b+c)/3
if promedio >= 3:
	print("aprobaste la materia")
elif promedio <= 3:
	print("reprobaste la materia ")