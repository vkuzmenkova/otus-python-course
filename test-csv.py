import csv
from faker import Faker

fake = Faker()

with open("tmp_csv.csv", mode='w', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=',', lineterminator="\r")
    names = ['Name', 'Job', 'Birthdate', 'Mail']
    csv_writer.writerow(names)

    for i in range(100):
        user = fake.profile()
        csv_writer.writerow([
            user['name'],
            user['job'],
            user['birthdate'],
            user['mail']
        ])

    csv_dictwriter = csv.DictWriter(file, delimiter=',',
                                    lineterminator="\r", fieldnames=names)
    csv_dictwriter.writeheader()
    for i in range(100):
        user = fake.profile()
        csv_dictwriter.writerow({
            'Name': user['name'],
            'Job': user['job'],
            'Birthdate': user['birthdate'],
            'Mail': user['mail']
        })

# with open("tmp_csv.csv", mode='r', encoding='utf-8') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     for line in csv_reader:
#         print(line)

with open("tmp_csv.csv", mode='r', encoding='utf-8') as file:
    csv_dictreader = csv.DictReader(file, delimiter=',')
    for line in csv_dictreader:
        print(f"{line['Name']}, {line['Job']}. Email: {line['Birthdate']}.")
