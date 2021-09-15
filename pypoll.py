
import csv
import os
from typing import Text
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a Variable to save tthe file to a pth
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total votes counter
total_votes = 0
#Candidate options 
candidate_options = []
#declare the empty dictionary 
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#OPEN the election results and read the file
with open(file_to_load) as election_data:
#To do: read and analyze the data here 
    file_reader = csv.reader(election_data)
    #READ the header row
    headers = next(file_reader) 
    #Print each row in the CSV file 
    for row in file_reader:
 # 2. Add to the total vote count 
        total_votes += 1 
    #Print the candidate name from  each row 
        candidate_name = row[2]
    #If the candidate does not match any exissting candidate 
        if candidate_name not in candidate_options:
            #Add it to the list 
            candidate_options.append(candidate_name)
            #Begin tracking candidate's vote count 
            candidate_votes[candidate_name] = 0
        #Add a vote to the candidates name 
        candidate_votes[candidate_name]+= 1
        #Save the results to our text file 
with open (file_to_save, "w") as txt_file:
    election_results = (
    f"\nElection Results\n"
    f"\n-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"---------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)


        # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
     # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the
    # terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

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
    #save the winning candidates result to the text file 
    txt_file.write(winning_candidate_summary)