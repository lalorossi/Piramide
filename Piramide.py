#La clase Juego es la base del programa. A partir de ella se comienza a resolver la piramide
class Juego:

	#Al iniciar el juego, se crea una piramide nueva
	def __init__(self):
		self._Tablero=Tablero()

	def IniciarJuego(self):
		pass

#La clase Tablero Es solamente la piramide, tomada como un array de los numeros que contiene
class Tablero:

	#Al iniciar la Piramide, creamos todas sus celdas
	#Se toma al 0 como celda vacia (Ya que no se puede ingresar un 0 en la piramide)
	def __init__(self):
		self._Piramide=[]
		for filas in range(6):
			print ("Ingrese los valores de izquierda a derecha de la fila %d" %(fila+1))
			print ("O ingrese un 0 para dejar la celda vacia")
			for posicion in range(6-fila):
				celda=Celda()
				self._Piramide.append(celda)

	def MostrarPiramide(self):
		pos=0
		numeros=0
		for i in range(6):
			numeros=pos+6-i
			print self._Piramide[pos:numeros]
			pos+=numeros

#La clase celda son los elementos dentro del tablero, cada una con su valor
class Celda:

	#Al crear una celda, esta nos pregunta su valor
	def __init__ (self):
		Valor=input("Ingrese el valor de la celda")
		if Valor == ' ':
			Valor=0

		self._Valor=Valor


NuevoJuego=Juego()