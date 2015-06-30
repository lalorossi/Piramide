#La clase Juego es la base del programa. A partir de ella se comienza a resolver la piramide
class Juego:

	#Al iniciar el juego, se crea una piramide nueva
	def __init__(self):
		self.Tablero=Tablero()

	def IniciarJuego(self):
		pass

#La clase Tablero Es solamente la piramide, tomada como un array de los numeros que contiene
class Tablero:

	#Al iniciar la Piramide, creamos todas sus celdas
	#Se toma al 0 como celda vacia (Ya que no se puede ingresar un 0 en la piramide)
	def __init__(self):
		self.Piramide=[]
		print ("")
		for filas in range(6):
			print ("")
			print ("Ingrese los valores de izquierda a derecha de la fila %d" %(filas+1))
			print ("O ingrese un 0 para dejar la celda vacia")
			print ("")
			for posicion in range(6-filas):
				celda=Celda()
				self.Piramide.append(celda)

	#Funcion para establecer relaciones entre las celdas
	#Se toma a PADRE como la celda superior derecha, y MADRE a la superior izquierda
	#HERMANO a la celda de la derecha y HERMANA a la de la izquierda
	#HIJO a la celda inferior derecha e HIJA a la inferior izquierda
	def EstablecerRelaciones(self):
		self._PosArray=0

		for fila in range (6):

			for celda in range (6-fila):

				print ("FILA: %d" %fila)
				print ("CELDA %d" %celda)
				print ("POS %d" %self._PosArray)
				print ("")

				#La fila superior solo tiene "parientes" hijos
				if fila!=5:

					if celda!=(6-fila-1):
						#Si NO es la celda de la derecha
						self.Piramide[self._PosArray].EstablecerPadre(self.Piramide[celda+(6-fila)])
						self.Piramide[self._PosArray].EstablecerHermano(self.Piramide[celda+1])
						#SE PUDRE TODO CUANDO ES LA PUNTA DE LA PIRAMIDE


					if celda!=(0):
						#Si NO es la celda de la izquierda
						self.Piramide[self._PosArray].EstablecerMadre(self.Piramide[celda+((6-fila)-1)])
						self.Piramide[self._PosArray].EstablecerHermana(self.Piramide[celda-1])
						#SE PUDRE TODO CUANDO ES LA PUNTA DE LA PIRAMIDE


				if fila!=0:
					#Son las celdas que tienen HIJOS (Todas menos las de la base)
						self.Piramide[self._PosArray].EstablecerHija(self.Piramide[celda-(7-fila)])
						self.Piramide[self._PosArray].EstablecerHijo(self.Piramide[celda-(6-fila)])


				self._PosArray+=1


	def MostrarFamiliares(self, Celda):
		ValorPadre=self.Piramide[Celda].Padre.getValor()
		ValorMadre=self.Piramide[Celda].Madre.getValor()
		ValorHermano=self.Piramide[Celda].Hermano.getValor()
		ValorHermana=self.Piramide[Celda].Hermana.getValor()
		ValorHijo=self.Piramide[Celda].Hijo.getValor()
		ValorHija=self.Piramide[Celda].Hija.getValor()


		print ("Padre: %d" %ValorPadre)
		print ("Madre: %d" %ValorMadre)
		print ("Hermano: %d" %ValorHermano)
		print ("Hermana: %d" %ValorHermana)
		print ("Hijo: %d" %ValorHijo)
		print ("Hija: %d" %ValorHija)

	
	def MostrarPiramide(self):
		self._ArrayDeValores=[]
		pos=0
		numeros=0

		#Agrego los valores a un array para poder mostrarlos más fácilmente
		for i in range(21):
			self._ArrayDeValores.append(self.Piramide[i].getValor())

		print ("")

		#muestro los primeros 6 valores, luego los siguientes 5, etc.
		for i in range(6):
			numeros=pos+6-i
			print (self._ArrayDeValores[pos:numeros])
			pos+=(6-i)
	

#La clase celda son los elementos dentro del tablero, cada una con su valor
class Celda:

	#Al crear una celda, esta nos pregunta su valor
	def __init__ (self):
		Valor=input("Ingrese el valor de la celda: ")
		if Valor == ' ':
			Valor=0

		self._Valor=int(Valor)

	def getValor(self):
		return self._Valor


	#Funciones para establecer la relacion de una celda con otras
	def EstablecerPadre(self, Padre):
		self.Padre=Padre

	def EstablecerMadre(self, Madre):
		self.Madre=Madre

	def EstablecerHermano(self, Hermano):
		self.Hermano=Hermano

	def EstablecerHermana(self, Hermana):
		self.Hermana=Hermana

	def EstablecerHijo(self, Hijo):
		self.Hijo=Hijo

	def EstablecerHija(self, Hija):
		self.Hija=Hija





NuevoJuego=Juego()

NuevoJuego.Tablero.MostrarPiramide()

NuevoJuego.Tablero.EstablecerRelaciones()

NuevoJuego.Tablero.MostrarFamiliares(12)