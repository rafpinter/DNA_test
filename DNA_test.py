import csv
from sys import argv, exit

# Checking usage
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")

# Opening database from csv file
data_sample = open(argv[1], "r") 
data = csv.DictReader(data_sample)

list_str = list(data.fieldnames)
del list_str[0]

# Opening sample DNA
DNA_sample = open(argv[2])
sample_reader = csv.reader(DNA_sample)
for row in sample_reader: 
    sample = row[0]

# Identifying number and size of STR regions
str_found = []
for new_str in list_str: 
    x = -len(new_str)
    repeat = list("0" * (len(new_str) - 1))
    repeat = [int(d) for d in repeat]
    my_range = len(sample) - x + 1

    for i in range(my_range):
        if i == 0:
            if new_str == sample[x:]:
                repeat.insert(0, 1)
            else:
                repeat.insert(0, 0)
        elif i == 1:
            if new_str == sample[x - i: -i]:
                repeat.insert(0, 1)
            else:
                repeat.insert(0, 0)
        else:
            if new_str == sample[x - i: -i]:
                repeat.insert(0, (1 + repeat[len(new_str) - 1]))
            else:
                repeat.insert(0, 0)
        i += 1

    str_found.append(max(repeat)) 

# Matching sample DNA to database
for row in data:
    check_nstr = []
    for my_str in list_str: 
        check_nstr.append(int(row[my_str]))
    if check_nstr == str_found:
        print(row['name'])
        exit()

# If no match
print("No match")
