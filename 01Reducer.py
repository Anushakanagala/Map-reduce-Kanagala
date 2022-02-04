import sys

thisKey = ""
thisValue = 0

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    source, likes = datalist

    if source != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = source
      thisValue = 0
  
    # apply the aggregation function
    thisValue  = thisValue + 1

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)