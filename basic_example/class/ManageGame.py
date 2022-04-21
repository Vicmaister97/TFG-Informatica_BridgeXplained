from ManagePlayers import *
from ManageTeams import *
from Sentences import *

class ManageGame:

	playerManager = ManagePlayers()
	teamManager = ManageTeams()



	def createPlayer(self, playerName, teamName):
		player = ManageGame.playerManager.createPlayer(playerName)
		if (player != False):
			ManageTeams.getTeamFromName(teamName).addPlayer(player)
			return True
		return False


	def createTeam(self, teamName):
		return ManageGame.teamManager.createTeam(teamName)

	@classmethod
	def setHC(cls, playerName, points):
		ManagePlayers.getPlayerFromName(playerName).setHC(points)
		ManageTeams.getTeamFromPlayer(playerName).updateHC(points)	# Update HC of the team

	def __str__(self):
		toString = Sentences.DECORATOR_TREE + "\n\n---- GAME INFO ----\n\n" \
		+ str(ManageGame.teamManager) + Sentences.DECORATOR_TREE
		return toString

	@classmethod
	def printGame(cls):
		toString = Sentences.DECORATOR_TREE + "\n\n---- GAME INFO ----\n\n" \
		+ str(ManageGame.teamManager) + Sentences.DECORATOR_TREE
		print(toString)


	@classmethod
	def delete(cls):
		ManageGame.playerManager.delete()
		ManageGame.teamManager.delete()
		print("\n---- GAME DELETED ----\n")
