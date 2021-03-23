import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

files=[0,1024,5120,10240,15360,20480,25600,30720,35840,40960,46080,51200,100000,128000,208000,256000,400000,512000,650000,1000000]
x=["0","1","5","10","15","20","25.6","30","36","41","46","51","100","128","208","256","400","512","650","1000"]
y=[]
for f in files:
    l=[]
    with open("Result-"+str(f)+".csv", 'rb') as fil:
        res=fil.read()
        res=res.split('\n')
        l=[int(i) for i in res[0:20]]
        l = np.array(l)
        l = l[(l>np.quantile(l,0.2)) & (l<np.quantile(l,0.85))].tolist()
        print(l)
        median=sum(l)/len(l)
        y.append(median)

temp=[i for i in range(len(files))]
plt.figure(figsize=(9, 6))
plt.plot(temp,y)
plt.xlabel("Payload in KBytes")
plt.ylabel("Latency (ms)")
plt.xticks(temp,x)
plt.title('Payload-Latency')
plt.savefig('Payload_Latency_DataTransfer.png')
plt.clf()

# Plot the low latency Payloads

y=[]
files=[0,1024,5120,10240,15360,20480,25600,30720,35840,40960,46080,51200,100000] 
x=["0","1","5","10","15","20","25.6","30","36","41","46","51","100"]
for f in files:
    l=[]
    with open("Result-"+str(f)+".csv", 'rb') as fil:
        res=fil.read()
        res=res.split('\n')
        l=[int(i) for i in res[0:20]]
        l = np.array(l)
        l = l[(l>np.quantile(l,0.2)) & (l<np.quantile(l,0.85))].tolist()
        print(l)
        median=sum(l)/len(l)
        y.append(median)

temp=[i for i in range(len(files))]
plt.figure(figsize=(9, 6))
plt.plot(temp,y)
plt.xlabel("Payload in KBytes")
plt.ylabel("Latency (ms)")
plt.xticks(temp,x)
plt.title('Payload-Latency')
plt.savefig('Payload_Latency_DataTransfer_partial.png')
plt.clf()