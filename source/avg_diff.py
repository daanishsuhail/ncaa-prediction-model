import csv


# Computes the average difference

def difference_average(str):
    # print("opening csv file") REMOVE COMMENTS TO ENABLE SEEING THE "open csv file" MEANT FOR DEBUGGING
    team = str; 
    with open("../data/team_data/"+team+".csv", 'r') as file:
        reader = csv.reader(file)
        abilene_test = list(reader)
        total_file_rows = len(list(open("../data/team_data/RUTGERS.csv")))
        row = 1
        column = 8
        number_of_games = 0
        point_diff = 0
        avg_point_diff = 0.0
        while row < total_file_rows:
            tmm_pts = float(abilene_test[row][column])
            opp_pts = float(abilene_test[row][column+1])
            # print(tmm_pts - opp_pts) REMOVE THE COMMENTS TO SEE THE INDIVIDUAL POINT DIFFERENCE OF EACH GAME
            point_diff += (tmm_pts - opp_pts)
            row += 1
            if row == total_file_rows:
                # print(point_diff) REMOVE THE COMMENTS TO SEE THE TOTALED POINT DIFFERENCES
                avg_point_diff = float(point_diff)/(row-1)
                print(avg_point_diff) # PRINTS THE AVERAGE POINT DIFFERENCE
