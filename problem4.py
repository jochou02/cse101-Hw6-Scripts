import csv

with open(f'./Script Outputs/problem4.txt', 'w') as outputFile:

    for index in range(100): 
        if index < 10:
            index = '0' + str(index)

        with open(f'./HW6_Inputs/streetlamps/streetlamps_{index}.csv', 'r') as file:

            # Skip first line
            file.readline()

            # Initialize lamps from CSV file
            lamps = []
            for line in file:
                split = line.split(',')
                split[2] = split[2][:-1]
                lamps.append(split)
            
            # Initialize array + bases cases
            dp = [[None for i in range(2000)] for j in range(len(lamps))]
            for i in range(len(lamps)):
                dp[i][0] = 0
            for j in range(2000):
                dp[0][j] = float('inf')

            # Populate dp array
            for i in range(1, len(lamps)): # lamps
                for j in range(1, 2000): # houses
                    # lamp i CANNOT illuminate house j
                    if int(lamps[i][1]) < j:
                        dp[i][j] = float('inf')
                    elif int(lamps[i][0]) > j:
                        dp[i][j] = dp[i - 1][j]
                    # lamp i CAN illuminate house j
                    else:
                        dp[i][j] = min(dp[i - 1][j], int(lamps[i][2]) + dp[i - 1][int(lamps[i][0]) - 1]) 
                
            outputFile.write(f'Solution for input # {index}: {dp[-1][-1]}\n')



