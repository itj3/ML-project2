import csv

# def bounds(startTime, endTime):
startTime= '2200'
endTime = '0630'
with open('AdelMathDeployment.csv', 'rb') as csvFile:
    content = csv.reader(csvFile, delimiter=',')
    night = open('night.csv', 'wb')
    switch = False

    startTime = int(startTime)
    endTime = int(endTime)
    # rowNum=0
    for row in content:
        # rowNum = rowNum+1
        try:
            time = str(row[4:5])
            if len(time) == 16:
                time = time[2:4] + time[5:7]
            else:
                time = time[2:3] + time[4:6]
            x = int(time)
            if endTime < startTime:
                switch = (x>=startTime or x <=endTime)
                if switch:
                    night.write("%s," % row[0])
                    night.write("%s," % row[3])
                    night.write("%s," % row[4])
                    night.write("%s," % row[6])
                    # night.write(str(rowNum))
                    night.write('\n')
            else:
                switch = (x>=startTime and x <=endTime)
                if switch:
                    night.write("%s," % row[0])
                    night.write("%s," % row[3])
                    night.write("%s," % row[4])
                    night.write("%s," % row[6])
                    # night.write(str(rowNum))
                    night.write('\n')
        except ValueError:
            pass