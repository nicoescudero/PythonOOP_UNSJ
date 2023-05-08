## Contexto
El Consorcio SIU, encargado del desarrollo de las soluciones informáticas que utilizan las
instituciones universitarias del país lo contrata a usted para el desarrollo de un módulo que
procese los archivos: **‘alumnos.csv’** y **‘materiasAprobadas.csv’**.

El archivo **‘alumnos.csv’** almacena la información de los alumnos inscriptos en las carreras de la
universidad. La estructura del mismo es la siguiente: dni, apellido, nombre, carrera, año de la
carrera que cursa.

El archivo **‘materiasAprobadas.csv’** almacena información de las materias que los alumnos
inscriptos en una carrera, han aprobado en los últimos tres meses, por examen, equivalencia o
promoción. La estructura de dicho archivo es la siguiente: dni, nombre de materia, fecha, nota,
aprobación (‘E’ – Examen, ‘X’ – Equivalencia, ‘P’ – Promoción).

**Los archivos no presentan ningún orden en particular.**

El módulo que se le solicita debe permitir.

1. Cargar los datos de los alumnos en un Manejador de Alumnos, implementado usando un
arreglo Numpy.
2. Cargar los datos de las materias aprobadas en un Manejador de Materias, implementado
usando una lista Python.
3. A través de un menú de opciones llevar a cabo las siguientes funcionalidades:

   **a.** Leer por teclado el número de dni de un alumno, e informar su promedio con
    aplazos y sin aplazos.
    
    **b.** Leer por teclado el nombre de una materia, e informar los estudiantes que la
    aprobaron en forma promocional, con nota mayor o igual que 7. El informe debe
    tener el siguiente formato:

    DNI     Apellido y nombre   Fecha       Nota    Año que cursa
    
    xxxxxxx xxxxxxxxxxxxxxxxxxx xx/xx/xxxx  xx.xx   xxxxxxx

    **c.** Obtener un listado de alumnos ordenado: por el año que cursan y alfabéticamente
    por apellido y nombre (ambos de menor a mayor).
    **Regla de negocio: el analista le solicita que para resolver esta opción
    sobrecargue el operador (<) en la clase que corresponda.**