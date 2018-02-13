#Alex Espinal
#The Import needed for opening the file.
import re
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler 

stdScaler = StandardScaler()

#This opens the wine data and puts them in lines. 
file = open("wine.data","r")

for line in file :
    values = [values for values in line ]
    values = re.split(", |  \n| ",line)

wineDataFrame = pd.io.parsers.read_csv('wine.data',header = None, usecols = [3,4,5])
#put the data into columns of 3. 
wineDataFrame.columns = ['wine1', 'wine2', 'wine3']
print("******************WINE DATA FRAME MIN MAX********************")

#This well put the data into standard deviation. 
std_scale = stdScaler.fit(wineDataFrame)

dataFrameTransform = std_scale.transform(wineDataFrame) 

#This is for calculating the Min and Max.
minMax_scale = stdScaler.fit(wineDataFrame)
dataFrameMinMax = minMax_scale.transform(wineDataFrame)

#This well print out the data into each row and column from Min and Max.
#This prints the the row, max, and min column.
n = 0 
for w in dataFrameMinMax:
    print("Row" ,n,": Max = ", dataFrameMinMax[n,:].max(),"Min = ", dataFrameMinMax[n,:].min())
    n = n + 1

#This is the Lamba with my constant, which i choose to be mutiplied by 4. 
print("**************Wine Data Lamba Function************")
n = 0
for w in dataFrameMinMax:
    dataFrameMinMax[n,0] = dataFrameMinMax[n,0] * 4
    dataFrameMinMax[n,1] = dataFrameMinMax[n,1] * 4
    dataFrameMinMax[n,2] = dataFrameMinMax[n,2] * 4
    n = n + 1

#Then prints out the data in Lamba.
print(dataFrameMinMax)
