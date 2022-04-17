from Player import *
from Sentences import *

class ManagePlayers:
	players = []	# Class variable

	MAX_PLAYERS = 4

	def __str__(self):
		toString = "Estos son los jugadores: "
		if ManagePlayers.players:
			for player in ManagePlayers.players:
				toString += "\n" + str(player)
			return toString
		else:
			return "No hay jugadores."


	def createPlayer(self, playerName):
		# Let's check if this player already exists
		if ManagePlayers.players:
			player = self.getPlayerFromName(playerName)
			if player != Sentences.NO_PLAYER_S(playerName):
				return Sentences.PLAYER_ALREADY_EXISTS_S(playerName)
		# Check MAX_PLAYERS
		if len(ManagePlayers.players) >= ManagePlayers.MAX_PLAYERS:
			return Sentences.MAX_PLAYERS_REACHED

		# Now we create the player
		player = Player(playerName)
		ManagePlayers.players.append(player)

	
	def getPlayerFromName(cls, playerName):
		for player in ManagePlayers.players:
			if player.name == playerName:
				return player
		return Sentences.NO_PLAYER_S(playerName)


	@classmethod
	def delete(cls):
		for player in ManagePlayers.players:
			player.deletePlayer()
		ManagePlayers.players = []
		if Player.HCGlobal == 0:
			print("ManagePlayers deleted.")
		else:
			print("ManagePlayers deleted, \
				pero el valor de HCGlobal no concuerda.")
