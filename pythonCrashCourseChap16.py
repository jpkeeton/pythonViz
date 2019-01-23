import csv

filename = 'C://Users//jeremy.keeton//PycharmProjects//pythonViz//sitkaData.csv'

# this example worked before, wtf
# file = 'C://Users//jkeeton//Downloads//titanic.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
