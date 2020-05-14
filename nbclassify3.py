import glob
import re
import os
from collections import Counter
import collections
from math import log
import ast
import sys
Prob1 = 0.0
Prob2 = 0.0
Prob3 = 0.0
Prob4 = 0.0

dics = []
with open('nbmodel.txt', 'r') as model:
    for line in model:
        dics.append(line)
    Positive = int(dics[0])
    Negative = int(dics[1])
    Truthful = int(dics[2])
    Deceptive = int(dics[3])
    ProbDeceptive = ast.literal_eval(dics[4])
    ProbTruthful = ast.literal_eval(dics[5])
    ProbPositive = ast.literal_eval(dics[6])
    ProbNegative = ast.literal_eval(dics[7])
    PriorDeceptive = float(dics[8])
    PriorTruthful = float(dics[9])
    PriorPositive = float(dics[10])
    PriorNegative = float(dics[11])

Test = []
all_files = glob.glob(os.path.join(sys.argv[1], '*/*/*/*.txt'))

for i in all_files:
    with open(i, 'r') as ff:
      text = ff.read()
    text = re.sub('[^A-Za-z]+', ' ', text)
    text = text.lower()
    words = text.split(" ")
    for j in words:
        if j not in ProbPositive:
            ProbPositive[j] = 1/Positive
            ProbNegative[j] = 1/Negative
            ProbTruthful[j] = 1/Truthful
            ProbDeceptive[j] = 1/Deceptive
        Prob1 += ProbPositive[j]
        Prob2 += ProbNegative[j]
        Prob3 += ProbTruthful[j]
        Prob4 += ProbDeceptive[j]
    Prob1 += log(PriorPositive)
    Prob2 += log(PriorNegative)
    Prob3 += log(PriorTruthful)
    Prob4 += log(PriorDeceptive)
    if Prob3 > Prob4:
        x = "truthful "
    else:
        x = "deceptive "
    if Prob1 > Prob2:
        x += "positive "
    else:
        x += "negative "
    f = open("nboutput.txt", "a+")
    f.write(x + i)
    f.write("\n")
f.close()

