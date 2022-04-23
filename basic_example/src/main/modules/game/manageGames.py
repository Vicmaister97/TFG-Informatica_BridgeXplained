from models.game import *

class ManageGames:

	games = []


	@classmethod
	def createGame(cls, gameName):
		# First, let's check if this game already exists
		gameExists = ManageGames.getGameFromName(gameName)
		if gameExists != False:
			print(Sentences.GAME_ALREADY_EXISTS_S(teamName))
			return False
		game = Game(gameName)
		ManageGames.games.append(game)
		return game


	@classmethod
	def getGameFromName(cls, gameName):
		for game in ManageGames.games:
			if game.name == gameName:
				return game
		return False


	def setHC(self, playerName, points):
		self.game.setHC(playerName, points)


	def __str__(self):
		toString = Sentences.DECORATOR_TREE_BEGIN + "\n\n---- GAME INFO ----\n\n" \
		+ str(self.game.teamManager) + Sentences.DECORATOR_TREE_END
		return toString


	@classmethod
	def printGames(cls):
		if ManageGames.games:
			toString = Sentences.DECORATOR_TREE_BEGIN + "\n\n---- GAMES INFO ----\n\n" 
			for game in ManageGames.games:
				toString += str(game)
			toString += "\n\n" + Sentences.DECORATOR_TREE_END
			print(toString)
		else:
			toString = Sentences.NO_GAMES
			print(toString)


	@classmethod
	def delete(cls):
		for game in ManageGames.games:
			game.deleteGame()
		ManageGames.games = []
		print("\n---- GAMES DELETED ----\n")
