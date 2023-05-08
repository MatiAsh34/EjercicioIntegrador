from ManejadorMaterias import *
from ManejadorAlumnos import *

def Menu_Opciones(Manejador_Alumno,Manejador_Materia):
    band = False
    while band == False:
        print ("\n1- Leer por teclado el número de dni de un alumno, e informar su promedio con aplazos y sin aplazos. ")
        print ("2- Indique el nombre materia, para informar los estudiantes que la aprobaron en forma promocional")
        print ("3- Mostrar un listado de alumnos ordenado: por el año que cursan y alfabéticamente por apellido y nombre")
        print ("4- Salir")
        opcion = int(input("\nIndique codigo: "))
        
        if opcion == 1:
            dni_alumno = int(input("Ingrese el dni de un alumno: "))
            Manejador_Materia.BuscaDNI(dni_alumno)
        
        if opcion == 2:
            nombre_materia = input("Ingrese nombre de la materia: ")
            Manejador_Materia.BuscaMateria(nombre_materia,Manejador_Alumno)
        
        if opcion == 3:
            Manejador_Alumno.Ordenar_Listado()
        
        if opcion == 4:
            print("Saliendo.....")
            band = True
        
        
if __name__ == '__main__':
    Manejador_Alumno = ManejadorAlumno(8)
    Manejador_Alumno.CrearAlumno()
    #Manejador_Alumno.Muestra()
    
    Manejador_Materia = ManejadorMateria()
    Manejador_Materia.Cargar()
    #Manejador_Materia.Muestra()
    
    Menu_Opciones(Manejador_Alumno,Manejador_Materia)