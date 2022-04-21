from Player import *
from Sentences import *

class ManagePlayers:

	players = []	# Class variable
	MAX_PLAYERS = 4



	def createPlayer(self, playerName):
		# Let's check if this player already exists
		if ManagePlayers.players:
			player = ManagePlayers.getPlayerFromName(playerName)
			if player != False:
				print(Sentences.PLAYER_ALREADY_EXISTS_S(playerName))
				return False
		# Check MAX_PLAYERS
		if len(ManagePlayers.players) >= ManagePlayers.MAX_PLAYERS:
			print(Sentences.MAX_PLAYERS_REACHED)
			return False

		# Now we create the player
		player = Player(playerName)
		ManagePlayers.players.append(player)
		return player


	@classmethod
	def getPlayerFromName(cls, playerName):
		for player in ManagePlayers.players:
			if player.name == playerName:
				return player
		#print(Sentences.NO_PLAYER_S(playerName))
		return False


	def __str__(self):
		toString = "Estos son los jugadores: "
		if ManagePlayers.players:
			for player in ManagePlayers.players:
				toString += "\n" + str(player)
			return toString
		else:
			return "No hay jugadores."


	def delete(self):
		for player in ManagePlayers.players:
			player.deletePlayer()
		ManagePlayers.players = []
		#print("ManagePlayers deleted.")
		del self