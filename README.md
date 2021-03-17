# MachineLearningIA
Program that allows you to predict a type of flower according to its characteristics. It uses the KPPV algorithm and therefore create a learning list to then be able to predict. This project was carried out during a practical work with a well-defined subject.

# Introduction
In this lab we will test the relevance of our K nearest neighbors algorithm. The procedure is as follows:
- We have reliable data that we will divide into two groups: a "learning" group and a "test" group,
- The learning group is the one that we will use as an identification model,
- For each data of the test group, we will compare the classification proposal of the algo kppv with the real classification,
- We obtain at the end a percentage of success which will give the relevance of our algorithm.

# The subject of study
We have a database of Iris flowers with characteristics. In this lab we will use the iris.data file containing 150 instances of iris flowers of three different species. It is a standard dataset where the species is known for all instances. Each flower is characterized by 4 flower measurements: sepal length, sepal width, petal length and petal width.

# Explanation
- The first thing to do is load our data file. Although the file is called iris.data, the data is in CSV format, so it can be treated like a regular CSV. Note: There is no header line or quotation marks.
- Next, we need to split the data into a training dataset that k-ppv can use to make predictions and a test dataset that we can use to assess the accuracy of the model. You will use a ratio of 67% for the learning and 33% for the test.
- We have a function that allows us to calculate "distances" from one instance to another instance. We use to collect the k most similar instances for a given unknown example.This is a simple process of calculating the distance for all instances and selecting a subset with the smallest distance values. The kppv () function which returns k most similar neighbors of the training set for a given test instance (using the distanceeuclidean function already defined). The kppv () function takes 3 arguments: The learning set: a list of lists, The element to test: a list, k: the number of desired close neighbors. The kppv () function will return a list of the k nearest neighbors.
- The prediction () function allowing to obtain the majority of a list of neighbors. (It is assumed that the class is the last attribute of each instance as in the iris.data file). We can use a dictionary to count the number of instances.

# Proof and percentage of success
<img src="https://cdn.discordapp.com/attachments/758355912426782762/821748430522417232/unknown.png" alt="" />

# Source
I carried out this project in IS during a practical work. From TP and the subject therefore comes from my high school. However the code is personal and fully encode by me.
