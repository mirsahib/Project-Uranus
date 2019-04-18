# Classifying hand position using Inertial Measurement Unit

### Introduction: 

In this project we present the development and implementation of an Inertial Measurement Unit  device which is used to collect data(accelerometer,gyroscope,magnetometer) from different position of the human hand.

### Description:
The data of the IMU are collected from both hand at five different position (10 position in total),The position of the hand is shown in Fig 1 and Fig 2.

<img width=500 src="image/class1_6.jpg">


<center>Fig 1: Subject holding IMU at position 1 to 6(black dot)</center>


<img width=500 src="image/class7_10.jpg">


<center>Fig 2: Subject holding IMU at position 7 to 10(black dot)</center>


<br>

From each position we have collected 250 sets of reading than we label this reading according to their position (eg:for position 1 its 1),then each position dataset is recompile to a larger dataset where every position data are stored.The size of this recompile data set is 1500 by 10.This dataset is then split into 30/70 ratio,30% for testing process and 70% is for training process.We used decision tree to classify those 10 different position and we have found that by using gini index as the decision tree criterion we get 39%  accuracy and by using information gain as the decision tree criterion we get 81% accuracy.
### Hardware used:
1. MPU 9250 9 axis IMU
2. Arduino Nano
3. DS 1307 RTC module
4. Micro SD Card

<img width=300 src="image/hardware.jpg">

### Hardware Description: 
The device is assembled according to the given image Fig 2.The MPU 9250(IMU) send 3 set of data to arduino nano from 3 sensors,The sensors are accelerometer,gyroscope and magnetometer.The DS 1307 rtc is a real time clock module which give the time stamp for each reading.This reading is collected by arduino nano and write it in a csv file using the micro sd card module.

### Data collection and preprocessing:
We have collected 10 set of data (350+ reading) by holding the hand at 10 different  position (**shown in Fig:1 & 2)**.We have discarded 50 reading from the top and 50 reading from the bottom because those reading contain the most noise (the hand is not stationary).The x,y and z axis of the accelerometer,gyroscope and magnetometer is the feature of this problem.We don’t consider timestamp(rtc reading) as the feature of this problem.We have label each of this reading according to their positional value and recompile into a larger data set (dataset.csv).This large data set is then split into 30/70 ratio,30% as training data and 70% as testing data.Before splitting the data we have shuffle the row so that each part(training and testing) get fair number of classes.
### Decision Tree:
We have modeled our decision tree into two classifiers,One classifier with gini index and another one is with information gain as the criterion.For both of the classifier we use max_depth= 3 , min_sample_leaf=5 and a random_state=100.Using gini index as the criterion we get 39% accuracy and 81% accuracy when we used information gain as the criterion.

### Confusion Matrix :
**Confusion matrix using gini index as criterion**

![gini confusion matrix](https://github.com/mirsahib/Project-Andromeda/blob/master/image/gini.jpg)


![gini heat map](https://github.com/mirsahib/Project-Andromeda/blob/master/image/gini_heat.png)


**Confusion matrix using Information gain as criterion**


![information gain](https://github.com/mirsahib/Project-Andromeda/blob/master/image/info.png)


![info heat](https://github.com/mirsahib/Project-Andromeda/blob/master/image/infoheatupdate.png)

### Code
[Link](https://github.com/mirsahib/Project-Andromeda/blob/master/IMU_updated.ipynb)

### Dataset
[Link](https://github.com/mirsahib/Project-Andromeda/tree/master/Dataset)
