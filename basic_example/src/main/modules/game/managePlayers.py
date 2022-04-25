from models.player import *
from helpers.sentences import *
from helpers.exceptions import *
import logging

logging.basicConfig(filename='game.log', encoding='utf-8', level=logging.DEBUG)


class ManagePlayers:

	MAX_PLAYERS = 4


	def __init__(self):
		self.players = []

	"""
	def getPlayers(self):
		return self.players
	"""

	# Exceptions: PlayerError
	def createPlayer(self, playerName):
		# Let's check if this player already exists
		try:
			playerExists = self.getPlayerFromName(playerName)
			raise PlayerError(Sentences.PLAYER_ALREADY_EXISTS_S(playerName))

		except PlayerNotFound:
			# Check MAX_PLAYERS
			if len(self.players) >= ManagePlayers.MAX_PLAYERS:
				raise PlayerError(Sentences.MAX_PLAYERS_REACHED)

			# Now we create the player
			player = Player(playerName)
			self.players.append(player)
			return player


	def getPlayerFromName(self, playerName):
		for player in self.players:
			if player.name == playerName:
				return player
		raise PlayerNotFound(Sentences.NOT_FOUND_PLAYER(playerName))


	def __str__(self):
		toString = Sentences.PLAYERS_INFO
		if self.players:
			for player in self.players:
				toString += "\n" + str(player)
		else:
			toString += Sentences.NO_PLAYERS

		return toString


	def delete(self):
		for player in self.players:
			player.deletePlayer()
		self.players = []
		logging.info(Sentences.PLAYER_MANAGER_DELETED)
		del self