
class DriverSentences:

	### USER MESSAGES
	TRUE_RULE = "\n------------\n%s\nTHE RULE YOU WROTE IS TRUE!!!!!!!!!!\n------------\n"
	FALSE_RULE = "\n------------\n%s\nThe rule you wrote is False.\n------------\n"
	RESET_S = "\n\n******** RESETTING BridgeXplained ********\n\n"
	START = "\n\n******** STARTING BridgeXplained ********\n%s\n\n"

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