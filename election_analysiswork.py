
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
    
    for candidate_name in candidate_votes:
        if candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            votes = int(votes)
            votesperc = (votes/ total_votes) * 100
            print(f"Total vote% received by {candidate_name} is {round(votesperc,2)}%")
            #vote% = votes/total_votes
            #print(f"vote for candidate {candidate_name : " {votes%})
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")


# Close the file
outfile.close()
