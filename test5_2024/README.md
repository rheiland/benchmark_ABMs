If you copy the .zip to your PhysiCell (1.13.1) /user_projects directory, unzip it, then from the root directory do:
```
make load PROJ=fix_motion
then:
make  # to build the executable 
mkdir output_fix_motion
fix_motion config/fix_motion
```
or perhaps run in the Studio.
