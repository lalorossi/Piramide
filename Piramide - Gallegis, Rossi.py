#La clase Juego es la base del programa. A partir de ella se comienza a resolver la piramide
class Juego:

	#Al iniciar el juego, se crea una piramide nueva
	def __init__(self):
		self.Tablero=Tablero()

	def IniciarJuego(self):
		  self.Tablero.ResolverTablero()

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
				celda=Celda(filas, posicion)
				self.Piramide.append(celda)

	#Funcion para establecer relaciones entre las celdas
	#Se toma a PADRE como la celda superior derecha, y MADRE a la superior izquierda
	#HERMANO a la celda de la derecha y HERMANA a la de la izquierda
	#HIJO a la celda inferior derecha e HIJA a la inferior izquierda
	def EstablecerRelaciones(self):
		self._PosArray=0

		for fila in range (6):

			for celda in range (6-fila):

				#La fila superior solo tiene "parientes" hijos
				if fila!=5:

					if celda!=(6-fila-1) :
						#Si NO es la celda de la derecha
						self.Piramide[self._PosArray].EstablecerPadre(self.Piramide[self._PosArray+(6-fila)])
						self.Piramide[self._PosArray].EstablecerHermano(self.Piramide[self._PosArray+1])



					if celda!=(0):
						#Si NO es la celda de la izquierda
						self.Piramide[self._PosArray].EstablecerMadre(self.Piramide[self._PosArray+((6-fila)-1)])
						self.Piramide[self._PosArray].EstablecerHermana(self.Piramide[self._PosArray-1])


				if fila!=0:
					#Son las celdas que tienen HIJOS (Todas menos las de la base)
						self.Piramide[self._PosArray].EstablecerHija(self.Piramide[self._PosArray-(7-fila)])
						self.Piramide[self._PosArray].EstablecerHijo(self.Piramide[self._PosArray-(6-fila)])

				self._PosArray+=1

	def ResolverTablero(self):
		self.Posicion=0
		Cambio=True
		while (Cambio):
			Cambio=False
			for i in range (21):
				self.Posicion+=1
				if self.Piramide[i].getEstado() == False:
					self.Piramide[i].ResolverCelda(self.Piramide[self.Posicion])

					if self.Piramide[i].getEstado():
						Cambio=True
		else:
			print ("Ganaste??")
			self.MostrarPiramide()


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
		print (self._ArrayDeValores)

		#muestro los primeros 6 valores, luego los siguientes 5, etc.
		for i in range(6):
			numeros=pos+6-i
			print (self._ArrayDeValores[pos:numeros])
			pos+=(6-i)
	

#La clase celda son los elementos dentro del tablero, cada una con su valor
class Celda:

	#Al crear una celda, esta nos pregunta su valor
	def __init__ (self, fila, posicion):
		self.Fila=fila
		self.Posicion=posicion
		Valor=input("Ingrese el valor de la celda: ")
	
		self._Valor=int(Valor)

		if self._Valor==0:
			self._Resuelto=False
		else:
			self._Resuelto=True


	def getValor(self):
		return self._Valor

	def getEstado(self):
		return self._Resuelto

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


	#Funcion que trata de ponerle una valor a la celda, comunicandose con sus parientes
	#Esta funcion solo se llama cuando self._Resuelto es False (La celda no está resuelta)
	def ResolverCelda(self, Invocador):
		#Hay 2 maneras de resolver una celda:
		#1- Tiene un padre y un hermano del mismo "genero" resuelto
		#2- Tiene los 2 hijos resueltos

		#1- No se aplica a la celda superior
		if (self.Fila != 5):

			#No se aplica a las celdas del costado derecho
			if self.Posicion != (6-self.Fila-1):
				if self.Padre.getEstado() and self.Hermano.getEstado():
					self._Valor	=self.Padre.getValor() - self.Hermano.getValor()
					self._Resuelto=True



			#1- No se aplica a las celdas del costado izquierdo
			if (self.Posicion != 0):
				if self.Madre.getEstado() and self.Hermana.getEstado():
					self._Valor	=self.Madre.getValor() - self.Hermana.getValor()
					self._Resuelto=True



		#2- No se aplica a las celdas de la base
		if self.Fila != 0:
			if self.Hijo.getEstado() and self.Hija.getEstado():
				self._Valor =self.Hija.getValor() + self.Hijo.getValor()
				self._Resuelto=True


		#Una vez que trato de resolverse, trata de resolver a sus parientes
		if (self.Fila != 5):
			if self.Posicion != (6-self.Fila-1):
				if self.Padre.getEstado()==False and Invocador != self.Padre:
					self.Padre.ResolverCelda(self)
				if self.Hermano.getEstado()==False and Invocador != self.Hermano:
					self.Hermano.ResolverCelda(self)

			#1- No se aplica a las celdas del costado izquierdo
			if (self.Posicion != 0):

				if self.Madre.getEstado()==False and Invocador != self.Madre:
					self.Madre.ResolverCelda(self)

				if self.Hermana.getEstado()==False and Invocador != self.Hermana:
					self.Hermana.ResolverCelda(self)


		#2- No se aplica a las celdas de la base
		if self.Fila != 0:
			if self.Hijo.getEstado()==False and Invocador != self.Hijo:
				self.Hijo.ResolverCelda(self)

			if self.Hija.getEstado()==False and Invocador != self.Hija:
				self.Hija.ResolverCelda(self)




NuevoJuego=Juego()

NuevoJuego.Tablero.EstablecerRelaciones()

NuevoJuego.IniciarJuego()

"""
El programa tiene un error:
Si dos celdas contiguas estan vacias, ambas trataran de resolverse mutuamente
Generando un ciclo infinito
NO SÉ CÓMO ARREGLARLO
"""
