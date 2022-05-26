
class Sentences:

	DECORATOR_TREE_BEGIN = "\n*\n*\n**\n***\n*****\n"
	DECORATOR_TREE_END = "\n*****\n***\n**\n*\n*\n"

	DECORATOR = "----"
	DECORATOR_BEGIN = "\n" + DECORATOR
	DECORATOR_END = DECORATOR + "\n"

	DECORATOR_MINI_BEGIN = "\n--"
	DECORATOR_MINI_END = DECORATOR + "\n"
	
	MAX_PLAYERS_REACHED = "MAX_PLAYERS reached."
	MAX_TEAMS_REACHED = "MAX_TEAMS reached."

	NO_GAMES = "Sorry, there are no games available."
	NO_PLAYERS = "Sorry, there are no players available."
	NO_TEAMS = "Sorry, there are no teams available."

	TEAM_MANAGER_DELETED = "Team manager deleted."
	PLAYER_MANAGER_DELETED = "Player manager deleted."
	
	PLAYERS_INFO = "\n\n* PLAYERS INFO *\n\n" 
	TEAMS_INFO = "\n" + DECORATOR_BEGIN + " TEAMS INFO " + DECORATOR_END + "\n"
	GAMES_INFO = "\n" + DECORATOR_BEGIN + " GAMES INFO " + DECORATOR_END + "\n"

	GAMES_DELETED = DECORATOR_BEGIN + " GAMES DELETED " + DECORATOR_END


	###	GAME ATTRIBUTES ###
	@classmethod
	def GAME_KNOWNCARDS_S(cls, knownCards):
		DECORATOR = "----"
		DECORATOR_BEGIN = "\n" + DECORATOR
		DECORATOR_END = "\n" + DECORATOR + "\n"

		sentence = DECORATOR_BEGIN + "These are the known cards:\n"
		for card, suit in knownCards:
			sentence += "\n" + str(card) + ", " + str(suit)

		return sentence + DECORATOR_END

	@classmethod
	def GAME_HC_S(cls, honors, suit):
		DECORATOR = "----"
		DECORATOR_MINI_BEGIN = "\n--"
		DECORATOR_MINI_END = DECORATOR + "\n"

		return DECORATOR_MINI_BEGIN + "We know " + str(honors) + " Honors in " + str(suit) + DECORATOR_MINI_END

	@classmethod
	def PLAYER_HC_S(cls, honors, suit):
		DECORATOR = "----"
		DECORATOR_MINI_BEGIN = "\n--"
		DECORATOR_MINI_END = DECORATOR + "\n"

		return DECORATOR_MINI_BEGIN + "Has " + str(honors) + " Honors in " + str(suit) + DECORATOR_MINI_END


	@classmethod
	def PLAYER_CARDS_S(cls, cards):
		DECORATOR = "----"
		DECORATOR_BEGIN = "\n" + DECORATOR
		DECORATOR_END = DECORATOR + "\n"

		sentence = DECORATOR_BEGIN + "These are his/her cards:\n"
		for card, suit in cards:
			sentence += "\n" + str(card) + ", " + str(suit)

		return sentence + DECORATOR_END

	@classmethod
	def MISSING_CARD(cls, name, card, suit):
		return "LOGIC ERROR: Player " + name + " does not have the " + str(card) + " of " + str(suit) + "."


	@classmethod
	def GAME_INFO_S(cls, name):
		DECORATOR = "----"
		DECORATOR_BEGIN = "\n" + DECORATOR
		DECORATOR_END = DECORATOR + "\n"

		return "\n" + DECORATOR_BEGIN + " GAME " + name + " INFO " + DECORATOR_END

	@classmethod
	def GAME_INFO_END_S(cls, name):
		DECORATOR = "----"
		DECORATOR_BEGIN = "\n" + DECORATOR
		DECORATOR_END = DECORATOR + "\n"

		return DECORATOR_BEGIN + " END " + name + " INFO " + DECORATOR_END

	@classmethod
	def PLAYER_INFO_S(cls, name):
		DECORATOR = "----"
		DECORATOR_BEGIN = "\n" + DECORATOR
		DECORATOR_END = DECORATOR + "\n"

		return DECORATOR_BEGIN + " Player " + str(name) + " info " + DECORATOR_END




	###	EXCEPTION MESSAGES ###
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
		DECORATOR = "----"
		DECORATOR_BEGIN = "\n" + DECORATOR
		DECORATOR_END = DECORATOR + "\n"

		return DECORATOR_BEGIN + " GAME " + name + " DELETED " + DECORATOR_END