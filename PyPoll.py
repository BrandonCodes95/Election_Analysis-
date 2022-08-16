
#import modules 

import csv 

import os

#chain files together using "join" function
file_to_load = os.path.join("Resources", "Election_results.csv")

file_to_save = os.path.join("Analysis", "election_analysis.txt")

#open file 
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

#read the file object with the reader function. 

    headers = next(file_reader)

    print(headers)


#close file
