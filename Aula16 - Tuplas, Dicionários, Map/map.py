def somar( valores ):
    soma = 0
    for x in valores:
        soma += x
    return soma

numeros = (1, 2, 3)  , (2.5, 0) , [10, 20, 30, 40] , [ (5 + 3) ]

result = map(  somar , numeros )
print( list(result) )