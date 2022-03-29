# driver.py

from __future__ import with_statement
import sys
import os
import time
from pyke import knowledge_engine, krb_traceback, goal

engine = knowledge_engine.engine(__file__)
activatedFC = False
activatedBC = False
""" 
    Variable "activated" is use for executing forward or backwards chaining several times
    and only execute the complete engine reasoning once.
"""

performingProof = False

TRUE_RULE = "\n------------\nTHE RULE YOU WROTE IS TRUE!!!!!!!!!!\n%s\n------------\n"
FALSE_RULE = "\n------------\nThe rule you wrote is False.\n%s\n------------\n"
RESET = "\n\n********RESETTING THE PROGRAM********\n\n"

# driver.fc('numbers.honores_corazones_new_post(S, 1)')
def fc():
    try:
        global activatedFC
        if activatedFC == False:
            # Clean files and engine conclussions
            clean()

            # Measure time of the complete reasoning
            start_time = time.time()
            engine.activate('fc_numbers')
            end_time = time.time()
            fc_time = end_time - start_time

            print ("FC reasoning time: %.4f seconds, %.0f asserts/sec" % \
                (fc_time, engine.get_kb('numbers').get_stats()[2] / fc_time))

            # To run several times the forward-chaining test without
            # executing again the engine complete reasoning
            activatedFC = True


        engine.print_stats()


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
        clean()
        #sys.exit(1)

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

        goal = False
        print ("Performing the proof:")
        # Measure time of the proof
        start_time = time.time()


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
        end_time = time.time()
        proof_time = end_time - start_time

        print ("Proof done.")
        print ("Proof time: %.4f seconds" % (proof_time))

    except:
        krb_traceback.print_exc()
        clean()
        #sys.exit(1)


# driver.bc('bc_numbers.honores_corazones_new_post(S, 1)')
def bc(rule_to_prove, initialProof):
    try:
        global activatedBC
        global activatedFC
        global performingProof

        if activatedFC == False:
            # Clean files and engine conclussions
            clean()

            # Measure time of the complete reasoning
            start_time = time.time()
            engine.activate('fc_numbers')       # NECESSARY FOR HAVING ALL THE FACTS
            end_time = time.time()
            fc_time = end_time - start_time

            print ("FC reasoning time: %.4f seconds, %.0f asserts/sec" % \
                (fc_time, engine.get_kb('numbers').get_stats()[2] / fc_time))

            # To run several times the forward-chaining test without
            # executing again the engine complete reasoning
            activatedFC = True

        if activatedBC == False:

            # Measure time of the complete reasoning
            start_time = time.time()
            engine.activate('bc_numbers')
            end_time = time.time()
            bc_time = end_time - start_time

            print ("BC reasoning time: %.6f seconds, %.0f asserts/sec" % \
                (bc_time, engine.get_kb('numbers').get_stats()[2] / bc_time))
            
            # To run several times the forward-chaining test without
            # executing again the engine complete reasoning
            activatedBC = True


        """
        with engine.prove_goal('bc_numbers.honores_corazones_FINAL()') \
          as gen:
            for vars, plan in gen:
                print "SE CONOCEN TODOS LOS PH EN CORAZONES!!!!!\n"
                print plan
        """

        goal = False
        if (initialProof == True):
            print ("Performing the proof:")
        else:
            print ("Performing the sub-proof:")
        # Measure time of the proof
        start_time = time.time()


        with engine.prove_goal(str(rule_to_prove)) \
          as gen2:
            for vars, plan in gen2:
                #print "%s tiene %s PH en corazones\n" % (vars['player'], vars['puntos'])
                #print plan
                #print gen2
                goal = True

        if (initialProof == True):
            if goal == True:
                print(TRUE_RULE) % (rule_to_prove)
            else:
                print(FALSE_RULE) % (rule_to_prove)
                # Measure time of the proof
                end_time = time.time()
                proof_time = end_time - start_time

                print ("Proof done.")
                print ("Proof time: %.4f seconds" % (proof_time))
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
        with open("midRules.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if "bc_numbers" in line:
                    # This means that we still have rules to prove
                    # We add the rule
                    midRules.append(line)

        if not midRules:   # Empty list
            print ("SE ACABO WEEEEEEEYYYYYY")

            # Measure time of the proof
            end_time = time.time()
            proof_time = end_time - start_time

            print ("Proof done.")
            print ("Proof time: %.4f seconds" % (proof_time))
            return

        performingProof = True
        
        # We remove those mid rules from the conclussions file
        # We leave only the final facts
        with open("midRules.txt", "w") as new_f:
            for followRule in midRules:
                lines.remove(followRule)

            # Write only the rules not to prove (final facts)
            new_f.writelines(lines)
            
        print (midRules)
        # Now, we have to prove those mid rules
        for followRule in midRules:
            while (performingProof):
                print ("SE VIENE %s") % (followRule)
                # We run this rule to follow the reasoning
                bc(followRule.rstrip("\n"), False)

        if initialProof == True:
            # Measure time of the proof
            end_time = time.time()
            proof_time = end_time - start_time

            print ("Proof done.")
            print ("Proof time: %.4f seconds" % (proof_time))


    except:
        krb_traceback.print_exc()
        clean()
        #sys.exit(1)

def clean():
    global activatedBC
    global activatedFC
    global performingProof

    print (RESET)
    engine.reset()

    # Clean files
    open("midRules.txt", "w").close()
    open("conclusiones.txt", "w").close()
    open("conclusiones_bc.txt", "w").close()
    
    # Clean global variables
    activatedFC = False
    activatedBC = False
    performingProof = False


"""


python rule = "bc_numbers.honores_corazones_new(%s, %s)\n" % ($player, $puntos)
        python f.write(rule)

"""

if __name__ == "__main__":
    import sys
    print ("Just for fun, ur name?")
    print (run(eval(sys.argv[1]), int(sys.argv[2])))