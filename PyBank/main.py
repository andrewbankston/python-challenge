# Import csv module
import csv

# Define path for csv file
budget_csv = 'Resources/budget_data.csv'

# Create empty months list to calculate number of months and pull month names
# with greatest increase and decrease
months = []

# Set net and previouspl (Previous Profit/Loss) calculation variables to 0
net = 0
previouspl = 0

# Create empty changes list to log each calculated change in Profit/Loss for
# each month from the previous month
changes = []

# Set increase and decrease calculation variables to 0 to find greatest of each
increase = 0
decrease = 0

# Open and read csv file using "," as the delimiter between columns
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Store header row and move on
    header = next(csvreader)
    
    # Iterate through each row of csv file
    for row in csvreader:
        
        # Add month in each row to months list
        months.append(row[0])
        
        # Add profit/loss in each row to current sum of profits/losses in
        # previous rows
        net += int(row[1])
        
        # Subtract the profit/loss in the previous row from that in the current
        # row and store the difference in the changes list
        changes.append(int(row[1])-previouspl)
        
        # Update the profit/loss value to the current row for use in the next
        # iteration
        previouspl = int(row[1])
        
    # Remove the first calculated difference as it does not involve two months 
    changes.pop(0)
    
    # Calculate average change and round to 2 decimal places
    avgchg = round(sum(changes)/(len(changes)), 2)
    
    # Iterate through changes list, comparing values in list to increase and
    # decrease variables.
    for change in changes:
        
        # Replace increase variable with item from changes list if item is
        # greater than current value of increase variable
        if change > increase:
            increase = change
            
        # Replace decrease variable with item from changes list if item is
        # less than current value of decrease variable
        elif change < decrease:
            decrease = change

# Find month in months list that corresponds to greatest increase and decrease
# by determining index from changes list and adding 1 (since first item of
# changes list was deleted) to get index for months list 
incMth = months[changes.index(increase) + 1]
decMth = months[changes.index(decrease) + 1]

# print results to terminal
print('Financial Analysis')
print('--------------------------')
print(f'Total Months: {len(months)}')
print(f'Total: ${net}')
print(f'Average Change: ${avgchg}')
print(f'Greatest Increase in Profits: {incMth} (${increase})')
print(f'Greatest Decrease in Profits: {decMth} (${decrease})')

# Define path for result text file to create it in analysis folder
text_output = 'analysis/PyBank_analysis.txt'

# Create text file
with open (text_output, 'w') as text:
    
    # Write the lines of text doc to match terminal printout
    text.writelines([
        'Financial Analysis', 
        '\n--------------------------',
        f'\nTotal Months: {len(months)}',
        f'\nTotal: ${net}',
        f'\nAverage Change: ${avgchg}',
        f'\nGreatest Increase in Profits: {incMth} (${increase})',
        f'\nGreatest Decrease in Profits: {decMth} (${decrease})'])
