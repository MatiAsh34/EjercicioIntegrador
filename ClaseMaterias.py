class Materia():
	def __init__(self,dni,nombre_materia,fecha,nota,aprobacion):
		self.__dni = dni
		self.__nombre_materia = nombre_materia
		self.__fecha = fecha
		self.__nota = nota
		self.__aprobacion = aprobacion
        
	def getDNI(self):
		return self.__dni
    
	def getNota(self):
		return self.__nota
    
	def getMateria(self):
		return self.__nombre_materia
    
	def getFecha(self):
		return self.__fecha
    	
	def Mostrar(self):
		return "%s %s %s %s %s" % (self.__dni,self.__nombre_materia,self.__fecha,self.__nota,self.__aprobacion)
