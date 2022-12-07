import csv
 
for i in range(10, 11): 

    with open(f'./HW6_Inputs/color/color_{i}.csv', 'r')as file:
        csvFile = csv.reader(file)

        ad_list = []

        for line in csvFile:
            if line[0] == 'vertex':
                continue
            ad_list.append(line[1:])

        print(ad_list)