from helpers.sentences import *
import logging


class Team:


	def __init__(self, name):

		self.name = name
		self.HC = 0
		self.players = []
		self.cards = []
		self.playedCards = []
		self.knownCards = []

		logging.debug(Sentences.CREATE_TEAM(self.name))


	### BASIC METHODS ###
	def addPlayer(self, player):
		self.players.append(player)

	def __str__(self):
		try:
			toString = Sentences.TEAM_INFO_S(self.name) \
			+ self.stringKnownCards()
			#+ self.stringCards() + self.stringHC
			toString += "\n\n\tJUGADORES: \n"
			for player in self.players:
				toString += "\n\t" + str(player)
			return toString
		except AttributeError:
			return Sentences.NO_INFO_TEAM(self.name)


	def deleteTeam(self):
		self.players = []
		self.cards = []
		logging.debug(Sentences.DEL_TEAM(self.name))
		del self



	### ATRIBUTES/INFO FOR RULES ###
	def updateCard(self, card, suit):
		self.knownCards.append((card, suit))
		self.cards.append((card, suit))

	def updatePlayedCard(self, card, suit):
		self.knownCards.append((card, suit))
		self.playedCards.append((card, suit))

	def getCardsToPlay(self):
		toPlayCards = self.knownCards
		try:
			for played in self.playedCards:
				toPlayCards.remove(played)
		except ValueError as e:
			pass
		return toPlayCards

	def stringKnownCards(self):
		return Sentences.TEAM_KNOWN_CARDS_S(self.cards)

	"""
	def updateHC(self, HC):
		self.HC += HC

	def stringHC(self):
		return Sentences.TEAM_HC_S(self.cards)
	"""