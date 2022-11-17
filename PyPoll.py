#The data we need to retrieve
#The total number of votes cast 369711
# A complete list of candidates who received votes ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
#The percentage of votes each candidate won
#The total number of votes each candate won 'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606
#The winner of the election based on popular vote

#add dependencies
import os

import csv
#assign variable
file_to_laod = os.path.join("resources" , "election_results.csv")
#assign variable to save path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate List
candidate_options = []

#candidate_votes
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open file 
with open(file_to_laod) as election_data:

    file_reader = csv.reader(election_data)

    #Read and print header row
    headers = next(file_reader)

    #Print each row
    for row in file_reader:

        total_votes +=1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
         
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
    f"\nElection Results\n"
    f"------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"------------------\n")
    
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)