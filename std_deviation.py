import math
import csv

with open("Xvalues.csv", newline="")as values:
    reader = csv.reader(values)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0

    for x in data :
        total = total + int(x)
    mean = total/n

    return mean

squared_list = []

for number in data :
    a = int(number)-mean(data)
    a = a ** 2
    squared_list.append(a)

sum = 0
 
for i in squared_list :
    sum = sum + i 

result = sum/(len(data)-1)

std_deviation = math.sqrt(result)
print("Standard Deviation : " + str(std_deviation))