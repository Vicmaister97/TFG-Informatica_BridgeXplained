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
		self.playedCards = []
		self.knownCards = []

		logging.debug(Sentences.CREATE_PLAYER(self.name))


	### BASIC METHODS ###
	def __str__(self):
		try:
			toString = Sentences.PLAYER_INFO_S(self.name) \
			+ self.stringKnownCards()
			#+ self.stringKnownCards()() + self.stringHC()
			return toString
		except AttributeError:
			return Sentences.NO_INFO_PLAYER(self.name)


	def deletePlayer(self):
		self.cards = []
		self.playedCards = []
		self.knownCards = []

		logging.debug(Sentences.DEL_PLAYER(self.name))
		del self



	### ATRIBUTES/INFO FOR RULES ###
	def setCard(self, card, suit):
		self.cards.append((card, suit))
		self.knownCards.append((card, suit))


	def setPlayedCard(self, card, suit):
		self.playedCards.append((card, suit))
		if (card, suit) not in self.knownCards:
			self.knownCards.append((card, suit))

	def getCardsToPlay(self):
		toPlayCards = self.knownCards
		try:
			for card, suit in self.playedCards:
				toPlayCards.remove((card, suit))
		except ValueError as e:
			pass
		return toPlayCards


	def stringKnownCards(self):
		if len(self.knownCards) == 0:
			return "Any known card."
		return Sentences.PLAYER_CARDS_S(self.knownCards)


	def stringCardsToPlay(self):
		cardsToPlay = self.getCardsToPlay()
		if len(cardsToPlay) == 0:
			return "Any (known) card to play."
		return Sentences.PLAYER_CARDSTOPLAY_S(cardsToPlay)

	"""

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
		return Sentences.PLAYER_HC_S(self.cards)