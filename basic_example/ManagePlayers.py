from Player import *

class ManagePlayers:
	players = []	# Class variable

	def __str__(self):
		toString = "Estos son los jugadores: "
		for player in ManagePlayers.players:
			toString += player.name + ", "
		return toString[:len(toString)-2] + "."	# To remove the last ", "


	def createPlayer(self, name):
		player = Player(name)
		ManagePlayers.players.append(player)


	
	@classmethod
	def getPlayerFromName(cls, name):
		for player in ManagePlayers.players:
			if player.name == name:
				return player
