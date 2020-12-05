import csv
import datetime

employee_csv = 'Resources/employee_data.csv'

ID = []
firstName = []
lastName = []
DOB = []
SSN = []
State = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(employee_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    header = next(csvreader)
    
    for row in csvreader:
        ID.append(row[0])
        
        first = row[1].split(' ')[0]
        last = row[1].split(' ')[1]
        firstName.append(first)
        lastName.append(last)
        
        old_dob = datetime.datetime.strptime(row[2], '%Y-%m-%d')
        DOB.append(old_dob.strftime('%m/%d/%Y'))
        
        ssn_secure = row[3].split('-')[2]
        SSN.append(f'***-**-{ssn_secure}')
        
        
        State.append(us_state_abbrev[row[4]])
        
new_employee_record= zip(ID, firstName, lastName, DOB, SSN, State)

output = 'analysis/reformatted_employee_data.csv'

with open(output, 'w', newline='') as datafile:
    writer = csv.writer(datafile)
    
    writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    
    writer.writerows(new_employee_record)
