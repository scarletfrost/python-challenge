import os
import csv

# cvs file path
csvpath = os.path.join('Resources', 'election_data.csv')

#creating empty variables
tot_votes = 0
winner = 0
votes = 0
win_votes = 0
# dictionary for counting candidates and their votes
poll_count = {}

# read csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # to skip the header row
    csv_header = next(csvreader)
    csvreader = list(csvreader)   
    
    #calculations
    for i in csvreader:
	# find the total votes
        tot_votes = tot_votes + 1
        # counting votes per candidates
        cand = i[2]
        # checking for same candidates
        if cand in poll_count:     
            poll_count[cand] = poll_count[cand] + 1 
        else: 
	    #add vote for candidate
            poll_count.update({cand:1})

#calculate the percentage and winner
# dictionary for holding results
poll_results = {}
for cand, votes in poll_count.items():
    poll_results[cand] = str(votes*100/tot_votes) +'% (' + str(votes)+ ')'
    if votes > win_votes:
        win_votes = votes 
        winner = cand



# printing the analysis to the terminal
print("Election Results")
print("--------------------------------------------------------")
print(f"Total Votes: {tot_votes} ")
print("--------------------------------------------------------")
#looping dictionary for results
for i, j in poll_results.items():
	print(i + ': '+ j)
print("--------------------------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------------------------")
		  
# exporting the analysis to a text file
output_path = os.path.join("ElectionResults.txt")
    
# Open the file using "write" mode
with open(output_path, 'w', newline='') as txtfile:
	txtfile.write("Election Results")
	txtfile.write('\n' + "---------------------------------------------------------"+ '\n')
	txtfile.write(f"Total Votes: {tot_votes}")
	txtfile.write('\n' + "---------------------------------------------------------"+ '\n')
	#looping dictionary for results
	for i, j in poll_results.items():
		txtfile.write( i + ': '+ j + '\n')	
	txtfile.write("---------------------------------------------------------"+ '\n')
	txtfile.write(f"Winner: {winner}")
	txtfile.write('\n' + "---------------------------------------------------------")
