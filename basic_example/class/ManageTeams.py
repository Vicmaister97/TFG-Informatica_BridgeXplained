from Team import *
from Sentences import *

#### Improvement: Force them to be Team(N,S) && Team(E,O)

class ManageTeams:
	teams = []	# Class variable

	MAX_TEAMS = 2

	def __str__(self):
		toString = "Estos son los equipos:\n"
		if ManageTeams.teams:
			for team in ManageTeams.teams:
				toString += str(team) + "\n\n"
			return toString
		else:
			return "No hay equipos."


	def createTeam(self, teamName):
		# First, let's check if this team already exists
		if ManageTeams.teams:
			team = self.getTeamFromName(teamName)
			if team != Sentences.NO_TEAM_S(teamName):
				return Sentences.TEAM_ALREADY_EXISTS_S(teamName)
		# Check MAX_TEAMS
		if len(ManageTeams.teams) >= ManageTeams.MAX_TEAMS:
			return Sentences.MAX_TEAMS_REACHED

		team = Team(teamName)
		ManageTeams.teams.append(team)


	def getTeamFromName(cls, teamName):
		for team in ManageTeams.teams:
			if team.name == teamName:
				return team
		return Sentences.NO_TEAM_S(teamName)

	@classmethod
	def getTeamFromPlayer(cls, searchPlayer):
		for team in ManageTeams.teams:
			for player in team.players:
				if player.name == searchPlayer.name:
					return team
		return Sentences.NO_PLAYER_IN_TEAM(searchPlayer.name)

	@classmethod
	def delete(cls):
		for team in ManageTeams.teams:
			#### HERE WE SHOULDN'T MANAGE PLAYERS DELETION
			"""
			for player in team.players:
				player.deletePlayer()
			"""
			team.deleteTeam()
		ManageTeams.teams = []
		print("ManageTeams deleted.")