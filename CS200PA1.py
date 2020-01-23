"""
Jake Gaughan

CS200 Programming Assignment 1

Purpose: Computer Assisted Logical Truth Tables
            Take in group of string logical statements and return whether or not statement in question is true/false/n/a
Outside Code:
    n/a
Outside Collaboration:
    n/a
Sample Output:
>>> %Run CS200PA1.py
enter prove prompt: prove(‘A or not C’, ‘(A and B) or not C’, ‘C or B’))
True
>>> 
Time Spent:
3 hrs
"""

CAPITALS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
logic_stats = ["not", "or", "and"]

def store_input(group_of_logic):
    """
    purpose of this function is to store the input as a set of strings
    inputs:
        input string
    outputs:
        cleaned set of inputs
    """
    inputs = []
    store =""
    count = 0
    #for the length of the statement (minus the "prove" at the beginning)
    for i in range(len(group_of_logic) - 6):
        z = 6 + i
        letter = group_of_logic[z]
        #figuring out the beginning / end of the boolean statement
        if letter == "‘" or letter == "’":
            count += 1
        #if it isn't a comma
        elif letter != "," :
            #add to current string
            store += letter
        #if it is the end of the statement then add the statement to the set and prepare for next statement
        if count == 2:
            inputs.append(store)
            store = ""
            count = 0
    #return the set
    return inputs

def get_variables(inputs):
    """
    purpose of this function is to figure out which variables are in the boolean statements
    inputs:
        set of inputs
    outputs:
        set of variables
    """
    variables = []
    #iterating through all sep. inputs
    for i in range(len(inputs)):
        statement = inputs[i]
        for j in range(len(statement)):
            #if the letter is capitalized and hasn't already been added, add it to the set
            if statement[j] in CAPITALS and not statement[j] in variables:
                variables.append(statement[j])
    #return the set of variables
    return variables

def truth_table(inputs, variables):
    """
    purpose of this funciton is to mimic a truth table and implement a proof by exhaustion
    inputs:
        set of all inputs
        set of all variables
    outputs:
        set of dictionaries
            each dictionary contains the boolean inputs that resulted in "True" for truth inputs
    """
    corrects = []
    #for every row of the truth table
    for c in range(2**(len(variables))):
        check = 0
        keys = {}
        #for every truth input statement
        for i in range(len(inputs) - 1):
            #select a specific truth input
            statement = inputs[i + 1]
            test = ""
            #iterate through the selected statement
            for j in range(len(statement)):
                #if the letter is a variable
                if statement[j] in variables:
                    #figuring out which variable the letter is
                    for letter in range(len(variables)):
                        if statement[j] == variables[letter]:
                            z = letter + 1
                            #figuring out how often the variable is supposed to oscilate between true and false
                            split = (2**(len(variables))) / (2**z)
                            break
                    #oscilating True
                    if ((split + c)//split) % 2 == 1:
                        keys[statement[j]] = "True"
                        test += "True"
                    #oscilating False
                    else:
                        keys[statement[j]] = "False"
                        test += "False"
                #if the letter is not a variable
                else:
                    test += statement[j]
            #if the truth input is actually true
            if eval(test):
                check += 1
            #if all truth inputs are true for a given row
            if check == (len(inputs) - 1):
                #append the dictionary of correct inputs
                corrects.append(keys)
    #return the set of correct inputs
    return corrects

def final_step(corrects, inputs):
    """
    purpose of this function is to test out the test input with the variables that we know result in truths from the input statements
    inputs:
        corrects, returned from truth_table
        inputs, the set of input statements
    outputs:
        n/a

    """
    #the first statement in inputs is the test input
    test = inputs[0]
    results = []
    #if there is nothing in corrects
    if len(corrects) == 0:
        print("not enough information")
        return
    #for every thing in corrects
    for j in range(len(corrects)):
        #selecting specific dictionary
        test_bools = corrects[j]
        test2 = ""
        #for every letter in the test statement
        for i in range(len(test)):
            #substitute the variables with boolean values
            if test[i] in test_bools.keys():
                test2 += test_bools[(test[i])]
            else:
                test2 += test[i]
        #add the boolean value of the statement to the result set
        results.append(eval(test2))
    #for all results
    for x in range(len(results) - 1):
        #if the results do not match
        if results[x+1] != results[x]:
            #inconclusive
            print("not enough information")
            return
    #if all of the results do match, print the result
    print(results[0])




if __name__ == "__main__":
    original = input("enter prove prompt: ")
    inputs = store_input(original)
    variables = get_variables(inputs)
    corrects = truth_table(inputs, variables)
    final_step(corrects,inputs)
