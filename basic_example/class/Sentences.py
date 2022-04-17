

class Sentences:

	MAX_PLAYERS_REACHED = "ERROR: MAX_PLAYERS reached."
	MAX_TEAMS_REACHED = "ERROR: MAX_TEAMS reached."

	@classmethod
	def NO_PLAYER_S(self, name):
		return "ERROR: Player " + name + " not found."

	@classmethod
	def NO_TEAM_S(self, name):
		return "ERROR: Team " + name + " not found."

	@classmethod
	def PLAYER_ALREADY_EXISTS_S(self, name):
		return "ERROR: Player " + name + " was previously created."

	@classmethod
	def TEAM_ALREADY_EXISTS_S(self, name):
		return "ERROR: Team " + name + " was previously created."

	@classmethod
	def NO_PLAYER_IN_TEAM(self, name):
		return "ERROR: Player " + name + " not found in any team."