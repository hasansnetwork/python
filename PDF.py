import codecs
import matplotlib.pyplot as plt
dics = []
count = 0
with codecs.open("iz.tr", "r", "UTF8") as inputFile:
    inputFile=inputFile.readlines()
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
time=[]
send_data=[]
received_data=[]
rates =[]
for i in range(20):
    send_data.append(0)
    received_data.append(0)
    time.append(i)
    rates.append(0)
for row in dics:
    i = int(float(row['time']))
    if row['event'] == "-" :#and int(row['pkt_size']) >= 1000:
        send_data[i] += 1
    if row['event'] == "r" :#and int(row['pkt_size']) >= 1000:
        received_data[i] += 1
for i in range(19):
    rates[i+1] = received_data[i+1]/send_data[i+1]
fig = plt.figure()
plt.plot(time[1::],rates[1::],"r.--",label="$PDF$")
plt.legend()
plt.title("Packet Delivery Rate")
plt.xlabel("time")
plt.ylabel("PDF")
plt.show()