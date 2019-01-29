import os
import operator
import math
import numpy as np

fre_word = []
idf = []
f = open("c:/DataMining/word/word.txt", "r", encoding="utf-8")
for line in f.readlines():
    fre_word = line.strip().split('\t')

f2 = open("c:/DataMining/word/idf.txt", "r", encoding="utf-8")
for line in f2.readlines():
    temp_idf = line.strip().split('\t')
temp_idf = np.array(temp_idf, np.float)
print(temp_idf.shape)
f.close()
f2.close()

temp = [0]*5000
tf = []
document_cnt = 0

for (path, dir, files) in os.walk("c:/term/Test_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.txt':
            fullname = path+"/"+filename
            try:
                with open(fullname, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            split = line.strip("\n ' '")
                            split = line.split('\t')
                            if split[1].count("NNG") != 0 or split[1].count("NNP") != 0:
                                split2 = split[1].split('+')
                                for i in range(len(split2)):
                                    if split2[i].count("NNG") == 1 or split2[i].count("NNP") == 1:
                                        split3 = split2[i].split('/')
                                        a = split3[0] in fre_word
                                        if a is True:
                                            index = fre_word.index(split3[0])
                                            temp[index] += 1
                    tf.append(temp)
                    temp = [0] * 5000
                    document_cnt += 1
            except IOError:
                print("Doesn't Exist file")

tf = np.array(tf)
tf = np.log(tf+1)

result = np.zeros((document_cnt, 5000), dtype=float)
result2 = np.zeros((document_cnt, 5000), dtype=float)
idf = np.zeros((document_cnt, 5000), dtype=float)

for i in range (0, document_cnt):
    idf[i] = temp_idf
result = tf*idf #d, 5000
#result2 = result ** 2

#sum_result = np.zeros((document_cnt, 5000), dtype=float)
#result_temp = result.sum(axis=1)

#for i in range(0, document_cnt):
#    sum_result[i] = result_temp[i]
#sum_result = sum_result ** 0.5

#tf_idf = np.zeros((document_cnt, 5000))
#tf_idf = result/sum_result


cnt = 0
# write
for (path, dir, files) in os.walk("c:/term/Test_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.txt':
            fullname2 = "c:/DataMining/"+filename
            try:
                with open(fullname2, "w", encoding="utf-8") as w:
                    for j in range(0, 5000):
                        w.write(str(result[cnt][j])+"\t")
                    cnt +=1
            finally:
                w.close()