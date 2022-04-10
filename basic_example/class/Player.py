

class Player:
	HCKnown = 0		# Honors in Hearts, *class variable*

	def __init__(self, name):
		self.name = name
		#self.HC = read_HC_from_conclussions(name)

	def __str__(self):
		try:
			return "Jugador " + self.name + " tiene " + str(self.HC) + " PH en corazones." + Player.stringHCKnown()
		except AttributeError:
			return "Aun no sabemos nada del jugador " + self.name + "."

	def deletePlayer(self):
		Player.HCKnown -= self.HC
		print("Player " + self.name + " deleted.")
		del self

	def setHC(self, HC):
		self.HC = HC
		Player.HCKnown += self.HC 		# Update global HC that we know
		print(self)


	#def readHCFromConclussions(player):

	@classmethod
	def stringHCKnown(cls):
		return "\nSe conocen en general " + str(Player.HCKnown) + "PH en corazones."

	@classmethod
	def printHCKnown(cls):
		print(Player.stringHCKnown())

# python if ($player == "N"): N.setHC(int($puntos_min))