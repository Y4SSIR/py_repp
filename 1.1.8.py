import math

radie=float(input("Skriv din radie: "))
decimaler=int(input("Ange antal decimaler du vil ha: "))
grad=round(math.degrees(radie), decimaler)
print("Din grad är", grad)