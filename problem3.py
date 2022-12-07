import csv
 
with open(f'./Script Outputs/problem3.txt', 'w') as outputFile:

    for i in range(0, 100): 
        if i < 10:
            i = '0' + str(i)

        with open(f'./HW6_Inputs/socks/socks_{i}.csv', 'r') as file:

            socks = []
            threshold = 0.25
            pairs = 0

            # Skip first line
            file.readline()

            for line in file:
                socks.append(float(line))

            socks.sort()

            while len(socks) > 1:
                if socks[1] - socks[0] <= threshold:
                    pairs += 1
                    socks = socks[2:]
                else:
                    socks = socks[1:]
            outputFile.write(f'Solution for input # {i}: {pairs}\n')

        