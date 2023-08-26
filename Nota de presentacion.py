"""
Calculo de la nota de presentación
Desarrollo fue mas general ya que funciona para n notas no esta limitada solo para 3.
"""
# Mensaje de bienvenida.
print ("\n************************************")
print ("*                                  *")
print ("* Bienvenido al calculo de tu nota *")
print ("*                                  *")
print ("************************************\n")

# Recepcion de datos por la consola.
notas_lab = input ("Ingresa las notas de Laboratorio separadas por un espacio y los decimales separados por '.':\n")
notas_tar = input ("Ingresa las notas de las Tareas separadas por un espacio y los decimales separados por '.':\n")
notas_sol = input ("Ingresa las notas de Solemnes separadas por un espacio y los decimales separados por '.':\n")

# Separacion de los elementos ingresados por el usuario.
cadenas_notas_lab = notas_lab.split( )
cadenas_notas_tar = notas_tar.split( )
cadenas_notas_sol = notas_sol.split( )

# Creacion de variables y asignacion de valor inicial.
suma_lab = 0
num_not_lab = 0
suma_tar = 0
num_not_tar = 0
suma_sol = 0
solemne = 0

# Mediante un ciclo para transformaremos los elementos, los sumaremos y los contaremos.
for cadena in cadenas_notas_lab:
    nota_lab = float(cadena)
    suma_lab = suma_lab + nota_lab
    num_not_lab = num_not_lab + 1

# Calculamos el promedio de las notas de laboratorio.
promedio_lab = suma_lab / num_not_lab

# Mediante un ciclo para transformaremos los elementos, los sumaremos y los contaremos.
for cadena in cadenas_notas_tar:
    nota_tar = float(cadena)
    suma_tar = suma_tar + nota_tar
    num_not_tar = num_not_tar + 1

# Calculamos el promedio de las notas de tareas en Clase.
promedio_tar = suma_tar / num_not_tar

# Mediante un ciclo para transformaremos los elementos, los sumaremos y los contaremos.
for cadena in cadenas_notas_sol:

    # MODIFICACION 1:
    # Las siguientes dos líneas de código se implementaron adicional ya que notas solemnes constituye un
    # 70% de la nota final (según nuestro problema son 35% de cada una) como dijimos que es
    # programa general pongámonos en el caso de que hay 3 o mas notas solemnes pasaremos el
    # umbral de 100% en la nota final entonces con las siguientes dos líneas demarcadas calcularemos el
    # porcentaje que constituye cada nota solemne.
    # 1)    Con la función (len) veremos cuantos elementos tenemos en variable cadenas_notas_sol
    # 2)    Después calcularemos que porcentaje vale cada nota solemne din un total de 70% 
    #---------------------------------------------
    numero_notas = int(len(cadenas_notas_sol)) # |
    procentaje = 0.70 / numero_notas           # |
    #---------------------------------------------

    nota_sol = float(cadena)
    solemne = nota_sol*procentaje
    suma_sol = suma_sol + solemne

# En esta línea de código calcularemos la nota final ya que sabemos que el promedio de las notas de
# laboratorio constituye un 15% de la nota final, promedio de las notas de tareas en clase también
# son un 15% de la nota final, y finalmente cada una de las notas solemnes (según el problema
# presentado constituye 35% cada una), si hablamos de un programa sin limitaciones para n notas
# sería los (70% dividido a número de notas) para complementar el 100%.
nota = (promedio_lab * 0.15) + (promedio_tar * 0.15) + suma_sol

# Por lo último se imprime en pantalla los resultados (nota) que correspondería al porcentaje por
# cada tipo de nota. Y finalmente se imprime la nota de presentación y agradecimientos.
print ("--------------------------------------------------------------------------")
print (f"Los 15% que constituyen las notas de tareas en Laboratorio son: '{(promedio_lab*0.15):.2f}'\n")
print (f"Los 15% que constituyen las notas de tareas en Clase son: '{(promedio_tar*0.15):.2f}'\n")
print (f"Los 70% que constituyen las nota Solemnes son: '{suma_sol:.2f}'")
print ("--------------------------------------------------------------------------\n")
print (f"Tu nota de Presentacion es: '{nota:.1f}'\n")
print (f"Gracias por calcular la nota final con nosotros.\n")
