carros = "Uno", "Doblo", "Jeep", "Pulse"

print( carros )
print( carros[2] )
print( carros[-2:] )
print( carros[1:] )
print( carros[1:-1] )

def calcular(x, y):
    return x+y , x-y , x*y , x/y

resultado = calcular( 25 , 5 )
print( resultado[1:3] )

a, b, c, d = resultado
print("Soma: " , a )
print("Subtração: " , b )
print("Multiplicação: " , c )
print("Divisão: " , d )
#resultado[0] = 10
print(resultado)

x = 5
y = 10

class Numero:
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return self.valor

valores = x , y
#valores[0] = 8
print(valores)
x = 8
print(valores)

p = Numero( 2 )
q = Numero( 3 )
numeros = p , q
print( numeros )

