import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    candidates = []
    rowcount = 0
    votesforkhan = []
    votesforcorrey = []
    votesforli = []
    votesforotooley = []
    percentages = []
    
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
        rowcount += 1
        
        if row[2] == "Khan":
            votesforkhan.append(row[0])
        elif row[2] == "Correy":
            votesforcorrey.append(row[0])
        elif row[2] == "Li":
            votesforli.append(row[0])
        elif row[2] == "O'Tooley":
            votesforotooley.append(row[0])
            

        
    percentkhan = (int(len(votesforkhan))/int(rowcount))*100
    percentages.append(percentkhan)
    
    percentcorrey = (int(len(votesforcorrey))/int(rowcount))*100
    percentages.append(percentcorrey)

    percentli = (int(len(votesforli))/int(rowcount))*100
    percentages.append(percentli)
    
    percentotooley = (int(len(votesforotooley))/int(rowcount))*100
    percentages.append(percentotooley)
    
    maxpercent = max(percentages)
    
    for percent in percentages:
        if maxpercent == percentkhan:
            winner = "Khan"
        elif maxpercent == percentcorrey:
            winner = "Correy"
        elif maxpercent == percentli:
            winner = "Li"
        elif maxpercent == percentotooley:
            winner = "O'Tooley"
            
    f = open('election.txt', 'w')
    
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(rowcount))
    print("Khan: " + str(percentkhan) + "%; Number of votes: " + str(len(votesforkhan)))
    print("Correy: " + str(percentcorrey) + "%; Number of votes: " + str(len(votesforcorrey)))
    print("Li: " + str(percentli) + "%; Number of votes: " + str(len(votesforli)))
    print("O'Tooley: " + str(percentotooley) + "%; Number of votes: " + str(len(votesforotooley)))
    print("----------------------------")
    print("Winnner: " + str(winner))
    print("----------------------------")
    
    f.close()
            
            
    
    
    

        
    
        