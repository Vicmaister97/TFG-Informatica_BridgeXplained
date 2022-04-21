## AUTHOR AND GENERAL VIEW OF THE CODE


from __future__ import with_statement
import sys
import os
import time
from pyke import knowledge_engine, krb_traceback, goal
sys.path.append("class/")
from ManageGame import *

"""
######## ######## VARIABLES ######## ########
"""

engine = knowledge_engine.engine(__file__)

""" 
Variable "activated" is use for executing forward or backwards chaining several times
    and only execute the complete engine reasoning once.
"""
isActiveFC = False
isActiveBC = False


performingProof = False     # Used for not trying to proove middle rules that we know are true
exception = False           # For exception handling

# USER MESSAGES
TRUE_RULE = "\n------------\n%s\nTHE RULE YOU WROTE IS TRUE!!!!!!!!!!\n------------\n"
FALSE_RULE = "\n------------\n%s\nThe rule you wrote is False.\n------------\n"
RESET = "\n\n********RESETTING THE PROGRAM********\n\n"
START = "\n\n********STARTING THE PROGRAM********\n\n"
END_PROOF = "\n\nEND PROOF of %s.\n------------------------------------\n\n\n"

# FILES VARIABLES
F_REASONING = "reasoning/"
F_MID_RULES = F_REASONING + "midRules.txt"
F_CONCLUSIONS = F_REASONING + "conclusiones.txt"
F_CONCLUSIONS_BC = F_REASONING + "conclusiones_bc.txt"

def fc():
    try:
        global isActiveFC
        if isActiveFC == False:
            # Clean files and engine conclussions
            cleanStart()

            # Run the engine and measure time of the complete FC reasoning
            runEngine('fc_numbers')

            ManageGame.printGame()

            # To run several times the forward-chaining test without
            # executing again the engine complete reasoning
            isActiveFC = True
            engine.print_stats()

        begin()

        """
        # TRY TO SEE IF WE CAN ACCESS ENGINE RELATIONS
        numbers.honores_corazones_FINAL($tot)
        # Now we read the conclusions
        file = open("conclussions.txt", "r")
        list_of_conclussions = file.readlines()
        for conclussion in list_of_conclussions
        """

    except:
        krb_traceback.print_exc()
        cleanReset()
        #sys.exit(1)


# driver.fc_proove('numbers.honores_corazones_new_post(S, 1)')
def fc_proove(rule_to_prove):
    fc()

    try:
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
        print ("Performing the proof:")
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
            print(TRUE_RULE) % (rule_to_prove)
        else:
            print(FALSE_RULE) % (rule_to_prove)


        # Measure time of the proof
        endTime = time.time()
        proofTime = endTime - startTime

        print ("Proof done.")
        print ("Proof time: %.4f seconds" % (proofTime))

    except:
        krb_traceback.print_exc()
        cleanReset()
        #sys.exit(1)


# driver.bc('bc_numbers.honores_corazones_new_post(S, 1)', True)
def bc(rule_to_prove, isInitialProof):
    try:
        global isActiveBC
        global isActiveFC
        global performingProof
        global exception

        if isActiveFC == False:
            # Clean files and engine conclussions
            cleanStart()

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
            begin()
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
        begin()
        goal = False

        if isInitialProof == True:
            print ("Performing the proof:")
        else:
            print ("Performing the sub-proof:")

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
                print(TRUE_RULE) % (rule_to_prove)
            else:
                print(FALSE_RULE) % (rule_to_prove)
                # Measure time of the proof
                endTime = time.time()
                proofTime = endTime - startTime

                print ("Proof done.")
                print ("Proof time: %.4f seconds" % (proofTime))
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

            print ("Proof done.")
            print ("Proof time: %.4f seconds" % (proofTime))


            # Leave some empty space in the conclussions_bc file for
            # future proofs
            with open(F_CONCLUSIONS_BC, "a") as f:
                f.write(END_PROOF % (rule_to_prove))

            return

        performingProof = True
        
        # We remove those mid rules from the conclussions file
        # We leave only the final facts
        with open(F_MID_RULES, "w") as new_f:
            for followRule in midRules:
                lines.remove(followRule)

            # Write only the rules not to prove (final facts)
            new_f.writelines(lines)
            
        print (midRules)
        # Now, we have to prove those mid rules
        for followRule in midRules:
            while performingProof:
                print ("SE VIENE %s") % (followRule)
                # We run this rule to follow the reasoning
                bc(followRule.rstrip("\n"), False)


        if isInitialProof == True:
            # Measure time of the proof
            endTime = time.time()
            proofTime = endTime - startTime

            if exception == False:
                print ("Proof done.")
                # Leave some empty space in the conclussions_bc file for
                # future proofs
                with open(F_CONCLUSIONS_BC, "a") as f:
                    f.write(END_PROOF % (rule_to_prove))
            else:
                print ("Proof done. It's not a complete proof as there was an exception.")
            print ("Proof time: %.4f seconds" % (proofTime))


    except:
        krb_traceback.print_exc()
        cleanReset()
        #sys.exit(1)


""" -------- AUXILIARY METHODS -------- """
def begin():
    print ("\n")


def cleanStart():
    print (START)

    # In the start we clean previous conclussions files
    #   and the engine
    cleanFiles()

    cleanEngine()


def cleanReset():
    global exception

    print (RESET)

    cleanEngine()

    # Delete Game info
    ManageGame.delete()

    # Set global variable
    exception = True


def cleanFiles():
    # Clean files
    open(F_MID_RULES, "w").close()
    open(F_CONCLUSIONS, "w").close()
    open(F_CONCLUSIONS_BC, "w").close()


def cleanEngine():
    global isActiveBC
    global isActiveFC
    global performingProof
    global exception

    engine.reset()

    # Clean global variables
    isActiveFC = False
    isActiveBC = False
    performingProof = False
    exception = False



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
    print (reasoningType + " engine time: %.6f seconds, %.0f asserts/sec" % \
        (engineTime, engine.get_kb('numbers').get_stats()[2] / engineTime))

"""


python rule = "bc_numbers.honores_corazones_new(%s, %s)\n" % ($player, $puntos)
        python f.write(rule)

"""

if __name__ == "__main__":
    import sys
    print ("Just for fun, ur name?")
    print (run(eval(sys.argv[1]), int(sys.argv[2])))