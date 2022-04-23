from models.player import *
from helpers.sentences import *

class ManagePlayers:

	MAX_PLAYERS = 4


	def __init__(self):
		self.players = []

	"""
	def getPlayers(self):
		return self.players
	"""


	def createPlayer(self, playerName):
		# Let's check if this player already exists
		playerExists = self.getPlayerFromName(playerName)
		if playerExists != False:
			print(Sentences.PLAYER_ALREADY_EXISTS_S(playerName))
			return False
		# Check MAX_PLAYERS
		if len(self.players) >= ManagePlayers.MAX_PLAYERS:
			print(Sentences.MAX_PLAYERS_REACHED)
			return False

		# Now we create the player
		player = Player(playerName)
		self.players.append(player)
		return player


	def getPlayerFromName(self, playerName):
		for player in self.players:
			if player.name == playerName:
				return player
		#print(Sentences.NO_PLAYER_S(playerName))
		return False


	def __str__(self):
		toString = "Estos son los jugadores: "
		if self.players:
			for player in self.players:
				toString += "\n" + str(player)
			return toString
		else:
			return "No hay jugadores."


	def delete(self):
		for player in self.players:
			player.deletePlayer()
		self.players = []
		#print("ManagePlayers deleted.")
		del self