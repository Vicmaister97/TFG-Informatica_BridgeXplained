

class Player:
	HCKnown = 0		# Honors in Hearts, *class variable*

	def __init__(self, name):
		self.name = name
		#self.HC = read_HC_from_conclussions(name)

	def __str__(self):
		return "Jugador " + self.name + " tiene " + str(self.HC) + " PH en corazones."


	def setHC(self, HC):
		self.HC = HC
		Player.HCKnown += self.HC 		# Update global HC that we know
		print(self)


	#def readHCFromConclussions(player):


	@classmethod
	def printHCKnown(cls):
		print("\nSe conocen en general " + str(Player.HCKnown) + "PH en corazones.")
		