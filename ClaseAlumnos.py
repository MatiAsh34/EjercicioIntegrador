class Alumno():
	def __init__(self,dni,apellido,nombre,carrera,año):
		self.__dni_alumno = dni
		self.__apellido = apellido
		self.__nombre = nombre
		self.__carrera = carrera
		self.__año = año
        
	def Mostrar(self):
		return "%s %s %s" % (self.__dni_alumno,self.__apellido,self.__nombre) 
    
	def Muestra_Listado(self):
		print (self.__año)
		print (self.__apellido)
		print (self.__nombre)
    
	def getDNI_Alumno(self):
		return self.__dni_alumno
    
	def getAño(self):
		return self.__año
    
	def getApellido(self):
		return self.__apellido
    
	def getNombre(self):
		return self.__nombre
    
	def __lt__(self, other):
		return (self.__año, (self.__apellido + self.__nombre)) < (other.__año, (other.__apellido + other.__nombre))