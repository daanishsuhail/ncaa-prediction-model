import csv

# despite what the file name may suggest in statistics, in this project, SRS is an abbreviation for Simple Rating System.

avg_diffs = {}
def SRS(team_avg_diffs, team):
    tad = open(team_avg_diffs, mode='r')
    reader = csv.DictReader(tad)
    l = list(reader)
    avg_diffs = dict()
    for d in l:
        avg_diffs[d["Teams"]] = d["Avg Point Diff"]
    # initial value
    init = avg_diffs[team]
    print(init)