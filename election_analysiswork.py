
import os
import csv
file_to_load = 'C:/Users/priya/Downloads/election_analysisfile.csv'
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    #for row in file_reader:
    headers = next(file_reader)
    print(headers)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")


# Close the file
outfile.close()
