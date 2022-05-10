from helpers.sentences import *
import logging


class Player:


	def __init__(self, name):
		self.name = name
		self.HC = 0
		#self.HC = read_HC_from_conclussions(name)
		logging.debug(Sentences.CREATE_PLAYER(self.name))

	"""
	def getHC(self):
		return self.HC
	"""

	def setHC(self, HC):
		self.HC = HC
	#######
	## Crear SETTER y atributo en el init segun config!!!
	## Asi, podemos poner nueva info/atributos de un jugador
	##	SIN TOCAR ESTE FICHERO!


	def __str__(self):
		try:
			return "Jugador " + self.name + " tiene " + str(self.HC) + " Honores en corazones."
		except AttributeError:
			raise 
			return Sentences.NO_INFO_PLAYER(self.name)


	def deletePlayer(self):
		logging.debug(Sentences.DEL_PLAYER(self.name))
		del self


	#def readHCFromConclussions(player):


# python if ($player == "N"): N.setHC(int($puntos_min))