
#import modules 

import csv 

import os

#chain files together using "join" function
file_to_load = os.path.join("Resources", "Election_results.csv")

file_to_save = os.path.join("Analysis", "election_analysis.txt")



#assign variable to count the votes 

total_votes = 0 

#Print Canidate names from each row with list
candidate_options = []

#create dictionary to hold candidate name as keys and votes each got as values 
candidate_votes = {}

#set empty variables for the winner to be decided 

winning_candidate = ""

winning_count = 0 

winning_percentage = 0 

#open file 
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

#read the file object with the reader function. 

    headers = next(file_reader)

    #Print each row in CSV 

    for row in file_reader:

        total_votes += 1 
    

        #print canidate name fron each row 
        candidate_name = row[2]

        #set conditional to only get the names that were not added already
        if candidate_name not in candidate_options: 


        #add naes of candidates to canidate option list 
            candidate_options.append(candidate_name)

        # begin tracking candidate vote count 
            candidate_votes[candidate_name] = 0 

        candidate_votes[candidate_name] += 1 

print(candidate_votes) 

for candidate_name in candidate_votes: 

    #retrieve vote count of a candidate 
    votes = candidate_votes[candidate_name]

    #calculate percentage of votes. 
    vote_percentage = float(votes) / float(total_votes) * 100 

    #print the candidate name and percentage of votes to terminal. 

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage): 
        #if true then set winning_count = votes and winning_percent = vote_percentage 

        winning_count = votes 

        winning_percentage = vote_percentage 


        winning_candidate = candidate_name 

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:>1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)


#close file
