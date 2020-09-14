# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:40:08 2020

@author: Ben
"""
import matplotlib.pyplot as plt

fileHandler = open("iz.tr","r")
listOfLines = fileHandler.readlines()
CongestionList = [ ]
CongestionCountList=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fileHandler.close()

for line in listOfLines:
        elemanlar = line.split(" ")
        if elemanlar[6] == "---A---":
            Congestion=+1
            CongestionList.append(elemanlar)
            for i in range(19):
                if int(float(elemanlar[1])) == i:
                    CongestionCountList[i]= int(CongestionCountList[i]) + 1
figure = plt.figure()
plt.title("CONGESTION PER SECOND")
plt.ylabel("CONGESTION EVENT")
plt.xlabel("TIME")
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], CongestionCountList, "r.-", label="$Congestion$")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
plt.legend()
plt.show()
print(CongestionCountList)
