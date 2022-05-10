from helpers.sentences import *
import logging


class Team:


	def __init__(self, name):

		self.name = name
		self.HC = 0
		self.players = []
		logging.debug(Sentences.CREATE_TEAM(self.name))

	"""
	def getPlayers(self):
		return self.players
	"""

	def addPlayer(self, player):
		self.players.append(player)


	def updateHC(self, HC):
		self.HC += HC


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
		logging.debug(Sentences.DEL_TEAM(self.name))
		del self


	"""
	def getHC(self):
		# As this info is updated through the reasoning,
		# 	this method is going to calculate
		# 	the *current* HC from the players info.
		self.HC = 0
		for player in self.players:
			self.HC += player.getHC()
		return self.HC
	"""
