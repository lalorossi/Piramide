class Juego:
	def __init__(self):
		self._Tablero=Tablero()

	def IniciarJuego(self):
		pass


class Tablero:
	def __init__(self):
		self._Piramide=[]
		for filas in range(6):
			print ("Ingrese los valores de izquierda a derecha de la fila %d" %(fila+1))
			print ("O ingrese un espacio para dejarlo vacio")
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


class Celda:
	def __init__ (self):
		Valor=input("Ingrese el valor de la celda")
		if Valor == ' ':
			Valor=0

		self._Valor=Valor


	NuevoJuego=Juego()