import pandas as pd
import matplotlib.pyplot as plt




data = pd.read_csv("payload_latency.csv")
length = len(data['ow concurrency'])


#PLOT Payload-Latency

lis=[]
dic={'timeout30':[],'timeout30payload1K':[],'timeout30payload100K':[],'timeout30payload1M':[]}
for i in range(length):
    temp = int(data['realtotaltime(msec)'][i].replace('(msec)',''))
    lis.append(temp)
    if data['loadtestconcurrency'][i]==10:
        dic[data['payloadfile'][i]].append((data['ow concurrency'][i],sum(lis)/len(lis)))
        lis=[]

concurrency=[1,2,3,4,5]
y=[]
for items in dic:
    l=[]
    for tup in dic[items]:
        l.append(tup[1])
    y.append((l,items))

#y is like [([],payload1),([],payload2),([],payload3),([],payload4)

#Plotter

for i in range(len(y)):
    plt.plot(concurrency,y[i][0],label=y[i][1],marker='o')
    plt.xticks(concurrency)

plt.legend(fontsize='x-small')
plt.xlabel('Concurrency')
plt.ylabel('Latency(ms)')
plt.title('Concurrency-Latency')
plt.savefig('Payloadplot_Latency.png')
plt.clf()



#plot Payload-Throughput


lis=[]
dic={'timeout30':[],'timeout30payload1K':[],'timeout30payload100K':[],'timeout30payload1M':[]}
for i in range(length):
    temp=int(data['rps'][i])
    lis.append(temp)
    if data['loadtestconcurrency'][i]==10:
        dic[data['payloadfile'][i]].append((data['ow concurrency'][i],sum(lis)/len(lis)))
        lis=[]

concurrency=[1,2,3,4,5]
y=[]
for items in dic:
    #print(items)
    l=[]
    for tup in dic[items]:
        l.append(tup[1])
    y.append((l,items))

#y is like [([],payload1),([],payload2),([],payload3),([],payload4)

#Plotter

for i in range(len(y)):
    plt.plot(concurrency,y[i][0],label=y[i][1],marker='x')
    plt.xticks(concurrency)

plt.legend(fontsize='x-small')
plt.xlabel('Concurrency')
plt.ylabel('Throughput(Request per Second)')
plt.title('Concurrency-Throughput')
plt.savefig('Payloadplot_Throughput.png')
plt.clf()


 