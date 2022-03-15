from collections import Counter
import csv
from itertools import count


with open("data.csv",newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

newData = list()
for i in range(len(fileData)):

    number = fileData[i][2]
    newData.append(float(number))

data = Counter(newData)
dataForRange = {
"100-120":0,
"120-130": 0,
"130-140": 0
}

for weight,occurence in data.items():
    if 100<float(weight)<120:
        dataForRange["100-120"] += occurence
    elif 120<float(weight)<130:
        dataForRange["120-130"] += occurence
    elif 130<float(weight)<140:
        dataForRange["130-140"] += occurence

modeRange,modeOccurence = 0,0
for range,occurence in dataForRange.items():

    if occurence> modeOccurence:
        modeRange,modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
    

mode = float((modeRange[0]+modeRange[1])/2)

print("The mode is: "+ str(mode))

