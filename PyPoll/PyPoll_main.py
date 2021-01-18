# Module for creating file paths across operating systems
import os
# Module for reading csv files
import csv

# Create file path where the input data is read from
data_csv = os.path.join('PyPoll_Resources', 'election_data.csv')

# Read using csv modeule. Data is separated by ","
with open(data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # Read header row and skip to first row of data
    header = next(csv_reader)

    #Assign iterative value and make empty candidate list
    tot_vote = 0
    candidate_ls = []
    # Holds copy of the data to run through csv a second time after completing candidate_ls
    csv_reader2 = []

    # Iterate down each row (header was skipped)
    for row in csv_reader:
        # Assume each Voter ID is unique
        tot_vote += 1
        # Append each row to copy of data
        csv_reader2.append(row)
        # Append each unique candidate in election_data to candidate_ls
        if row[2] not in candidate_ls:
            candidate_ls.append(row[2])

    # Create candidate dictionary (name:votes)
    can_dict = {name: 0 for name in candidate_ls}

    # Iterate down each row (header was skipped first time around)
    for row in csv_reader2:
        # For (k)ey, (v)alue in every candidate dictionary item
        for k,v in can_dict.items():
            # If position equals the key (candidate name), add 1 vote
            if row [2] == k:
                can_dict[k] += 1

#Prints in terminal
print("Election Results")
print ("-------------------------")
print(f"Total Votes: {tot_vote}")
print ("-------------------------")

# Holds results for each unique candidate
results_ls = []

# Initialize variable to hold highest candidate vote
win_vote = 0

#for k,v in can_dict.items():
#    print (f"{k}: {round((v/tot_vote)*100,2)}% ({v})")

# For (k)ey, (v)alue in every candidate dictionary item
for k,v in can_dict.items():
    # Append the results list
    results_ls.append(f"{k}: {round((v/tot_vote)*100,2)}% ({v})")
    # Check if the iterative candidate's votes is greater than current win_vote
    if v > win_vote:
        winner = k
        win_vote = v

# Print each esult in results_ls on a new line in terminal
for result in results_ls:
    print (result)

#Prints in terminal
print ("-------------------------")
print(f"Winner: {winner}")
print ("-------------------------")

# Create file path where the output data is written to
output_path = os.path.join("PyPoll_Analysis", "PyPoll_Output.txt")

# Write output data to the output file
with open(output_path, "w", newline = '') as output_file:
    writer = csv.writer(output_file, delimiter = ',')
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {tot_vote}"])
    writer.writerow(["-------------------------"])
    for result in results_ls:
        writer.writerow([result])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["-------------------------"])