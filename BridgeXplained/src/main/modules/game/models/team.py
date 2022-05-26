from helpers.sentences import *
import logging


class Team:


	def __init__(self, name):

		self.name = name
		self.HC = 0
		self.players = []
		self.cards = []
		logging.debug(Sentences.CREATE_TEAM(self.name))


	### BASIC METHODS ###
	def addPlayer(self, player):
		self.players.append(player)

	def __str__(self):
		try:
			toString = "Equipo " + self.name + " tiene " + str(self.HC) + " Honores en corazones."
			toString += "\n\tJUGADORES: "
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
	def updateHC(self, HC):
		self.HC += HC

	def updateCard(self, card, suit):
		self.cards.append((card, suit))