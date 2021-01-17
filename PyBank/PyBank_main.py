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
    goat_dec = 0

    for row in csv_reader:
        tot_mo += 1
        net_tot += int(row[1])
        ch = int(row[1]) - prev_profit
        ch_list.append(ch)
        if ch > int(goat_inc[1]):
            goat_inc [0] = row[0]
            goat_inc[1] = row[1]
        elif ch < goat_dec:
            goat_dec = ch
        prev_profit = int(row[1])

    def average(numbers):
        length = len(numbers)
        total = 0.0
        for number in numbers:
            total += number
        return total / length
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {tot_mo}")
    print(f"Total: ${net_tot}")
    #print(ch_list)
    print(f"Average Change: ${round(average(ch_list[1:]), 2)}")
    print(f"Greatest Increase in Profits: {goat_inc[0]} (${goat_inc[1]})")
    print(f"Greatest Increase in Profits: (${goat_dec})")

    output_path = os.path.join("PyBank_Analysis", "PyBank_Output.txt")


 
file1 = open("PyBank_Output.txt","w") 
  
# \n is placed to indicate EOL (End of Line) 
file1.write(f"Average Change: ${round(average(ch_list[1:]), 2)}") 

file1.close() #to change file access modes

