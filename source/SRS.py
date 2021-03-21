import csv

# despite what the file name may suggest in statistics, in this project, SRS is an abbreviation for Simple Rating System.

avg_diffs = {}
def SRS(team_avg_diffs, team):
    tad = open(team_avg_diffs, mode='r')
    reader = csv.DictReader(tad)
    for k, v in reader:
        avg_diffs[k] = v
        print(k+', '+v)
    # initial value
    init = avg_diffs[team]