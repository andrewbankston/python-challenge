# Import csv module
import csv

# Define path for csv file
election_csv = 'Resources/election_data.csv'

# Set vote counting variable to 0
votes = 0

# Set up candidates dictionary to keep track of candidate names and vote count
candidates = {}

# Open and read csv file using "," as the delimiter between columns
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Store header row and move on
    header = next(csvreader)
    
    #Iterate through each row of csv file
    for row in csvreader:
        
        # Add 1 to vote counting variable for each row
        votes += 1
        
        # If the candidate name in the third column is not in the candidates
        # dictionary, add it to the dictionary as a key with value equals 1.
        # Add one to the value every time the candidate name appears again to
        # get a vote count for each candidate.
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

# Set most_votes variable to compare candidate vote counts against and find winner.
most_votes = 0

# Set empty winner variable to be filled each time candidate vote counts > most votes.
winner = ''

# Create empty result list to contain results info for creation of text doc.
result = []

# Print results to terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {votes}')
print('-------------------------')

# Iterate through candidates dictionary
for candidate in candidates:
    
    # Retreive value for candidate_votes variable from value associated with 
    # candidate key
    candidate_votes = candidates[candidate]
    
    # Replace value of most_votes with candidate_votes and winner with candidate
    # name if they have more votes than current most_votes value
    if candidate_votes > most_votes:
        most_votes = candidate_votes
        winner = candidate
        
    # Calculate percent of votes won by each candidate
    percent_won = (candidate_votes/votes)*100
    
    # Add a list with the name, percent of votes, and vote count for each
    # candidate to the results list.
    result.append([candidate, percent_won, candidate_votes])
    
    #Print remainder of results to terminal
    print(f'{candidate}: {round(percent_won,4)}% ({candidate_votes})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# Define path for result text file to create it in analysis folder
text_output = 'analysis/PyPoll_analysis.txt'

# Create text file
with open (text_output, 'w') as text:
    
    # Write the lines of the text doc to match terminal printout
    text.writelines([
        'Election Results',
        '\n-------------------------',
        f'\nTotal Votes: {votes}',
        '\n-------------------------',
        
        # Pull from each candidate's list (first index) within their index in 
        #results list (second index)
        f'\n{result[0][0]}: {round(result[0][1],4)}% ({result[0][2]})',
        f'\n{result[1][0]}: {round(result[1][1],4)}% ({result[1][2]})',
        f'\n{result[2][0]}: {round(result[2][1],4)}% ({result[2][2]})',
        f'\n{result[3][0]}: {round(result[3][1],4)}% ({result[3][2]})',
        '\n-------------------------',
        f'\nWinner: {winner}',
        '\n-------------------------'])
