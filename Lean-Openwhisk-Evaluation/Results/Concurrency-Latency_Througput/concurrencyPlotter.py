import pandas as pd
import matplotlib.pyplot as plt




data = pd.read_csv("ConcurrencyLatency.csv")
#USED FOR CONCURRENCY - LATENCY PLOT 


dic={}
lst=[]
for i in range(len(data['ow concurrency'])):
    temp = int(data['realtotaltime(msec)'][i].replace('(msec)',''))  # Temp has total time as int in msec'
    #temp=int(data['rps'][i])
    if (data['errors'][i] <= 10):
        lst.append(temp)
    if (data['loadtestconcurrency'][i]==30):
        dic[data['ow concurrency'][i]]=lst
        lst=[]

fig, ax = plt.subplots()
ax.boxplot(dic.values(),showfliers=False)
ax.set_xticklabels(dic.keys())
plt.xlabel('Concurrency')
plt.ylabel('Latency(ms)')
plt.title('Concurrency-Latency')
plt.savefig('Conc_Latency.png')
plt.clf()



 

#USED FOR CONCURRENCY - Throughput PLOT 



dic={}
lst=[]
for i in range(len(data['ow concurrency'])):
    temp=int(data['rps'][i])
    if (data['errors'][i] <= 10):
        lst.append(temp)
    if (data['loadtestconcurrency'][i]==30):
        dic[data['ow concurrency'][i]]=lst
        lst=[]

fig, ax = plt.subplots()
ax.boxplot(dic.values(),showfliers=False)
ax.set_xticklabels(dic.keys())
plt.xlabel('Concurrency')
plt.ylabel('Throughput(Request per Second)')
plt.title('Concurrency-Throughput')
plt.savefig('Conc_Throughput.png')
plt.clf()
