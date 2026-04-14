# Reto de Práctica

# Escribe un código que pregunte al usuario:

# 1. Su **nombre**.
# 2. Su **comida favorita**.
# 3. El **precio** de esa comida (aproximado).

# Luego, imprime un solo mensaje usando **f-strings** que diga:

# *"Hola {nombre}, me encanta el/la {comida} y veo que cuesta {precio} euros."*

nombre = input("Cual es tu nombre? ")
comida = input("Cual es tu comida favorita? ")
precio = input("Cual es el precio aproximado? ")

print(f"Hola {nombre}, me encanta el/la {comida} y veo que cuesta {precio} euros.")