

class Sentences:

	DECORATOR_TREE_BEGIN = "\n*\n*\n**\n***\n*****\n"
	DECORATOR_TREE_END = "\n*****\n***\n**\n*\n*\n"
	
	MAX_PLAYERS_REACHED = "ERROR: MAX_PLAYERS reached."
	MAX_TEAMS_REACHED = "ERROR: MAX_TEAMS reached."
	NO_GAMES = "Sorry, there are no games available."


	@classmethod
	def GAME_INFO_S(cls, name):
		return "\n\n---- GAME " + name + " INFO ----\n\n"

	@classmethod
	def GAME_INFO_END_S(cls, name):
		return "\n---- END " + name + " INFO ----\n"


	@classmethod
	def NO_PLAYER_S(cls, name):
		return "ERROR: Player " + name + " not found."

	@classmethod
	def NO_TEAM_S(cls, name):
		return "ERROR: Team " + name + " not found."

	@classmethod
	def NO_GAME_S(cls, name):
		return "ERROR: Game " + name + " not found."

	@classmethod
	def PLAYER_ALREADY_EXISTS_S(cls, name):
		return "ERROR: Player " + name + " was previously created."

	@classmethod
	def TEAM_ALREADY_EXISTS_S(cls, name):
		return "ERROR: Team " + name + " was previously created."

	@classmethod
	def GAME_ALREADY_EXISTS_S(cls, name):
		return "ERROR: Game " + name + " was previously created."


	@classmethod
	def NO_PLAYER_IN_TEAM(cls, name):
		return "ERROR: Player " + name + " not found in any team."