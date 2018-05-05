## Twitter-Sentiment-Analysis  ##

This repo aims to provide the sentiment analysis of twitter post in the form of score range 1-5.

#### 1. Start fetching the data from twitter:####  
	``Command: ./bin/flume-ng agent -n TwitterAgent -c conf -f /usr/lib/apache-flume-1.4.0-bin/conf/flume.conf``

#### 2. Run python program in HDFS Cluster: ####  
	``hadoop jar contrib/streaming/hadoop-streaming-mr1.jar -file /home/cloudera/Desktop/mapper.py -mapper /home/cloudera/Desktop/temp/mapper.py -file /home/cloudera/Desktop/temp/reducer.py -reducer /home/cloudera/Desktop/reducer.py -input /user/project/AFINN-111.txt /user/project/FlumeData.txt -output /user/project/output``

