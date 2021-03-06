from managePlayers import *
from manageTeams import *
from helpers.sentences import *
import logging


class Game:


	def __init__(self, name):
		self.name = name
		self.playerManager = ManagePlayers()
		self.teamManager = ManageTeams()
		self.HC = 0
		logging.debug(Sentences.CREATE_GAME(self.name))


	def createPlayer(self, playerName, teamName):
		player = self.playerManager.createPlayer(playerName)
		if (player != False):
			self.teamManager.getTeamFromName(teamName).addPlayer(player)
			return True
		return False


	def createTeam(self, teamName):
		return self.teamManager.createTeam(teamName)


	def setHC(self, playerName, points):
		self.playerManager.getPlayerFromName(playerName).setHC(points)
		self.teamManager.getTeamFromPlayer(playerName).updateHC(points)	# Update HC of the team
		self.HC += points


	def stringHCGlobal(self):
		return Sentences.GAME_HC_S(self.HC)


	def printHCGlobal(self):
		print(self.stringHCGlobal())

	def __str__(self):
		toString = Sentences.GAME_INFO_S(self.name) \
		+ self.stringHCGlobal() + str(self.teamManager) + Sentences.GAME_INFO_END_S(self.name)
		return toString


	def deleteGame(self):
		self.playerManager.delete()
		self.teamManager.delete()
		logging.debug(Sentences.DEL_GAME(self.name))
		del self