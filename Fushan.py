# this code is used to obtain the relationship between peoples in the TV series, based on the co-appeareance frequency of two people in one line of the txt. we get person names from baidu search and put them into "dict.txt". use "jieba" tool to discretize the play txt into single words and know if this singe word is person name or not. the relationship can be visualized by "gephi" tool at last.

# -*- coding: utf-8 -*-

import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {}   #a dictionary for storing names and frequency in whole txt
relationships = {} # inserted two dictionaries for storing relationships, person A: person B: weight
lineNames = [] # inserted two lists for person names appearing for i paragraph like {{person A, person B},{person A, person X},{},{},...}

# here consider one line as one paragraph, and the name identifying is repeated line by line
jieba.load_userdict("dict.txt") # give the name of persons to "jieba"
with codecs.open("busan.txt","r","utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line) # cut txt into words by "dict.txt"
        lineNames.append([]) # add one sublist for each line
        for w in poss:  # poss is something like dictionary, containg the property and value of each word
            if w.flag != "nr" or len(w.word) < 2: # if the property is not "nr", then this word is not a person name
                continue #lop out from this iteration time
            lineNames[-1].append(w.word) # otherwise, word is person name, add it into lineNames for current line
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {} # this "if" is to avoid anormaly because "names" and "relationships" are {} in the beginning
            names[w.word] += 1 

for name, times in names.items():
    print (name,times)


for line in lineNames:      #for each line
    for name1 in line: 
        for name2 in line:   # arbitary two persons in each line
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
# if these two persons have not appear in the same line yet
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2]+1 

# export "names" and "relationships" into txt, when exporting, deal with "relationships" so that times less than 3 are ignored
with codecs.open("busan_node.txt","w","gbk") as f:
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write(name + " " + name + " " +str(times) + "\r\n") 

with codecs.open("busan_edge.txt", "w", "gbk") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + " " + v + " " + str(w) + "\r\n")


