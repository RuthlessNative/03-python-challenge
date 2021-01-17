import os
import csv

data_csv = os.path.join('PyBank_Resources', 'budget_data.csv')

with open(data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    header = next(csv_reader)

    tot_mo = 0
    net_tot = 0
    prev_profit = 0
    ch_list = []
    ch = 0
    goat_inc = [0,0]
    goat_dec = [0,0]

    for row in csv_reader:
        tot_mo += 1
        net_tot += int(row[1])
        ch = int(row[1]) - prev_profit
        ch_list.append(ch)
        if ch > int(goat_inc[1]):
            goat_inc[0] = row[0]
            goat_inc[1] = ch
        elif ch < int(goat_dec[1]):
            goat_dec[0] = row[0]
            goat_dec[1] = ch
        prev_profit = int(row[1])

    def average(numbers):
        length = len(numbers)
        total = 0.0
        for number in numbers:
            total += number
        return total / length
    
    #write this as a list? and then print here and in with open?
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {tot_mo}")
    print(f"Total: ${net_tot}")
    print(f"Average Change: ${round(average(ch_list[1:]), 2)}")
    print(f"Greatest Increase in Profits: {goat_inc[0]} (${goat_inc[1]})")
    print(f"Greatest Decrease in Profits: {goat_dec[0]} (${goat_dec[1]})")

output_path = os.path.join("PyBank_Analysis", "PyBank_Output.txt")

with open(output_path, "w", newline = '') as output_file:
    writer = csv.writer(output_file)
    writer.writerow([f"Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Month: ${net_tot}"])
    writer.writerow([f"Average Change: ${round(average(ch_list[1:]), 2)}"])
    writer.writerow([f"Greatest Increase in Profits: {goat_inc[0]} (${goat_inc[1]})"])
    writer.writerow([f"Greatest Decrease in Profits: {goat_dec[0]} (${goat_dec[1]})"])