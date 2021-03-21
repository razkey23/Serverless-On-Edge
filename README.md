# Serverless-On-Edge
## Introduction
Edge goes hand in hand with event driven architecture since most edge workloads (especially IoT ones) are event driven. In this repo we'll scratch the surface of the serverless architecture on edge nodes. More specifically, this repo contains all the code needed to explore the fundamentals of a Serverless architecture on Edge Devices. To complete this project the following *tools* were used :
* Raspberry Pi 4 (Using Raspbian OS)
* Lean Openwhisk (Serverless infrastructure) 

## Raspberry Pi 4 & Lean Openwhisk
### Raspberry
Almost everyone knows what a Raspberry Pi is. This mini computer is one the first examples that comes to mind when we think about edge nodes.(Even though their computational power has rised to pc standards). In this project we used a Raspberry Pi 4 ,64-bit architecture, 4GB ram equipped with raspbian OS.These hardware specification to run a similar project are not necessary. This raspberry might even be an overkill for the overall project.Even a more performance-constrained device could probably manage all the tasks we are about to do.
### Lean OpenWhisk
Most of the people who have grasped the idea of serverless have probably heard about OpenWhisk. OpenWhisk is an open source Serverless platform that executes functions in response to events (**event driven**). These events could be HTTP request or they can be more complex triggers coming from Feeds(like a slack message). 
The following pictures shows the components of Openwhisk:
![openwhisk_components](https://miro.medium.com/max/2400/1*AgbaSrvlqTP1ZnXOJJBJkA.jpeg)

All of these components are Huge Open Source Projects so it is fairly obvious that Openwhisk lies on the shoulders of giants.Openwhisk was built to handle tens of thousands of user actions concurrently ,and wasn't meant to handle those actions from an edge node. Running Openwhisk itself on a constrained edge node is infeasible and not that smart.That's where lean Openwhisk comes in. What's Lean Openwhisk?
* Lean Openwhisk is a **significantly downsized** Apache Openwhisk which retains the core functionality profile and core components of Openwhisk 
* Lean Openwhisk is built on the core source code of Openwhisk and it's an official branch of the Apache Openwhisk project on github

To minimize the overhead of Openwhisk and downsize it enough to run on edge nodes the components of Openwhisk needed to change a bit. The Lean Openwhisk components are shown below:
![Lean_Openwhisk](https://miro.medium.com/max/2400/1*7vZ-OZCYhT4n6tDQ9FfRXg.png)

The core differences are:
1. Lean Loadbalancer is implemented
2. Controller and Invoker are compiled together (Lean Load Balancer calls the Invoker's method for an action queued in the in-memory queue)
3. Removal of Kafka (biggest impact in reducing size) which is now mimiced by an in-memory-queue.
