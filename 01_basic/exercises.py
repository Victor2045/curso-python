###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Victor Presilla", "Upata", sep="\n")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(f"La variable a es de tipo: {type(a)}")
print(f"La variable b es de tipo: {type(b)}")
print(f"La variable c es de tipo: {type(c)}")
print(f"La variable d es de tipo: {type(d)}")
print(f"La variable e es de tipo: {type(e)}")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
numero = 3.99

print(int(cadena))
print(float(cadena))
print(int(numero))
print("La funcion int() se encarga de eliminar los digitos despues del punto, no como la funcion round() que se encarga de redondear un numero determinado por sus decimales")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = "Victor"
edad = 25
altura = 1.83

print(f"Hola! Me llamo {name} y tengo {edad} años, mido {altura} metros")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

numero = round(3,14159)

numero = int(numero / 2)

print(f"El resultado es: {numero}")