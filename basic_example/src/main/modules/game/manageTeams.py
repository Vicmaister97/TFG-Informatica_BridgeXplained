from models.team import *
from helpers.sentences import *

#### Improvement: Force them to be Team(N,S) && Team(E,O)

class ManageTeams:

	MAX_TEAMS = 2

	def __init__(self):
		self.teams = []


	def createTeam(self, teamName):
		# First, let's check if this team already exists
		teamExists = self.getTeamFromName(teamName)
		if teamExists != False:
			print(Sentences.TEAM_ALREADY_EXISTS_S(teamName))
			return False
		# Check MAX_TEAMS
		if len(self.teams) >= ManageTeams.MAX_TEAMS:
			print(Sentences.MAX_TEAMS_REACHED)
			return False

		team = Team(teamName)
		self.teams.append(team)
		return True



	def getTeamFromName(self, teamName):
		for team in self.teams:
			if team.name == teamName:
				return team
		#print(Sentences.NO_TEAM_S(teamName))
		return False



	def getTeamFromPlayer(self, playerName):
		for team in self.teams:
			for player in team.players:
				if player.name == playerName:
					return team
		print(Sentences.NO_PLAYER_IN_TEAM(playerName))
		return False


	def __str__(self):
		toString = "Estos son los equipos:\n"
		if self.teams:
			for team in self.teams:
				toString += str(team) + "\n\n"
			return toString
		else:
			return "No hay equipos."


	def delete(self):
		for team in self.teams:
			team.deleteTeam()
		self.teams = []
		#print("ManageTeams deleted.")
		del self