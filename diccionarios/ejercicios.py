#Ejercicio: Escriba una función en Python que reproduzca lo siguiente: 𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2  Valor para X=3 y valor para Y=5
def f(x, y):
    return x*2 + y*2  # Definición de una función llamada 'f' que toma dos argumentos, 'x' e 'y', y retorna el resultado de la expresión x*2 + y*2.

x = 3  # Asignación de valor 3 a la variable 'x'.
y = 5  # Asignación de valor 5 a la variable 'y'.
result = f(x, y)  # Llamada a la función 'f' con los valores de 'x' e 'y' como argumentos, y se asigna el resultado a la variable 'result'.
print(result)  


#Ejercicio: Tomé el presente ejercicio,  y pasé a la función la lista con los días de la semana restantes

def diccionario(arg, resultado={}):

#Esta función toma un argumento `arg` y un diccionario `resultado`.Agrega `arg` al diccionario y luego imprime el diccionario actualizado.

    resultado[arg] = arg
    print(resultado)

diasSemana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']

for dia in diasSemana:
    diccionario(dia)
