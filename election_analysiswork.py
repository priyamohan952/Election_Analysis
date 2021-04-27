
import os
import csv
file_to_load = 'C:/Users/priya/Downloads/election_analysisfile.csv'
total_votes = 0
candidate_list = []
candidate_votes = {}
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    #for row in file_reader:
    headers = next(file_reader)
    #candidate_votes[candidate] = 0
    for row in file_reader:
        total_votes = total_votes + 1
        candidate = row[2]
        
        if candidate not in candidate_list:
         candidate_list.append(candidate)
         candidate_votes[candidate] = 0
        candidate_votes[candidate] +=1
    #print(total_votes)
    #print(candidate_list)
    print(candidate_votes)
    winning_perc = 0
    winning_name = ""
    winning_votes = 0
    for candidate_name in candidate_votes:
        if candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            votes = int(votes)
            votesperc = (votes/ total_votes) * 100
            print(f"Total vote% received by {candidate_name} is {votesperc: .1f}% \n")
            
            
# check the winning candidate name
        if (votesperc > winning_perc):
            winning_perc = votesperc
            winning_name = candidate_name
            winning_votes = votes
    print(f"Winning candidate is {winning_name}. \n He received {winning_votes} votes and received a winning % of {round(winning_perc,2)}%")

    # winning candidate summary
    print(f"Winning candidate is : {winning_name} \nWinning votes is : \
    {winning_votes} votes \nWinning Percentage is : {winning_perc : .1f}%")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")


# Close the file
outfile.close()
