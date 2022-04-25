from models.team import *
from helpers.sentences import *
from helpers.exceptions import *

import logging

logging.basicConfig(filename='game.log', encoding='utf-8', level=logging.DEBUG)


#### Improvement: Force them to be Team(N,S) && Team(E,O)

class ManageTeams:

	MAX_TEAMS = 2


	def __init__(self):
		self.teams = []

	# Exceptions: TeamError
	def createTeam(self, teamName):
		# First, let's check if this team already exists
		try:
			teamExists = self.getTeamFromName(teamName)
			raise TeamError(Sentences.TEAM_ALREADY_EXISTS_S(teamName))
			
		except TeamNotFound:

			# Check MAX_TEAMS
			if len(self.teams) >= ManageTeams.MAX_TEAMS:
				raise TeamError(Sentences.MAX_TEAMS_REACHED)

			team = Team(teamName)
			self.teams.append(team)
			return team


	def getTeamFromName(self, teamName):
		for team in self.teams:
			if team.name == teamName:
				return team
		raise TeamNotFound(Sentences.NOT_FOUND_TEAM_S(teamName))


	def getTeamFromPlayer(self, playerName):
		for team in self.teams:
			for player in team.players:
				if player.name == playerName:
					return team
		raise PlayerNotFound(Sentences.NO_PLAYER_IN_TEAM(playerName))


	def __str__(self):
		toString = Sentences.TEAMS_INFO
		if self.teams:
			for team in self.teams:
				toString += str(team) + "\n\n"
		else:
			toString += Sentences.NO_TEAMS

		return toString

	def delete(self):
		for team in self.teams:
			team.deleteTeam()
		self.teams = []
		logging.info(Sentences.TEAM_MANAGER_DELETED)
		del self