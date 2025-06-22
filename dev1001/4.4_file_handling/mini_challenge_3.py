# Task: Read new_grades.csv (that was just created) and print only the
#       names of students who scored above 90.

import csv

with open('new_grades.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Score']) > 90:
            print(row['Name'])

# OR

with open('new_grades.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name, subject, score = row
        if int(score) > 90:
            print(name)
