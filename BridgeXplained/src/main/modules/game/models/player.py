from helpers.sentences import *
from helpers.exceptions import *
import logging


#######
## Crear SETTER y atributo en el init segun config!!!
## Asi, podemos poner nueva info/atributos de un jugador
##	SIN TOCAR ESTE FICHERO!

class Player:


	def __init__(self, name):
		self.name = name
		self.HC = 0
		self.cards = []
		logging.debug(Sentences.CREATE_PLAYER(self.name))


	### BASIC METHODS ###
	def __str__(self):
		try:
			toString = Sentences.PLAYER_INFO_S(self.name) \
			+ self.stringCards()
			#+ self.stringCards() + self.stringHC()
			return toString
		except AttributeError:
			return Sentences.NO_INFO_PLAYER(self.name)


	def deletePlayer(self):
		self.cards = []
		logging.debug(Sentences.DEL_PLAYER(self.name))
		del self



	### ATRIBUTES/INFO FOR RULES ###
	def setCard(self, card, suit):
		self.cards.append((card, suit))

	def stringCards(self):
		return Sentences.PLAYER_CARDS_S(self.cards)

	def checkIfAbleToPlay(self, cardCheck, suitCheck):
		for card, suit in self.cards:
			if card == cardCheck:
				if suit == suitCheck:
					return

		raise PlayerError(Sentences.MISSING_CARD(self.name, cardCheck, suitCheck))

	"""
	def setHC(self, HC):
		self.HC = HC

	def stringHC(self):
		return Sentences.PLAYER_HC_S(self.knownCards)
	"""