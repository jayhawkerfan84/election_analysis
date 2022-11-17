#The data we need to retrieve
#The total number of votes cas
# A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candate won
#The winner of the election based on popular vote

#add dependencies
import os

import csv
#assign variable
file_to_laod = os.path.join("resources" , "election_results.csv")
#assign variable to save path
file_to_save = os.path.join("analysis", "election_analysis.txt")


#Open file 
with open(file_to_laod) as election_data:

    file_reader = csv.reader(election_data)

    #Read and print header row
    headers = next(file_reader)
    print(headers)