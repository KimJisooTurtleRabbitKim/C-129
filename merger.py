import csv 

dataset1 = []
dataset2 = []

with open ("dataset1.csv","r") as f :
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset1.append(row)

with open ("dataset2.csv","r") as f :
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset2.append(row)

header1 = dataset1[0]
header2 = dataset2[0]
planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

header = header1 + header2
planet_data = []
for index,data in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open ("final.csv","a+") as f :
    csvWriter = csv.writer(f)
    csvWriter.writerow(header)
    csvWriter.writerows(planet_data)

