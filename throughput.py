# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:58:52 2020

@author: Ben
"""

import codecs
import matplotlib.pyplot as plt

dics = []
count = 0

with codecs.open("iz.tr", "r", "UTF8") as inputFile:
    inputFile = inputFile.readlines()
for line in inputFile:
    item = line.split(" ");

    line_dic = {}

    line_dic['event'] = item[0]
    line_dic['time'] = item[1]
    line_dic['from_node'] = item[2]
    line_dic['to_node'] = item[3]
    line_dic['pkt_type'] = item[4]
    line_dic['pkt_size'] = item[5]
    line_dic['flags'] = item[6]
    line_dic['fid'] = item[7]
    line_dic['srcadd'] = item[8]
    line_dic['dstadd'] = item[9]
    line_dic['seqnum'] = item[10]
    line_dic['pkti'] = item[11]

    dics.append(line_dic)
time = []
bayts = []
for i in range(20):
    time.append(i)
    bayts.append(0)

for row in dics:
    i = int(float(row['time']))
    if row['event'] == "r" and int(row['pkt_size']) >= 1000:
        bayts[i] += int(row['pkt_size'])

for i in range(19):
    bayts[i + 1] = (bayts[i + 1] * 8) / (1000 * 1)  # carpi bir saniye

fig = plt.figure()
plt.plot(time, bayts, "b.-", label="$DATA$")
plt.legend()
plt.title("Throughput")
plt.xlabel("Time")
plt.ylabel("Kbps")
plt.show()

# print(dics)