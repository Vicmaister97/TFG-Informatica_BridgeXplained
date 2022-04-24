
class Sentences:

	DECORATOR_TREE_BEGIN = "\n*\n*\n**\n***\n*****\n"
	DECORATOR_TREE_END = "\n*****\n***\n**\n*\n*\n"
	
	MAX_PLAYERS_REACHED = "MAX_PLAYERS reached."
	MAX_TEAMS_REACHED = "MAX_TEAMS reached."

	NO_GAMES = "Sorry, there are no games available."

	@classmethod
	def GAME_INFO_S(cls, name):
		return "\n\n---- GAME " + name + " INFO ----\n\n"

	@classmethod
	def GAME_INFO_END_S(cls, name):
		return "\n---- END " + name + " INFO ----\n"


	@classmethod
	def NO_INFO_PLAYER(cls, name):
		return "\nAun no sabemos nada del jugador " + name + "."

	@classmethod
	def NO_INFO_TEAM(cls, name):
		return "Aun no sabemos nada del equipo " + name + "."


	@classmethod
	def NOT_FOUND_PLAYER(cls, name):
		return "Player " + name + " not found."

	@classmethod
	def NO_TEAM_S(cls, name):
		return "Team " + name + " not found."

	@classmethod
	def NO_GAME_S(cls, name):
		return "Game " + name + " not found."


	@classmethod
	def PLAYER_ALREADY_EXISTS_S(cls, name):
		return "Player " + name + " was previously created."

	@classmethod
	def TEAM_ALREADY_EXISTS_S(cls, name):
		return "Team " + name + " was previously created."

	@classmethod
	def GAME_ALREADY_EXISTS_S(cls, name):
		return "Game " + name + " was previously created."


	@classmethod
	def NO_PLAYER_IN_TEAM(cls, name):
		return "Player " + name + " not found in any team."



	@classmethod
	def CREATE_PLAYER(cls, name):
		return "player " + name + " created."

	@classmethod
	def CREATE_TEAM(cls, name):
		return "Team " + name + " created."

	@classmethod
	def CREATE_GAME(cls, name):
		return "Game " + name + " created."



	@classmethod
	def DEL_PLAYER(cls, name):
		return "\nPlayer " + name + " deleted."

	@classmethod
	def DEL_TEAM(cls, name):
		return "Team " + name + " deleted."

	@classmethod
	def DEL_GAME(cls, name):
		return "\n---- GAME DELETED ----\n"