import os
import csv

data_csv = os.path.join('PyPoll_Resources', 'election_data.csv')

with open(data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    header = next(csv_reader)

    tot_vote = 0
    candiate_ls = []

    for row in csv_reader:
        tot_vote += 1
        if row[2] not in candiate_ls:
            candiate_ls.append(row[2])


print("Election Results")
print ("-------------------------")
print(f"Total Votes: {tot_vote}")
print ("-------------------------")
print(candiate_ls)