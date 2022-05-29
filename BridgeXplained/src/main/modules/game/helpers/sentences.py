from helpers.auxiliary import *

class Sentences:

	### DECORATORS ###
	DECORATOR_TREE_BEGIN = "\n*\n*\n**\n***\n*****\n"
	DECORATOR_TREE_END = "\n*****\n***\n**\n*\n*\n"

	DECORATOR = "----"
	DECORATOR_BEGIN = "\n" + DECORATOR
	DECORATOR_END = DECORATOR + "\n"

	DECORATOR_MINI_BEGIN = "\n--"
	DECORATOR_MINI_END = DECORATOR + "\n"
	
	### EXCEPTION MESSAGES ###
	MAX_PLAYERS_REACHED = "MAX_PLAYERS reached."
	MAX_TEAMS_REACHED = "MAX_TEAMS reached."

	NO_GAMES = "Sorry, there are no games available."
	NO_PLAYERS = "Sorry, there are no players available."
	NO_TEAMS = "Sorry, there are no teams available."

	TEAM_MANAGER_DELETED = "Team manager deleted."
	PLAYER_MANAGER_DELETED = "Player manager deleted."
	

	### SHOW ATTRIBUTES/INFO ABOUT OBJECTS ###
	GAMES_INFO = "\n" + DECORATOR_BEGIN + " GAMES INFO " + DECORATOR_END + "\n"
	PLAYERS_INFO = "\n\n* PLAYERS INFO *\n\n" 
	TEAMS_INFO = "\n" + DECORATOR_BEGIN + " TEAMS INFO " + DECORATOR_END + "\n"

	GAMES_DELETED = DECORATOR_BEGIN + " GAMES DELETED " + DECORATOR_END

	SHOW_CARDS = DECORATOR_MINI_BEGIN + " These are all the known cards in the game:\n"
	PLAYER_CARDS = DECORATOR_MINI_BEGIN + " Player *KNOWN* cards:\n"
	PLAYER_CARDSTOPLAY = DECORATOR_MINI_BEGIN + " Player is *ABLE TO PLAY* these cards:\n"
	TEAM_CARDS = DECORATOR_MINI_BEGIN + " These are all the known cards in the team:\n"

	###	GAME INFO SENTENCES ###
	@classmethod
	def GAME_KNOWNCARDS_S(cls, knownCards):
		return Sentences.SHOW_CARDS + Sentences.sortPretty(knownCards)

	@classmethod
	def TEAM_KNOWN_CARDS_S(cls, knownCards):
		return Sentences.TEAM_CARDS + Sentences.sortPretty(knownCards)

	@classmethod
	def TEAM_CARDS_S(cls, cards):
		return Sentences.TEAM_CARDS + Sentences.sortPretty(cards)

	@classmethod
	def PLAYER_CARDS_S(cls, cards):
		return Sentences.PLAYER_CARDS + Sentences.sortPretty(cards)

	@classmethod
	def PLAYER_CARDSTOPLAY_S(cls, cards):
		return Sentences.PLAYER_CARDSTOPLAY + Sentences.sortPretty(cards)

	@classmethod
	def sortPretty(cls, cards):
		sentence = ""
		sentence += Auxiliary.stringSortedCards(cards)
		sentence + "\n" + Sentences.DECORATOR_MINI_END
		return sentence


	@classmethod
	def GAME_HC_S(cls, HC):
		return Sentences.DECORATOR_MINI_BEGIN + " In the game are known " + str(HC) + " Honors in Corazones" + Sentences.DECORATOR_MINI_END

	@classmethod
	def PLAYER_HC_S(cls, HC):
		return Sentences.DECORATOR_MINI_BEGIN + " Has " + str(HC) + " Honors in Corazones" + Sentences.DECORATOR_MINI_END

	@classmethod
	def TEAM_HC_S(cls, HC):
		return Sentences.DECORATOR_MINI_BEGIN + " Team has " + str(HC) + " Honors in Corazones" + Sentences.DECORATOR_MINI_END


	@classmethod
	def GAME_INFO_S(cls, name):
		return "\n" + Sentences.DECORATOR_BEGIN + " GAME " + name + " INFO " + Sentences.DECORATOR_END

	@classmethod
	def GAME_INFO_END_S(cls, name):
		return Sentences.DECORATOR_BEGIN + " END " + name + " INFO " + Sentences.DECORATOR_END

	@classmethod
	def PLAYER_INFO_S(cls, name):
		return Sentences.DECORATOR_BEGIN + " Player " + str(name) + " info " + Sentences.DECORATOR_END

	@classmethod
	def TEAM_INFO_S(cls, name):
		return Sentences.DECORATOR_BEGIN + " Team " + str(name) + " info " + Sentences.DECORATOR_END



	###	EXCEPTION MESSAGES ###
	@classmethod
	def MISSING_CARD(cls, name, card, suit):
		return "LOGIC ERROR: Player " + name + " does not have the " + str(card) + " of " + str(suit) + "."



	@classmethod
	def NO_INFO_PLAYER(cls, name):
		return "There is no info about Player " + name + "."

	@classmethod
	def NO_INFO_TEAM(cls, name):
		return "There is no info about Team " + name + "."

	@classmethod
	def NOT_FOUND_PLAYER(cls, name):
		return "Player " + name + " not found."

	@classmethod
	def NOT_FOUND_TEAM_S(cls, name):
		return "Team " + name + " not found."

	@classmethod
	def NOT_FOUND_GAME_S(cls, name):
		return "Game " + name + " not found."

	@classmethod
	def NO_PLAYER_IN_TEAM(cls, name):
		return "Player " + name + " not found in any team."



	@classmethod
	def PLAYER_ALREADY_EXISTS_S(cls, name):
		return "Player " + name + " was previously created."

	@classmethod
	def TEAM_ALREADY_EXISTS_S(cls, name):
		return "Team " + name + " was previously created."

	@classmethod
	def GAME_ALREADY_EXISTS_S(cls, name):
		return "Game " + name + " was previously created."



	### DEBUG SENTENCES ###
	@classmethod
	def CREATE_PLAYER(cls, name):
		return "Player " + name + " created."

	@classmethod
	def CREATE_TEAM(cls, name):
		return "Team " + name + " created."

	@classmethod
	def CREATE_GAME(cls, name):
		return "Game " + name + " created."


	@classmethod
	def DEL_PLAYER(cls, name):
		return "Player " + name + " deleted."

	@classmethod
	def DEL_TEAM(cls, name):
		return "Team " + name + " deleted."

	@classmethod
	def DEL_GAME(cls, name):
		return Sentences.DECORATOR_BEGIN + " GAME " + name + " DELETED " + Sentences.DECORATOR_END