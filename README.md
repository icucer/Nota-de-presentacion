# Crear un programa que calcule la nota de prsentacion.
##  Supóngamos que un ramo tiene las siguientes evaluaciones:
## - 3 tareas en laboratorio, estas valen un 15% del curso.
## - 3 tareas en clase, que valen un 15% del curso.
## - 2 notas solemnes, cada una un 35%.
***
## A continuacion dejare un ejemplo de calculo:
***
Lab 1 = 4.5\
Lab 2 = 7.0\
Lab 3 = 5.5\
Tarea 1 = 6.2\
Tarea 2 = 5.0\
Tarea 3 = 2.1\
Solemne 1 = 1.8\
Solemne 2 = 5.4\
Nota de presentación = (Prom Lab)\*0,15 + (Prom Tareas)\*0.15 + Sol1\*0.35 + Sol2\*0.35\
Prom Lab = 5.7\
Prom Tarea = 4.4\
Nota de presentación = 5.7\*0.15 + 4.4\*0.15 + 1.8\*0.35 + 5.4\*0.35\
Nota de presentación = 4.0

***
## A tomar en cuenta:
- Complicamos un poco la tarella calculando 'nota de presentacion para **n notas** de cada categoria' esto condicionara los procentajes de las notas solemnes &#x1F440;
.