from Team import *
from Sentences import *

#### Improvement: Force them to be Team(N,S) && Team(E,O)

class ManageTeams:

	teams = []	# Class variable
	MAX_TEAMS = 2



	def createTeam(self, teamName):
		# First, let's check if this team already exists
		if ManageTeams.teams:
			team = ManageTeams.getTeamFromName(teamName)
			if team != False:
				print(Sentences.TEAM_ALREADY_EXISTS_S(teamName))
				return False
		# Check MAX_TEAMS
		if len(ManageTeams.teams) >= ManageTeams.MAX_TEAMS:
			print(Sentences.MAX_TEAMS_REACHED)
			return False

		team = Team(teamName)
		ManageTeams.teams.append(team)
		return True


	@classmethod
	def getTeamFromName(cls, teamName):
		for team in ManageTeams.teams:
			if team.name == teamName:
				return team
		#print(Sentences.NO_TEAM_S(teamName))
		return False


	@classmethod
	def getTeamFromPlayer(cls, playerName):
		for team in ManageTeams.teams:
			for player in team.players:
				if player.name == playerName:
					return team
		print(Sentences.NO_PLAYER_IN_TEAM(playerName))
		return False


	def __str__(self):
		toString = "Estos son los equipos:\n"
		if ManageTeams.teams:
			for team in ManageTeams.teams:
				toString += str(team) + "\n\n"
			return toString
		else:
			return "No hay equipos."


	def delete(self):
		for team in ManageTeams.teams:
			team.deleteTeam()
		ManageTeams.teams = []
		#print("ManageTeams deleted.")
		del self