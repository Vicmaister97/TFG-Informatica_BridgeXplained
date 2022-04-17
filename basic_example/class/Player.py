from ManageTeams import *

class Player:
	HCGlobal = 0		# Honors in Hearts, *class variable*

	def __init__(self, name):
		self.name = name
		self.HC = 0
		#self.HC = read_HC_from_conclussions(name)


	def __str__(self):
		try:
			return "Jugador " + self.name + " tiene " + str(self.HC) + " PH en corazones."
		except AttributeError:
			return "Aun no sabemos nada del jugador " + self.name + "."


	def deletePlayer(self):
		Player.HCGlobal -= self.HC
		print("Player " + self.name + " deleted.")
		del self


	def setHC(self, HC):
		self.HC = HC
		Player.HCGlobal += self.HC 							# Update global HC that we know
		ManageTeams.getTeamFromPlayer(self).updateHC(HC)	# Update HC of the team

	def getHC(self):
		return self.HC


	@classmethod
	def stringHCGlobal(cls):
		return "\nSe conocen en general " + str(Player.HCGlobal) + "PH en corazones."

	#def readHCFromConclussions(player):


# python if ($player == "N"): N.setHC(int($puntos_min))