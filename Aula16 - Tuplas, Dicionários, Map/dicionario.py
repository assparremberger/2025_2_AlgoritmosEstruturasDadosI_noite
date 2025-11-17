carro01 = { "modelo" : "Uno" , "ano" : 2004 }
carro02 = { "modelo" : "Doblo" , "ano" : 2006 }
carro03 = { "modelo" : "Uno Way" , "ano" : 2015 }

frota = carro01 , carro02

print( carro01 )

print( frota )

#frota[0] = carro03

carro01["modelo"] = "Jeep"

print( frota )