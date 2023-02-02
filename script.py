import csv 

with open("gender_submission.csv", "test.csv", "train.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)