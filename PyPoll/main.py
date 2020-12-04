# Import csv module
import csv

# Define path for csv file
election_csv = 'Resources/election_data.csv'

votes = 0
candidates = {}

with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    header = next(csvreader)
    
    for row in csvreader:
        
        votes += 1
        
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
        
        
    
    
print('Election Results')
print('-------------------------')
print(f'Total Votes: {votes}')
print('-------------------------')
for candidate in candidates:
    percent_won = (float(candidates.values())/votes)*100
    print(f'{candidates.keys()}: {round(percent_won,3)}% ({candidates.values()})')

print(candidates)