from managePlayers import *
from manageTeams import *
from helpers.sentences import *
import logging


class Game:


	def __init__(self, name):
		self.name = name
		self.playerManager = ManagePlayers()
		self.teamManager = ManageTeams()

		# Game info taken into account
		self.HC = 0
		self.knownCards = []

		logging.debug(Sentences.CREATE_GAME(self.name))


	### BASIC METHODS ###
	def createPlayer(self, playerName, teamName):
		player = self.playerManager.createPlayer(playerName)
		if (player != False):
			self.teamManager.getTeamFromName(teamName).addPlayer(player)
			return True
		return False


	def createTeam(self, teamName):
		return self.teamManager.createTeam(teamName)

	def __str__(self):
		toString = Sentences.GAME_INFO_S(self.name) \
		+ self.stringCardsGlobal() + str(self.teamManager) + Sentences.GAME_INFO_END_S(self.name)
		#+ self.stringCardsGlobal() + self.stringHCGlobal() + str(self.teamManager) + Sentences.GAME_INFO_END_S(self.name)
		return toString


	def deleteGame(self):
		self.playerManager.delete()
		self.teamManager.delete()

		self.knownCards = []
		logging.debug(Sentences.DEL_GAME(self.name))
		del self


	### AUXILIARY METHODS FOR RULES ###
	def getLastPlayer(self, playersThatHavePlayed):
		if len(playersThatHavePlayed) == 4:
			# All players have played, so new round
			return "NextRound"

		# We are going to iterate through the players
		# that have played. If next player is not in
		# playersThatHavePlayed, is the last one
		lastPlayer = None
		for player in playersThatHavePlayed:
			if player == "N":
				if "E" not in playersThatHavePlayed:
					lastPlayer = "N"
					break
			if player == "E":
				if "S" not in playersThatHavePlayed:
					lastPlayer = "E"
					break
			if player == "S":
				if "W" not in playersThatHavePlayed:
					lastPlayer = "S"
					break
			if player == "W":
				if "N" not in playersThatHavePlayed:
					lastPlayer = "W"
					break

		return lastPlayer


	def checkIfAbleToPlay(self, playerName, card, suit):
		self.playerManager.getPlayerFromName(playerName).checkIfAbleToPlay(card, suit)


	## ADD INFO FROM RULES TO OBJECTS
	def setCard(self, playerName, card, suit):
		self.playerManager.getPlayerFromName(playerName).setCard(card, suit)
		self.teamManager.getTeamFromPlayer(playerName).updateCard(card, suit)	# Update cards of the team
		self.knownCards.append((card, suit))

	def stringCardsGlobal(self):
		return Sentences.GAME_KNOWNCARDS_S(self.knownCards)

	def printCardsGlobal(self):
		print(self.stringCardsGlobal())

	"""
	def setHC(self, playerName, points):
		self.playerManager.getPlayerFromName(playerName).setHC(points)
		self.teamManager.getTeamFromPlayer(playerName).updateHC(points)	# Update HC of the team
		self.HC += points

	def stringHCGlobal(self):
		return Sentences.GAME_HC_S(self.HC)

	def printHCGlobal(self):
		print(self.stringHCGlobal())
	"""