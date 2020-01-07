import os
import csv

# cvs file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#creating empty lists
total_months = []
total_profit = []
monthly_profit_change = []

# read csv file 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # to skip the header row
    csv_header = next(csvreader)
    csvreader = list(csvreader)    
    
    #loop for total number of months and profit
    for i in csvreader:
        # adding all the months in a list
        total_months.append(i[0])
        count_months = len(total_months)

        # adding all the profits/losses in a list
        total_profit.append(int(i[1]))
        sum_profits = sum(total_profit)
        
    # loop to find the change between months
    for i in range(0, (len(csvreader)-1)): 
        old_rev = int(csvreader[i][1])
        new_rev = int(csvreader[i+1][1]) 
        change = new_rev - old_rev
        # adding the monthly change in a list
        monthly_profit_change.append(change)
        avg_change = round(sum(monthly_profit_change)/len(monthly_profit_change), 2)  
    
    # calculating greatest increase and decrease
    g_inc = max(monthly_profit_change)
    g_dec = min(monthly_profit_change)       
    
    # finding the months for greatest increase and decrease
    g_inc_monthindex = monthly_profit_change.index(g_inc) + 1
    g_dec_monthindex  = monthly_profit_change.index(g_dec) + 1
    
    g_inc_month = csvreader[g_inc_monthindex][0]
    g_dec_month  = csvreader[g_dec_monthindex][0]
    
    
    
    # printing the analysis to the terminal
    print("Financial Analysis")
    print("--------------------------------------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: $ {sum_profits}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {g_inc_month}  (${g_inc})")
    print(f"Greatest Decrease in Profits: {g_dec_month}  (${g_dec})")
                  
    # exporting the analysis to a text file
    output_path = os.path.join("FinancialAnalysis.txt")
    
    # Open the file using "write" mode
    with open(output_path, 'w', newline='') as txtfile:
        txtfile.write("Financial Analysis")
        txtfile.write('\n' + "---------------------------------------------------------")
        txtfile.write('\n' + f"Total Months: {count_months}")
        txtfile.write('\n' + f"Total: ${sum_profits}")
        txtfile.write('\n' + f"Average Change: ${avg_change}")
        txtfile.write('\n' + f"Greatest Increase in Profits: {g_inc_month}  (${g_inc})")
        txtfile.write('\n' + f"Greatest Decrease in Profits: {g_dec_month}  (${g_dec})")        
            