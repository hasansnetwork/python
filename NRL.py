# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:16:21 2020

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
data_packets = []
ack_packets = []
rates = []
for i in range(20):
    data_packets.append(0)
    ack_packets.append(0)
    time.append(i)
    rates.append(0)

for row in dics:
    i = int(float(row['time']))
    if row['event'] == "r" and row['pkt_type'] == "ack":
        ack_packets[i] += 1
    if row['event'] == "r" and row['pkt_type'] == "tcp" and int(row['pkt_size']) > 1000:
        data_packets[i] += 1

print(ack_packets)
print(data_packets)

for i in range(19):
    rates[i + 1] = ack_packets[i + 1] / data_packets[i + 1]

fig = plt.figure()
plt.plot(time[1::], rates[1::], "g--", label="$NRL$")
plt.legend()
plt.title("Normalised Routing Load")
plt.xlabel("time")
plt.ylabel("Routing Packets")
plt.show()
