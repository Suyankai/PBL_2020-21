# Cooperative Blind Source Separation
# Overview
- The content of the paper.
- Usage of the simulation.
- Citation
# The content of the paper.
## Abstract
## Introduction
- 5G in general
- The application of 5G(eMBB, URLLC, mIoT)
- Mobile edge computing(which enables URLLC)
  - Definition
  - Why MEC is needed?
- Blind source seperation 
  - General
  - Application in MEC and URLLC
  - The problem in its application. (Enormous calculation)
- The content of this article.
- The contribution of the members.
## Background 
- ICA in mathematical details.(A. Hyvarinen.)
- MeICA in mathematical details.
- The objective of the seperation.
## Method
- How to seperate in details
  - The Pseudo Code.
  - Detailed decription.
## Simulation and the result
- Details of the input data.
- Result.
- Discussion
## Conclusion
- The summary
# Usage of the simulation.
This part's core and alogrithm also base on `pyfastbss_core.py`.

Here is Information to run the Simulator of Microservice. 

run the `client.py` to show the figure of **Time-Source Number** and **SNR-Source Number**
```
python3 client.py
```

If you want to see the Hop Microservice information, you can run:
```
python3 client.py --iter_time 1 0
```
If you want to compare MeICA on MS with MeICA and FastICA, run:
```
python3 client.py --run_FastICA --run_MeICA
```
Because the time reason, we don't simulate it in `mininet` so we provide a simple simulator to compare the proformance by run:
```
python3 client.py --run_FastICA --run_MeICA --run_Simulator
```
You can also setting the parameter for this simulator:
```
--service_latency SERVICE_LATENCY
                        setting the latency of service for origin MeICA, 
                        default: 50 [ms]
--service_performance SERVICE_PERFORMANCE
                        setting the performance of service compare to mircoservice, 
                        default: 10 [times]
--micro_latency MICRO_LATENCY
                        setting the latency of micro service, 
                        default: 0.5 [ms]
```
The default sounce number is : 5 , you can set it by running, e.x:
```
--source_num 10
```
More Information by running you can see help, by running:
```
python3 client.py -h
```
### Tips:
If you use WSL2, you need to use Tkagg to show the figure, by adding
```
import matplotlib 
matplotlib.use('TkAgg')
```
in `client.py`

and you need XServer to show the GUI, for VSCode you need to set:
```
export DISPLAY=`cat /etc/resolv.conf | grep nameserver | awk '{print $2}'`:0
```
