from perro import Perro

perro1  = Perro("Canis lupus familiaris", 5, 80, "ADN12345", "Omnívoro", "Doméstico", True, "Esqueleto óseo", "Corto", 2, "Labrador", 10)

perro1.ladrar()
print(perro1.energia)
perro1.desplazarse()
print(perro1.energia)

perro1.energia = 7

perro1.desplazarse()

print(perro1.energia)