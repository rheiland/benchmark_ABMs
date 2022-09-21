# benchmark_ABMs

This repository contains the PhysiCell code, configuration files, and input data needed for the https://permedcoe.eu/community-driven-benchmarking-hackathon/

This README is accompanied by a publicly accessible google doc (https://docs.google.com/document/d/1WrESd-lrWHv2HPY5n0W-Hj2Jm67Srw4BkAR2noyR9I8/edit#) which captures part of the development and visualization process.

To run the unit tests and use cases from the command line, the following steps should get you started.
For now, clone/download the main branch of this repo; later we will probably provide releases.

We assume a modern g++ compiler will be available (which will be the case on the BSC cluster).
For other platforms, rf. https://github.com/physicell-training/ws2022/tree/main/setup .

Unit tests:
```
M1P~/git/benchmark_ABMs$ cd PhysiCell
M1P~/git/benchmark_ABMs/PhysiCell$ make -j2
M1P~/git/benchmark_ABMs/PhysiCell$ mv project template  # this executable will suffice most of the time

compile custom models:
# single cell travels in specific direction <1,0,0>
M1P~/git/benchmark_ABMs/PhysiCell$ cp ../test3/custom_modules/custom.cpp  custom_modules/.
M1P~/git/benchmark_ABMs/PhysiCell$ make 
M1P~/git/benchmark_ABMs/PhysiCell$ mv project test3

# two cells travel in opposite directions
M1P~/git/benchmark_ABMs/PhysiCell$ cp ../test4/custom_modules/custom.cpp  custom_modules/.
M1P~/git/benchmark_ABMs/PhysiCell$ make 
M1P~/git/benchmark_ABMs/PhysiCell$ mv project test4

M1P~/git/benchmark_ABMs/PhysiCell$ cp ../test5/custom_modules/custom.cpp  custom_modules/.
M1P~/git/benchmark_ABMs/PhysiCell$ make 
M1P~/git/benchmark_ABMs/PhysiCell$ mv project test5

then from this same directory (optionally direct terminal output to a .log file):

./template data/ABM_unit_test1_3D.xml   # >unit_test1.log
./template data/ABM_unit_test2_3D.xml   # >unit_test2.log
./test3 data/ABM_unit_test3_3D.xml      # >unit_test3.log
./test4 data/ABM_unit_test4_2D.xml      # >unit_test4.log
./test5 data/ABM_unit_test5_3D.xml      # >unit_test5.log
./template data/ABM_unit_test6_3D.xml   # >unit_test6.log
./template data/ABM_unit_test7_3D.xml   # >unit_test7.log
./template data/ABM_unit_test8_3D.xml   # >unit_test8.log

```
Use cases:
```
compile custom models:
M1P~/git/benchmark_ABMs/PhysiCell$ cp ../usecase5/custom_modules/custom.cpp  custom_modules/.
M1P~/git/benchmark_ABMs/PhysiCell$ make 
M1P~/git/benchmark_ABMs/PhysiCell$ mv project case5

M1P~/git/benchmark_ABMs/PhysiCell$ template data/ABM_usecase1_3D.xml  # > usecase1.log
M1P~/git/benchmark_ABMs/PhysiCell$ template data/ABM_usecase2_3D.xml  # > usecase2.log
M1P~/git/benchmark_ABMs/PhysiCell$ template data/ABM_usecase3_2D.xml  # > usecase3.log
M1P~/git/benchmark_ABMs/PhysiCell$ template data/ABM_usecase4_3D.xml  # > usecase4.log
M1P~/git/benchmark_ABMs/PhysiCell$ case5 data/ABM_usecase5_2D.xml     # > usecase5.log
```
