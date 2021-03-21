import csv
print("opening csv file")

with open('../data/team_data/ABILENECHRISTIAN.csv', 'r') as file:
    reader = csv.reader(file)
    abilene_test = list(reader)
    total_file_rows = len(list(open("../data/team_data/ABILENECHRISTIAN.csv")))
    row = 1
    column = 8
    number_of_games = 0
    point_diff = 0
    while row < total_file_rows:
        tmm_pts = int(abilene_test[row][column])
        opp_pts = int(abilene_test[row][column+1])
        print(tmm_pts - opp_pts)
        point_diff += (tmm_pts - opp_pts)
        row += 1
        if row == total_file_rows:
            print(point_diff)
