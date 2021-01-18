# Module for creating file paths across operating systems
import os
# Module for reading csv files
import csv

# Create file path where the input data is read from
data_csv = os.path.join('PyBank_Resources', 'budget_data.csv')

# Read using csv modeule. Data is separated by ","
with open(data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Read header row and skip to first row of data
    header = next(csv_reader)

    #Assign iterative values
    tot_mo = 0
    net_tot = 0
    prev_profit = 0
    ch = 0
    # Holds all changes in month-to-month Profit/Losses
    ch_list = []
    # Holds greatest of all time iteratve data
    goat_inc = [0,0]
    goat_dec = [0,0]

    # Iterate down each row (header was skipped)
    for row in csv_reader:
        # Counts each row of data as 1 month and sums total
        tot_mo += 1
        # Captures net total amount of "Profit/Losses" over the entire period
        net_tot += int(row[1])
        # Captures changes in month-to-month Profit/Losses
        ch = int(row[1]) - prev_profit
        ch_list.append(ch)
        # Captures greatest of all time iterative data
        if ch > int(goat_inc[1]):
            goat_inc[0] = row[0]
            goat_inc[1] = ch
        elif ch < int(goat_dec[1]):
            goat_dec[0] = row[0]
            goat_dec[1] = ch
        prev_profit = int(row[1])

    # Function calculates averages
    def average(numbers):
        length = len(numbers)
        total = 0.0
        for number in numbers:
            total += number
        return total / length

# Print output data to the terminal    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {tot_mo}")
print(f"Total: ${net_tot}")
print(f"Average Change: ${round(average(ch_list[1:]), 2)}")
print(f"Greatest Increase in Profits: {goat_inc[0]} (${goat_inc[1]})")
print(f"Greatest Decrease in Profits: {goat_dec[0]} (${goat_dec[1]})")

# Create file path where the output data is written to
output_path = os.path.join("PyBank_Analysis", "PyBank_Output.txt")
# Write output data to the output file
with open(output_path, "w", newline = '') as output_file:
    writer = csv.writer(output_file)
    writer.writerow([f"Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Month: ${net_tot}"])
    writer.writerow([f"Average Change: ${round(average(ch_list[1:]), 2)}"])
    writer.writerow([f"Greatest Increase in Profits: {goat_inc[0]} (${goat_inc[1]})"])
    writer.writerow([f"Greatest Decrease in Profits: {goat_dec[0]} (${goat_dec[1]})"])