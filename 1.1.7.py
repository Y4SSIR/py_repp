import math

grad=float(input("Skriv din grad: "))
decimaler=int(input("Ange antal decimaler du vil ha: "))
radie=round(math.radians(grad), decimaler)
print("Din radie är", radie)