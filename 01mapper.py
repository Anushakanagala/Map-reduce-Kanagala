import sys

for line in sys.stdin:  
    dataList = line.strip().split(",") 
    
    if (len(dataList) == 5) :
        date,retweets,source,author,likes = dataList 
        print (source,"\t", likes)