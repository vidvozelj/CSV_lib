import csv

output = []

with open("username-password-recovery-code.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        output.append(dict(row))

print(output)