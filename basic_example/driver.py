## AUTHOR AND GENERAL VIEW OF THE CODE

from __future__ import with_statement
import sys
import os
import time
import logging
from pyke import knowledge_engine, krb_traceback, goal
from datetime import datetime

sys.path.append("src/main/modules/game/")
from manageGames import *
from helpers.exceptions import *

"""
######## ######## GLOBAL VARIABLES ######## ########
"""

engine = knowledge_engine.engine(__file__)

""" 
Variable "activated" is use for executing forward or backwards chaining several times
	and only execute the complete engine reasoning once.
"""
isActiveFC = False
isActiveBC = False


performingProof = False     # Used for not trying to proove middle rules that we know are true
startTime = time.time()     # For exception handling
rule_prooving = "NO RULE"

# USER MESSAGES
TRUE_RULE = "\n------------\n%s\nTHE RULE YOU WROTE IS TRUE!!!!!!!!!!\n------------\n"
FALSE_RULE = "\n------------\n%s\nThe rule you wrote is False.\n------------\n"
RESET_S = "\n\n********RESETTING THE PROGRAM********\n\n"
START = "\n\n********STARTING THE PROGRAM********\n%s\n\n"

PROOF_BEGIN_DECORATOR = "\n\n\n------------------------------------\n"
PROOF_END_DECORATOR = "\n------------------------------------\n\n\n"


PROOF_BEGIN = PROOF_BEGIN_DECORATOR + "\nBEGIN PROOF of %s.\n"
PROOF_START = "\n\nPerforming the proof of %s:"
SUBPROOF_START = "\nPerforming the sub-proof (%s):"
PROOF_END = "\nEND PROOF of %s.\n" + PROOF_END_DECORATOR
PROOF_DONE = "\tProof done."
PROOF_DONE_BAD = "\tProof done. It's not a complete proof as there was an exception."
PROOF_TIME = "\tProof time: %.4f seconds"

# FILES VARIABLES
DIRECTORY_CONCLUSSIONS = "./conclusions/"
DIRECTORY_LOG = "./logs/"
DIRECTORIES = [DIRECTORY_CONCLUSSIONS, DIRECTORY_LOG]

F_MID_RULES = DIRECTORY_CONCLUSSIONS + "midRules.txt"
F_CONCLUSIONS = DIRECTORY_CONCLUSSIONS + "conclusiones.txt"
F_CONCLUSIONS_FC = DIRECTORY_CONCLUSSIONS + "conclusiones_fc.txt"
F_CONCLUSIONS_BC = DIRECTORY_CONCLUSSIONS + "conclusiones_bc.txt"

LIST_OF_FILES = [F_MID_RULES, F_CONCLUSIONS, F_CONCLUSIONS_FC, F_CONCLUSIONS_BC]

logging.basicConfig(filename=DIRECTORY_LOG+'game.log', encoding='utf-8', level=logging.DEBUG)



def fc():
	try:
		global isActiveFC
		if isActiveFC == False:
			# Clean files and engine conclussions
			START_CLEAN()

			# Run the engine and measure time of the complete FC reasoning
			runEngine('fc_numbers')

			ManageGames.printGames()

			# To run several times the forward-chaining test without
			# executing again the engine complete reasoning
			isActiveFC = True
			engine.print_stats()

		"""
		# TRY TO SEE IF WE CAN ACCESS ENGINE RELATIONS
		numbers.honores_corazones_FINAL($tot)
		# Now we read the conclusions
		file = open("conclussions.txt", "r")
		list_of_conclussions = file.readlines()
		for conclussion in list_of_conclussions
		"""


	except Exception as e:
		logging.error(e)
		RESET()
		#sys.exit(1)
	except NotFound as e:
		logging.warning(e)
		RESET()




# driver.fc_proove('numbers.honores_corazones_new_post(S, 1)')
def fc_proove(rule_to_prove):
	fc()

	try:
		global startTime
		global rule_prooving
		rule_prooving = rule_to_prove
		"""
		with engine.prove_goal('numbers.honores_corazones_FINAL()') \
		  as gen:
			for vars, plan in gen:
				print "SE CONOCEN TODOS LOS PH EN CORAZONES!!!!!\n"
				print plan
		"""

		"""
		The following proving rule is just to know if the rule is true or false.
		With FC, we don't get the reasoning.
		"""
		goal = False
		logProofBEGIN(F_CONCLUSIONS_FC)
		printAndLog(PROOF_START % rule_prooving)
		# Measure time of the proof
		startTime = time.time()


		with engine.prove_goal(str(rule_to_prove)) \
		  as gen2:
			for vars, plan in gen2:
				#print "%s tiene %s PH en corazones\n" % (vars['player'], vars['puntos'])
				#print plan
				#print gen2
				goal = True
		if goal == True:
			logTrueRule(rule_to_prove, F_CONCLUSIONS_FC)
		else:
			logFalseRule(rule_to_prove, F_CONCLUSIONS_FC)


		# Measure time of the proof
		endTime = time.time()
		proofTime = endTime - startTime

		# Logging
		logProofDone(rule_to_prove, proofTime, F_CONCLUSIONS_FC)


	except Exception as e:
		logging.error(e)
		RESET_PROOF(F_CONCLUSIONS_FC)
		#sys.exit(1)
	except NotFound as e:
		logging.warning(e)
		RESET_PROOF(F_CONCLUSIONS_FC)



# driver.bc('bc_numbers.honores_corazones_new_post(S, 1)', True)
def bc(rule_to_prove, isInitialProof):
	try:
		global isActiveBC
		global isActiveFC
		global performingProof
		global startTime
		global rule_prooving


		if isActiveFC == False:
			# Clean files and engine conclussions
			START_CLEAN()

			# Run the engine and measure time of the complete FC reasoning
			runEngine('fc_numbers')     # NECESSARY FOR COMPLEX PROOFS

			# To run several times the forward-chaining test without
			# executing again the engine complete reasoning
			isActiveFC = True

		if isActiveBC == False:

			# Run the engine and measure time of the complete BC reasoning
			runEngine('bc_numbers')
			
			# To run several times the forward-chaining test without
			# executing again the engine complete reasoning
			isActiveBC = True
			engine.print_stats()


		"""
		with engine.prove_goal('bc_numbers.honores_corazones_FINAL()') \
		  as gen:
			for vars, plan in gen:
				print "SE CONOCEN TODOS LOS PH EN CORAZONES!!!!!\n"
				print plan
		"""

		"""
		The following proving rule resolves if the rule is true or false.

		The main importance of this proving goal is that
			*** we obtain the reasoning that leds to the proof of this goal ***
		"""
		logProofBEGIN(F_CONCLUSIONS_BC)
		goal = False

		if isInitialProof == True:
			rule_prooving = rule_to_prove
			printAndLog(PROOF_START % rule_prooving)
		else:
			printAndLog(SUBPROOF_START % rule_to_prove)

		# Measure time of the proof
		startTime = time.time()


		with engine.prove_goal(str(rule_to_prove)) \
		  as gen2:
			for vars, plan in gen2:
				#print "%s tiene %s PH en corazones\n" % (vars['player'], vars['puntos'])
				#print plan
				#print gen2
				goal = True

		if isInitialProof == True:
			if goal == True:
				logTrueRule(rule_to_prove, F_CONCLUSIONS_BC)
			else:
				logFalseRule(rule_to_prove, F_CONCLUSIONS_BC)
				# Measure time of the proof
				endTime = time.time()
				proofTime = endTime - startTime

				# Logging
				logProofDone(rule_to_prove, proofTime, F_CONCLUSIONS_BC)
				return

		"""
			Pyke with backwards chaining only prints the last rule, altough
			it has done all the reasoning and gone through several rules to
			prove that the goal it's true.
			That's why we write in the conclussions file the direct rules that
			have led to the proven one, so we can "prove" them (call prove_goal)
			again in order to force Pyke to write them and their direct rules,
			and repeat this process again till we hit an initial fact.
			This will allow us to have the complete reasoning.

			In resume: If we still have to explain more about how we reached the proven
			statement (it comes from another rule), we execute the engine till 
			we hit an initial fact.
		"""
		midRules = []
		with open(F_MID_RULES, "r") as f:
			lines = f.readlines()
			for line in lines:
				if "bc_numbers" in line:
					# This means that we still have rules to prove
					# We add the rule
					midRules.append(line)

		if not midRules:   # Empty list
			print ("SE ACABO WEEEEEEEYYYYYY")

			# Measure time of the proof
			endTime = time.time()
			proofTime = endTime - startTime

			# Logging
			logProofDone(rule_to_prove, proofTime, F_CONCLUSIONS_BC)
			return

		performingProof = True
		
		# We remove those mid rules from the conclussions file
		# We leave only the final facts
		with open(F_MID_RULES, "w") as new_f:
			for followRule in midRules:
				lines.remove(followRule)

			# Write only the rules not to prove (final facts)
			new_f.writelines(lines)
			
		print(midRules)
		# Now, we have to prove those mid rules
		for followRule in midRules:
			while performingProof:
				print("SE VIENE %s") % (followRule)
				# We run this rule to follow the reasoning
				bc(followRule.rstrip("\n"), False)


		if isInitialProof == True:
			# Measure time of the proof
			endTime = time.time()
			proofTime = endTime - startTime

			# Logging
			logProofDone(rule_to_prove, proofTime, F_CONCLUSIONS_BC)


	except Exception as e:
		logging.error(e)
		RESET_PROOF(F_CONCLUSIONS_BC)
		#sys.exit(1)

	except NotFound as e:
		logging.warning(e)
		RESET_PROOF(F_CONCLUSIONS_BC)


""" -------- AUXILIARY METHODS -------- """

####	LOGGING and print

def logTrueRule(rule_to_prove, file):
	printAndLogInfo(TRUE_RULE % (rule_to_prove))
	with open(file, "a") as f:
		f.write(TRUE_RULE % (rule_to_prove))

def logFalseRule(rule_to_prove, file):
	printAndLogInfo(FALSE_RULE % (rule_to_prove))
	with open(file, "a") as f:
		f.write(FALSE_RULE % (rule_to_prove))


def logProofDone(rule_to_prove, proofTime, file):
	printAndLog(PROOF_DONE)
	logProofTime(proofTime)
	logProofEND(file)

def logProofDoneBad(proofTime, file):
	printAndLogWarning(PROOF_DONE_BAD)
	logProofTime(proofTime)
	logProofEND(file)


def logProofTime(proofTime):
	printAndLog(PROOF_TIME % (proofTime))

def logProofBEGIN(file):
	global rule_prooving
	printAndLog(PROOF_BEGIN % (rule_prooving))
	with open(file, "a") as f:
		f.write(PROOF_BEGIN % (rule_prooving))

def logProofEND(file):
	global rule_prooving
	printAndLog(PROOF_END % (rule_prooving))
	# Leave some empty space in the conclussions_bc file for
	# future proofs
	with open(file, "a") as f:
		f.write(PROOF_END % (rule_prooving))

def printAndLog(sentence):
	print(sentence)
	logging.debug(sentence)

def printAndLogInfo(sentence):
	print(sentence)
	logging.info(sentence)

def printAndLogWarning(sentence):
	print(sentence)
	logging.warning(sentence)


####	MANAGE PROGRAM

def START_CLEAN():
	now = datetime.now()
	nowStr = now.strftime("%d/%m/%Y %H:%M:%S")
	print(START) % nowStr
	logging.debug(START % nowStr)

	# In the start we clean previous conclussions files
	#   and the engine
	cleanFiles()

	cleanEngine()


def RESET():
	krb_traceback.print_exc()
	#logging.debug(krb_traceback)

	print(RESET_S)
	logging.debug(RESET_S)

	cleanEngine()

	cleanGame()


def RESET_PROOF(file):
	global startTime
	global rule_to_prove
	# Measure time of the proof
	endTime = time.time()
	proofTime = endTime - startTime
	logProofDoneBad(proofTime, file)
	RESET()


def cleanFiles():
	# We need that the directories exists
	for directory in DIRECTORIES:
		if os.path.isdir(directory) == False:
			os.mkdir(directory)

	# Clean files
	for file in LIST_OF_FILES:
		open(file, "w").close()


def cleanEngine():
	global isActiveBC
	global isActiveFC
	global performingProof

	engine.reset()

	# Clean global variables
	isActiveFC = False
	isActiveBC = False
	performingProof = False


# Delete Game debug
def cleanGame():
	ManageGames.delete()


def runEngine(reasoning):
	# Measure time of the complete reasoning
	startTime = time.time()
	engine.activate(reasoning)
	endTime = time.time()
	engineTime = endTime - startTime

	if reasoning == 'fc_numbers':
		reasoningType = "\n\nFC"
	else:
		reasoningType = "\n\nBC"
	print(reasoningType + " engine time: %.6f seconds, %.0f asserts/sec" % \
		(engineTime, engine.get_kb('numbers').get_stats()[2] / engineTime))

"""


python rule = "bc_numbers.honores_corazones_new(%s, %s)\n" % ($player, $puntos)
		python f.write(rule)

"""

if __name__ == "__main__":
	import sys
	print ("Just for fun, ur name?")
	print (run(eval(sys.argv[1]), int(sys.argv[2])))