import csv

class Streetlamp():

    def __init__(self, left, right, cost):
        self.left = int(left) - 1
        self.right = int(right) - 1
        self.cost = int(cost)

    def __repr__(self):
        return f'Left: {self.left} Right: {self.right} Cost: {self.cost}'

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
                lamp = Streetlamp(split[0], split[1], split[2])
                lamps.append(lamp)
            
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
                    if lamps[i].right < j:
                        dp[i][j] = float('inf')
                    elif lamps[i].left > j:
                        dp[i][j] = dp[i - 1][j]
                    # lamp i CAN illuminate house j
                    else:
                        
                        dp[i][j] = min(dp[i - 1][j], lamps[i].cost + dp[i - 1][lamps[i].left - 1]) 
                
            outputFile.write(f'Solution for input # {index}: {dp[-1][-1]}\n')



