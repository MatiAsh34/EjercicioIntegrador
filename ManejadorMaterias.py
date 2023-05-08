import csv
from ClaseMaterias import *

class ManejadorMateria():
	def __init__(self):
		self.__lista = []
        
	def Cargar(self):
		archivo = open('materiasAprobadas.csv')
		reader = csv.reader(archivo,delimiter=';')
		for fila in reader:
			materia = Materia(int(fila[0]),fila[1],fila[2],float(fila[3]),fila[4])
			self.__lista.append(materia)	
            
	def Muestra(self):
		for i in range(len(self.__lista)):
 			print("Materia:",i+1)
 			print(self.__lista[i].Mostrar()) 
             
        
	def Informar(self,i):
		print("En la materia: ",self.__lista[i].getMateria()," tiene un promedio de: ",self.__lista[i].getNota())
          
	def BuscaDNI(self,dni):
		i = 0
		while i < len(self.__lista):
			if self.__lista[i].getDNI() == dni:
				ManejadorMateria.Informar(self,i)
			i += 1  
            
	def BuscaMateria(self,materia,Manejador_Alumno):
		i = 0
		while i < len(self.__lista):
			if self.__lista[i].getMateria() == materia:
				Manejador_Alumno.BuscoAlumno(self.__lista[i].getDNI(),self.__lista[i].getNota(),self.__lista[i].getFecha())
			i += 1