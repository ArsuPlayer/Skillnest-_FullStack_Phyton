#Estructura if - elif - else
n1 = int(input("Ingresar primer número: "))
n2 = int(input("Ingresar segundo número: "))
n3 = int(input("Ingresar tercer número: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
    if n2 <= n3:
        menor = n2
    else:
        menor = n3
elif n2 >= n1 and n2 >= n3:
    mayor = n2
    if n1 <= n3:
        menor = n1
    else:
        menor = n3
else: 
    mayor = n3
if n1 <= n2:
    menor = n1
else:
    menor = n2
    if n1 <= n2:
        menor = n1
    else:
        menor = n2
        print(f"El mayor es {mayor} y el menos es {menor}")