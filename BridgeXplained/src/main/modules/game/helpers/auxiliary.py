
class Auxiliary:

	###	GAME INFO AUXILIARY METHODS ###
	@classmethod
	def stringSortedCards(cls, cards):
		toReturn = ""
		sortedGroups = Auxiliary.sortCards(cards)

		# Now we create the return sentence with grouped and sorted cards
		for sortedSuit in sortedGroups:
			toReturn += "\nSUIT: " + str(sortedSuit[0][1])
			for card, suit in sortedSuit:
				toReturn += "\n" + str(card) + ", " + str(suit)

		return toReturn


	@classmethod
	def sortCards(cls, cards):
		picasGroup = []
		corazonesGroup = []
		diamantesGroup = []
		trebolesGroup = []
		
		# We group into suits, translating JQKA into numbers
		for card, suit in cards:
			if suit == "P":
				picasGroup.append((Auxiliary.cardToNumber(card), suit))
			if suit == "C":
				corazonesGroup.append((Auxiliary.cardToNumber(card), suit))
			if suit == "D":
				diamantesGroup.append((Auxiliary.cardToNumber(card), suit))
			if suit == "T":
				trebolesGroup.append((Auxiliary.cardToNumber(card), suit))

		# Now we sort in each suit group by card
		groupsNumbers = []
		if len(picasGroup) != 0:
			groupsNumbers.append(picasGroup)
		if len(corazonesGroup) != 0:
			groupsNumbers.append(corazonesGroup)
		if len(diamantesGroup) != 0:
			groupsNumbers.append(diamantesGroup)
		if len(trebolesGroup) != 0:
			groupsNumbers.append(trebolesGroup)

		sortedGroupsNumbers = []
		for unsortedSuit in groupsNumbers:
			sortedSuit = sorted(unsortedSuit, key=lambda x: x[0])
			sortedGroupsNumbers.append(sortedSuit)

		# We translate numbers to JQKA
		sortedGroups = []
		for sortedSuitNumbers in sortedGroupsNumbers:
			sortedSuit = []
			for card, suit in sortedSuitNumbers:
				sortedSuit.append((Auxiliary.numberToCard(card), suit))

			sortedGroups.append(sortedSuit)

		return sortedGroups

	@classmethod
	def compare(cls, card1, card2):
		if (Auxiliary.cardToNumber(card1) < Auxiliary.cardToNumber(card2)):
			return -1
		elif (Auxiliary.cardToNumber(card1) > Auxiliary.cardToNumber(card2)):
			return 1
		else:
			return 0

	@classmethod
	def compareEquals(cls, card1, card2):
		if (Auxiliary.cardToNumber(card1) <= Auxiliary.cardToNumber(card2)):
			return -1
		elif (Auxiliary.cardToNumber(card1) >= Auxiliary.cardToNumber(card2)):
			return 1
		else:
			return 0

	@classmethod
	def cardToNumber(cls, card):
		if str(card) == "J":
			return 11
		elif str(card) == "Q":
			return 12
		elif str(card) == "K":
			return 13
		elif str(card) == "A":
			return 14
		else:
			return int(card)

	@classmethod
	def numberToCard(cls, card):
		if str(card) == "11":
			return "J"
		elif str(card) == "12":
			return "Q"
		elif str(card) == "13":
			return "K"
		elif str(card) == "14":
			return "A"
		else:
			return str(card)

