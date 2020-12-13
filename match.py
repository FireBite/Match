import csv
import random

people = []

with open("./in.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        people.append(row)

random.shuffle(people)

with open("./out.txt", mode='w') as f:
    while len(people) > 1:
        a = people.pop(-1)
        b = people.pop(-1)
        print(f'1: {a[0]}\n2: {b[0]}\n')

        print(f'-------({a[0]} -> {b[0]})-------', file=f)
        print(f'{a[0]} -> \n{b[1]}\n', file=f)
        print(f'{b[0]} -> \n{a[1]}\n', file=f)
    
    if len(people) == 1:
        print(f"\n(!) JEDNA OSOBA ({people[0][0]}) BEZ PARY! (!)", file=f)