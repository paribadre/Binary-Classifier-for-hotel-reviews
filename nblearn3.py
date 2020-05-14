
import glob
import re
import os
from collections import Counter
import collections
from math import log
import sys

all_files = glob.glob(os.path.join(sys.argv[1], '*/*/*/*.txt'))
CountDeceptive = Counter()
CountTruthful = Counter()
CountPositive = Counter()
CountNegative = Counter()
ProbDeceptive = Counter()
ProbTruthful = Counter()
ProbPositive = Counter()
ProbNegative = Counter()
Vocabulary = []
StopWord = []
test_by_class = collections.defaultdict(list)
train_by_class = collections.defaultdict(list)

words = []
Deceptive = []
Truthful = []
Positive = []
Negative = []
Test = []

for i in all_files:
    if "deceptive_from_MTurk" in i:
        Deceptive.append(i)
    else:
        Truthful.append(i)
    if "negative_polarity" in i:
        Negative.append(i)
    else:
        Positive.append(i)

for i in Deceptive:
    with open(i, 'r') as ff:
      text = ff.read()
    text = re.sub('[^A-Za-z]+', ' ', text)
    text = text.lower()
    words = text.split(" ")
    for j in words:
        CountDeceptive[j] += 1
        if j not in Vocabulary:
            Vocabulary.append(j)

for i in Truthful:
    with open(i, 'r') as ff:
      text = ff.read()
    text = re.sub('[^A-Za-z]+', ' ', text)
    text = text.lower()
    words = text.split(" ")
    for j in words:
        CountTruthful[j] += 1
        if j not in Vocabulary:
            Vocabulary.append(j)

for i in Positive:
    with open(i, 'r') as ff:
      text = ff.read()
    text = re.sub('[^A-Za-z]+', ' ', text)
    text = text.lower()
    words = text.split(" ")
    for j in words:
        CountPositive[j] += 1

for i in Negative:
    with open(i, 'r') as ff:
      text = ff.read()
    text = re.sub('[^A-Za-z]+', ' ', text)
    text = text.lower()
    words = text.split(" ")
    for j in words:
        CountNegative[j] += 1

PriorDeceptive = len(Deceptive)/(len(Deceptive) + len(Truthful))
PriorTruthful = len(Truthful)/(len(Deceptive) + len(Truthful))
PriorPositive = len(Positive)/(len(Positive) + len(Negative))
PriorNegative = len(Negative)/(len(Positive) + len(Negative))
VocabCount = len(Vocabulary)

for i in Vocabulary:
    ProbDeceptive[i] = log(CountDeceptive[i] + 1) - log(sum(CountDeceptive.values()) + VocabCount +1)
    ProbTruthful[i] = log(CountTruthful[i] + 1) - log(sum(CountTruthful.values()) + VocabCount + 1)
    ProbPositive[i] = log(CountPositive[i] + 1) - log(sum(CountPositive.values()) + VocabCount + 1)
    ProbNegative[i] = log(CountNegative[i] + 1) - log(sum(CountNegative.values()) + VocabCount + 1)

print(C)

f = open("nbmodel.txt", "w")
f.write(str(sum(CountPositive.values()) + VocabCount +1))
f.write("\n")
f.write(str(sum(CountNegative.values()) + VocabCount +1))
f.write("\n")
f.write(str(sum(CountTruthful.values()) + VocabCount +1))
f.write("\n")
f.write(str(sum(CountDeceptive.values()) + VocabCount +1))
f.write("\n")
f.write(str(dict(ProbDeceptive)))
f.write("\n")
f.write(str(dict(ProbTruthful)))
f.write("\n")
f.write(str(dict(ProbPositive)))
f.write("\n")
f.write(str(dict(ProbNegative)))
f.write("\n")
f.write(str(PriorDeceptive))
f.write("\n")
f.write(str(PriorTruthful))
f.write("\n")
f.write(str(PriorPositive))
f.write("\n")
f.write(str(PriorNegative))
f.close()
