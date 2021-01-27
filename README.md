# Cooperative Blind Source Separation
# Overview
- [The content of the paper.](#the-content-of-the-paper)
- [Usage of the simulation.](#usage-of-the-simulation)
- [Citation](#usage-of-the-simulation)
# The content of the paper.
## Abstract （一起）
## Introduction (一起)
- 5G in general（马）
- The application of 5G(eMBB, URLLC, mIoT)（苏）
- Mobile edge computing(which enables URLLC)（翁）
  - Definition
  - Why MEC is needed?
- Blind source seperation （姚）
  - General
  - Application in MEC and URLLC
  - The problem in its application. (Enormous calculation)
- The content of this article.（苏）
- The contribution of the members.(苏)
## Background （马、姚）
- ICA in mathematical details.(A. Hyvarinen.)
- MeICA in mathematical details.
- The objective of the seperation.
## Method（翁）
- How to seperate in details
  - The Pseudo Code.
  - Detailed decription.
## Simulation and the result（苏）
- Details of the input data.
- How to set up
- Result.
- Discussion（马）
## Conclusion（苏）
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
# Citation

``` 
@INPROCEEDINGS{Wu2006:Component,
AUTHOR="Huanzhuo Wu and Yunbin Shen and Jiajing Zhang and Ievgenii Anatolijovuch Tsokalo and Hani Salah and Frank H.P. Fitzek",
TITLE="{Component-Dependent} Independent Component Analysis for {Time-Sensitive} Applications",
BOOKTITLE="2020 IEEE International Conference on Communications (ICC): SAC Internet of Things Track (IEEE ICC'20 - SAC-06 IoT Track)",
ADDRESS="Dublin, Ireland",
DAYS=6,
MONTH=jun,
YEAR=2020
}
```

```
@INPROCEEDINGS{Wu2012:Adaptive,
AUTHOR="Huanzhuo Wu and Yunbin Shen and Jiajing Zhang and Hani Salah and Ievgenii Anatolijovuch Tsokalo and Frank H.P. Fitzek",
TITLE="Adaptive {Extraction-Based} Independent Component Analysis for {Time-Sensitive} Applications",
BOOKTITLE="2020 IEEE Global Communications Conference: Selected Areas in Communications: Internet of Things and Smart Connected Communities (Globecom2020 SAC IoTSCC)",
ADDRESS="Taipei, Taiwan",
DAYS=6,
MONTH=dec,
YEAR=2020,
KEYWORDS="Blind source separation; Independent component analysis; Time-sensitive application; IoT"
}
```
