import csv

with open('grades.csv', newline='') as f: # newline='' skips newlines in the data. The default value is '\n'.
    # csv_reader = csv.reader(f) # csv_reader iterates over the CSV rows.
    # header = next(csv_reader) # Skip the header row.
    # for row in csv_reader:
    #     # print(row)
    #     name, subject, grade = row # destructure
    #     print(f'{name} scored {grade} in {subject}.')
    # print(header)
    reader = csv.DictReader(f) # csv_reader iterates over the CSV rows.
    for row in reader:
        print(f'{row['Name']} scored {row['Grade']} in {row['Subject']}.')

new_data = [
    ["Name", "Subject", "Score"],
    ["David", "History", 88],
    ["Eve", "Art", 92]
]

with open('new_grades.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(new_data)