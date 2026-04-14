#Ejercicio 1
# # print("hola mundo!!!")

#Ejercicio 2
# #print("Hola, me llamo Paola y estoy aprendiendo Python") #esto solo muestra los resultados en pantalla

#Ejercicio 3
# nombre="Lucía"
# edad=28
# altura=1.68
# le_gusta_python=True

# print("Hola, soy ", nombre, "tengo ", edad, "años y mido", altura, "m.") 

# print(f"Hola soy {nombre}. Tengo {edad} años y mido {altura} m.") 

# frase=f"Hola soy {nombre}. Tengo {edad} años y mido {altura} m."
# print(frase)


#Ejecicio 4
# nombre="Ana"
# edad=25
# me_gusta_pizza=True

# frase=f"Hola, soy {nombre} y tengo {edad} años y ¿me gusta la pizza? {me_gusta_pizza}"
# print(frase)


#Ejercicio 4
#Reto:  crear un script que calcule tu "Puntaje de Energía" del día

nombre = input("Como te llamas? ")
cafes_tomado = input("Cuantos cafés te has tomado hoy? ")
horas_sueno = input("Cuantas horas has dormido hoy? ")

energia= int(cafes_tomado) + int(horas_sueno)

print(f"Hola {nombre}, tu energía hoy es de {energia} puntos.")