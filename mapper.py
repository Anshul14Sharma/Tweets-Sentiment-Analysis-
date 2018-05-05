#!/usr/bin/env python

import sys
import string
import re
import json
count=1
scores = {}
intermediate = {}
def emit_intermediate(key, value):
        # if key not already in dictionary, set value to empty list
    intermediate.setdefault(key, [])
        # add value to list associated with key
    intermediate[key].append(value)
    print '%s\t%s' % (key,value)
    #print key,"\t",value

for line in sys.stdin:
    try:
        term, score = line.rsplit("\t")  # split on last whitespace separator
        scores[term] = int(score)
    except ValueError:
        print "Could not split line: %s", line
        continue    

for lines in sys.stdin:
    record = json.loads(lines)
    for key in record:
        if key=="text":
            for word in record[key].split(" "):
                if "#" in word:
                     word=word.split("#")[0]
                url=re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))')
                retw=re.compile("(?<!RT\s)@\S+")
                if url.match(word) or word.startswith('#') or retw.match(word) or word=="RT" or word.startswith('@'):
                    continue
                word=word.lower()
                word=word.encode('UTF-8').translate(None,string.punctuation)
                if word in scores:
                    emit_intermediate(count,scores[word])
                 
                else:
                    emit_intermediate(count,0) 
    count=count+1
