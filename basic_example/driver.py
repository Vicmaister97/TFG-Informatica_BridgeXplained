# driver.py

from __future__ import with_statement
import sys
import os
import time
from pyke import knowledge_engine, krb_traceback, goal

engine = knowledge_engine.engine(__file__)
activated = False       
""" 
    Variable "activated" is use for executing backwards chaining several times
    and only execute forward chaining once.
"""

# driver.fc('numbers.honores_corazones_new_post(S, 1)')
def fc(rule_to_prove):
    try:
        #global activated
        #if activated == False:
        # To run several times the forward-chaining test without
        # executing again the engine complete reasoning
        #activated = True

        # Clean files and engine conclussions
        clean()


        # Measure time of the complete reasoning
        start_time = time.time()
        engine.activate('fc_numbers')       # NECESSARY FOR HAVING ALL THE FACTS
        end_time = time.time()
        fc_time = end_time - start_time

        print ("fc time %.2f, %.0f asserts/sec" % \
            (fc_time, engine.get_kb('numbers').get_stats()[2] / fc_time))

        """
        with engine.prove_goal('bc_numbers.honores_corazones_FINAL()') \
          as gen:
            for vars, plan in gen:
                print "SE CONOCEN TODOS LOS PH EN CORAZONES!!!!!\n"
                print plan
        """

        goal = False
        print ("doing proof")
        with engine.prove_goal(str(rule_to_prove)) \
          as gen2:
            for vars, plan in gen2:
                #print "%s tiene %s PH en corazones\n" % (vars['player'], vars['puntos'])
                #print plan
                #print gen2
                goal = True
        if goal == True:
            print("\n------------\nTHE RULE YOU WROTE IS TRUE!!!!!!!!!!\n------------\n")
        else:
            print("\n------------\nThe rule you wrote is False.\n------------\n")


        print ("proof done.")
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

# driver.bc('bc_numbers.honores_corazones_new_post(S, 1)')
def bc(rule_to_prove):
    try:
        global activated
        if activated == False:
            clean()
            engine.activate('fc_numbers')   # NECESSARY FOR HAVING ALL THE FACTS
            engine.activate('bc_numbers')
            activated = True

        """
        with engine.prove_goal('bc_numbers.honores_corazones_FINAL()') \
          as gen:
            for vars, plan in gen:
                print "SE CONOCEN TODOS LOS PH EN CORAZONES!!!!!\n"
                print plan
        """
        goal = False
        with engine.prove_goal(str(rule_to_prove)) \
          as gen2:
            for vars, plan in gen2:
                #print "%s tiene %s PH en corazones\n" % (vars['player'], vars['puntos'])
                #print plan
                #print gen2
                goal = True
        if goal == True:
            print("\n------------\nTHE RULE YOU WROTE IS TRUE!!!!!!!!!!\n------------\n")
        else:
            print("\n------------\nThe rule you wrote is False.\n------------\n")

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

        if midRules == False:   # Empty list
            print ("SE ACABO WEEEEEEEYYYYYY")
            return

        
        # We remove those mid rules from the conclussions file
        with open("midRules.txt", "w") as new_f:
            for followRule in midRules:
                lines.remove(followRule)
            # Write only the rules not to prove
            new_f.writelines(lines)
        
        print (midRules)
        # Now, we have to prove those mid rules
        for followRule in midRules:
            print ("SE VIENE")
            # We run this rule to follow the reasoning
            bc(followRule.rstrip("\n"))

        

    except:
        krb_traceback.print_exc()
        clean()
        #sys.exit(1)

def clean():
    print ("********RESETTING THE PROGRAM********\n\n")
    engine.reset()
    open("midRules.txt", "w").close()
    open("conclusiones.txt", "w").close()
    open("conclusiones_bc.txt", "w").close()


"""


python rule = "bc_numbers.honores_corazones_new(%s, %s)\n" % ($player, $puntos)
        python f.write(rule)

"""

if __name__ == "__main__":
    import sys
    print ("Just for fun, ur name?")
    print (run(eval(sys.argv[1]), int(sys.argv[2])))