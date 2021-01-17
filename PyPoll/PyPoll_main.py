import os
import csv

data_csv = os.path.join('PyPoll_Resources', 'election_data.csv')

with open(data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    header = next(csv_reader)

    tot_vote = 0
    candidate_ls = []
    # Holds copy of the data to run through csv a second time
    csv_reader2 = []

    for row in csv_reader:
        # Assume each Voter ID is unique
        tot_vote += 1
        csv_reader2.append(row)
        if row[2] not in candidate_ls:
            candidate_ls.append(row[2])

    # Create candidate dictionary (name:votes)
    can_dict = {name: 0 for name in candidate_ls}

    for row in csv_reader2:    
        for k,v in can_dict.items():        
            if row [2] == k:
                can_dict[k] += 1

print("Election Results")
print ("-------------------------")
print(f"Total Votes: {tot_vote}")
print ("-------------------------")

for k,v in can_dict.items():
    print (f"{k}: {round((v/tot_vote)*100,2)}% ({v})")

