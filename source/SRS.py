import csv

# despite what the file name may suggest in statistics, in this project, SRS is an abbreviation for Simple Rating System.

# this is the function responsible for actually calculating every SRS

def calcSRS(atdDict, confSpread, confProp, iterations):
    # STRUCTURE:
    
    if (iterations > 0):
        # i = the dictionary of teams with their avg. point diff * their respective confProp
        oldest = {}
        # Loop through teams (conf)
        for t in atdDict:
            atd = atdDict[t]
            conR = confProp[confSpread[t]]
            oldest[t] = float(atd) * float(conR)/64
        
        z = 0
        old = {}
        new = {}
        while z < iterations-1:
            new = __calcSRS(oldest, old)
            old = new
            z += 1

        return old
    else:
        return atdDict

def __calcSRS(marginDict, rDict):
    # newDict = the returning value
    newDict = dict()

    for t, r in marginDict.items():
        TOTAL = 0
        for t1, r1 in rDict.items():
            if t1 != t:
                TOTAL += r1
        avg = TOTAL/((len(rDict))-1)
        newDict[t] = r-avg
    
    return newDict

def calcSRS(atdDict):
    d = dict()
    return d

# This only works for CSVs structured like a dictionary. Essentially, they can only have two headers:
# One that functions like a key, and one that functions like the value w/ the key provided
def csvToDict(csvPath, keyHeader, valHeader):
    c = open(csvPath, mode='r')
    reader = csv.DictReader(c)
    l = list(reader)
    d = dict()
    for d1 in l:
        d[d1[keyHeader]] = d1[valHeader]
    return d

def mergeListsAsDict(keys, vals):
    d = dict()
    if len(keys) == len(vals):
        for k in keys:
            d[k] = vals[keys.index(k)]
    return d

# This function returns an entire column as a list.
def parseCSV(csvPath, colNum, rowStart):
    l = list()
    file = open(csvPath, mode='r')
    reader = csv.reader(file)
    parsed = list(reader)
    rows = len(list(open(csvPath)))
    for r in range(rowStart, rows):
        l.append(parsed[r][colNum])
    return l