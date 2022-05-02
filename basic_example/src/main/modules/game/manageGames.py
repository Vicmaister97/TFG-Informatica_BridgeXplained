from models.game import *
from helpers.sentences import *
from helpers.exceptions import *

import logging


class ManageGames:

	games = []


	@classmethod
	def createGame(cls, gameName):
		# First, let's check if this game already exists
		try:
			gameExists = ManageGames.getGameFromName(gameName)
			raise GameError(Sentences.GAME_ALREADY_EXISTS_S(gameName))

		except GameNotFound:
			game = Game(gameName)
			ManageGames.games.append(game)
			return game


	@classmethod
	def getGameFromName(cls, gameName):
		for game in ManageGames.games:
			if game.name == gameName:
				return game
		raise GameNotFound(Sentences.NOT_FOUND_GAME_S(gameName))


	"""
	def setHC(self, playerName, points):
		self.game.setHC(playerName, points)
	"""


	def __str__(self):
		toString = Sentences.DECORATOR_TREE_BEGIN + Sentences.GAMES_INFO
		if ManageGames.games:
			for game in ManageGames.games:
				toString += str(game)
		else:
			toString += Sentences.NO_GAMES
		
		toString += "\n\n" + Sentences.DECORATOR_TREE_END
		return toString


	@classmethod
	def printGames(cls):
		toString = Sentences.DECORATOR_TREE_BEGIN + Sentences.GAMES_INFO
		if ManageGames.games:
			for game in ManageGames.games:
				toString += str(game)
		else:
			toString += Sentences.NO_GAMES

		toString += "\n\n" + Sentences.DECORATOR_TREE_END
		print(toString)


	@classmethod
	def delete(cls):
		for game in ManageGames.games:
			game.deleteGame()
		ManageGames.games = []
		logging.debug(Sentences.GAMES_DELETED)
