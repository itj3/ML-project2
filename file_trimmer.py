import csv

# def bounds(startTime, endTime):
startTime= '2200'
endTime = '0800'
webster = {}
with open('ArbTempDataset.csv', 'r') as csvTemp:
    stuff = csv.reader(csvTemp, delimiter=',')
    for row in stuff:
        try:
            temp = str(row[3:4]).split("'")
            keye = str(row[1:3]).split("[")
            keye = keye[1].split("]")
            keye = keye[0].split("'")
            x = len(keye[3])-7
            keye = keye[1]+" "+keye[3][0:x]
            # print keye
            webster[keye] = float(temp[1])
        except ValueError:
            pass
# print webster['4/16/2015 5:40']
with open('AdelMathDeployment.csv', 'r') as csvFile:
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
                    try:
                        keyes = str(row[3:5]).split("]")
                        keyes = keyes[0].split("[")
                        keyes = keyes[1]
                        keyes = keyes.split("'")
                        x = len(keyes[3])-7
                        keyes = keyes[1] + " " + keyes[3][0:x]
                        datTime = webster[keyes];
                        night.write("%s," % row[0])
                        night.write("%s," % row[3])
                        night.write("%s," % row[4])
                        night.write("%s," % row[6])
                        night.write("%s," % datTime)
                        # night.write(str(rowNum))
                        night.write('\n')
                    except KeyError:
                        pass
            else:
                switch = (x>=startTime and x <=endTime)
                if switch:
                    try:
                        keyes = str(row[3:5]).split("]")
                        keyes = keyes[0].split("[")
                        keyes = keyes[1]
                        keyes = keyes.split("'")
                        x = len(keyes[3])-7
                        keyes = keyes[1] + " " + keyes[3][0:x]
                        datTime = webster[keyes]

                        night.write("%s," % row[0])
                        night.write("%s," % row[3])
                        night.write("%s," % row[4])
                        night.write("%s," % row[6])
                        night.write("%s," % datTime)
                        # night.write(str(rowNum))
                        night.write('\n')
                    except KeyError:
                        pass
        except ValueError:
            pass