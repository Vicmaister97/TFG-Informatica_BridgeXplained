from Player import *

class ManagePlayers:
	players = []	# Class variable

	def __str__(self):
		toString = "Estos son los jugadores: "
		for player in ManagePlayers.players:
			toString += player.name + ", "
		if ManagePlayers.players:
			return toString[:len(toString)-2] + "."	# To remove the last ", "
		else:
			return "No hay jugadores."


	def createPlayer(self, name):
		player = Player(name)
		ManagePlayers.players.append(player)


	
	@classmethod
	def getPlayerFromName(cls, name):
		for player in ManagePlayers.players:
			if player.name == name:
				return player

	@classmethod
	def deletePlayers(cls):
		for player in ManagePlayers.players:
			player.deletePlayer()
		ManagePlayers.players = []
		if Player.HCKnown == 0:
			print("ManagePlayers deleted.")
		else:
			print("ManagePlayers deleted, \
				pero el valor de HCKnown no concuerda.")