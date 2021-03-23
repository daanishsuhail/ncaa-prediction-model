import csv

# despite what the file name may suggest in statistics, in this project, SRS is an abbreviation for Simple Rating System.

# this is the function responsible for actually calculating every SRS

def calcSRS(atdDict, confSpread, confProp, iterations):
    # STRUCTURE:
    # this recursive calculation is split in two parts:
    # 1) the merge between the conference weight
    # 2) the recursive calculation of:
    #       - constant: team's average point differential
    #       - variable: the average of every other team's rating
    #    the final result of one iteration is the constant minus the variable.
    #    this means that the variable will rapidly approach the final calculation, where the constant will not change
    # after "iterations" number of iterations, the absolute result is returned.

    # if this explanation is not clear enough, do not hesitate to ask questions.
    # it is not recommended that you change anything in any of these functions without full knowledge over how the code was written.

    if (iterations > 0):
        z = 0
        # the purpose of old and new
        # old and new are what allow the recursion to process correctly.
        oldest = {}

        for t in atdDict:
            # atd = the average point differential for team "t"
            atd = atdDict[t]
            # conR = conference ratio of team "t"
            conR = confProp[confSpread[t]]
            oldest[t] = (float(atd) * float(conR))/64
        
        # old = the old dictionary of variable ratings
        old = oldest
        # new = the new dictionary of variable ratings
        new = {}

        # 
        while z < iterations-1:
            new = __calcSRS(oldest, old)
            old = new
            z += 1

        return old
    else:
        # incase we just want the actual average point differentials of each team instead, just set iterations to zero.
        # then it will return what was inputted into the function in the first place.
        return atdDict

def __calcSRS(marginDict, rDict):
    # newDict = the returning value
    newDict = dict()

    for t, r in marginDict.items():
        TOTAL = 0
        for t1, r1 in rDict.items():
            if t1 != t:
                TOTAL += float(r1)
        avg = TOTAL/((len(marginDict))-1)
        newDict[t] = r+avg
    
    return newDict

def calcSRS(atdDict):
    d = dict()
    return d

