import numpy as np
import csv
from ClaseAlumnos import *

class ManejadorAlumno():
	__cantidad = 0 #elementos cargados en el arreglo
	__dimension = 0 #cuantas componentes tiene el arreglo
	__incremento = 8 #en cuentas unidades se va incrementar el arreglo

	def __init__(self,tamaño):
		self.__dimension = tamaño
		self.__arreglo = np.empty(tamaño,dtype=Alumno)

	def Cargar(self,alumno):
		if self.__cantidad == self.__dimension:
			self.__dimension += self.__incremento
			self.__arreglo.resize(self.__dimension)

		self.__arreglo[self.__cantidad] = alumno
		self.__cantidad += 1

	def CrearAlumno(self):
		archivo = open('alumnos.csv')
		reader = csv.reader(archivo,delimiter=';')

		for fila in reader:
			alumno = Alumno(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
			ManejadorAlumno.Cargar(self,alumno)
			
	def Muestra(self):
		for i in range(8):
			'''print("Alumno:", i+1)
			print(self.__arreglo[i].Mostrar())'''
			print(self.__arreglo[i].getDNI_Alumno())
            
	def Informe(self,i,nota,fecha):
		print(self.__arreglo[i].Mostrar(),nota,fecha,self.__arreglo[i].getAño())
            
	def BuscoAlumno(self,dni,nota,fecha):
		i = 0
		while i < 8:
			if self.__arreglo[i].getDNI_Alumno() == dni:
				ManejadorAlumno.Informe(self,i,nota,fecha)
			i += 1
            
	def Mostrar_Listado_Ordenado(self,listado_ordenado):
		for alumno in listado_ordenado:
			alumno.Muestra_Listado()    
    
	def Ordenar_Listado(self):
		listado_ordenado = sorted(self.__arreglo)
		self.Mostrar_Listado_Ordenado(listado_ordenado)