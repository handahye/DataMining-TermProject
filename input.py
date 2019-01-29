import os
import operator
import math
import numpy as np

temp = {}
temp2 = {}
word = {}
s_word = {}
word_list = []
document_cnt = 0

for (path, dir, files) in os.walk("c:/term/Input_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.txt':
            fullname = path+"/"+filename
            # print("%s" % fullname)
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
                                        if len(split3[0]) >= 2:
                                            a = split3[0] in temp
                                            if a is False:
                                                temp[split3[0]] = 1
                                                temp2[split3[0]] = 1
                                            elif a is True:
                                                temp[split3[0]] += 1
                                                temp2[split3[0]] = temp[split3[0]]
                    word_list.append(temp2)
                    temp2 = {}
                    document_cnt += 1
            except IOError:
                print("Doesn't Exist file")


sorted_temp = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)
for k in range(0, 5000):
    word[sorted_temp[k][0]] = sorted_temp[k][1]
sorted_word = sorted(word.items(), key=operator.itemgetter(0))
fre_word = []
for k in range(0, 5000):
    s_word[sorted_word[k][0]] = sorted_word[k][1]
    fre_word.insert(k, sorted_word[k][0])

tf_cnt = [0] * 5000
idf_cnt = []
idf_sum = [0] * 5000

idf = np.zeros((document_cnt, 5000), dtype=float)
tf = np.zeros((document_cnt, 5000), dtype=float)

for i in range(0, document_cnt):
    for j in range(0, 5000):
        a = fre_word[j] in word_list[i]
        if a is True:
            temp = word_list[i][fre_word[j]]+1
            tf_cnt[j] = math.log10(temp)
            idf_sum[j] = 1
    tf[i] = tf_cnt
    idf_cnt.insert(j, idf_sum)
    tf_cnt = [0] * 5000
    idf_sum = [0] * 5000

idf_cnt = np.array(idf_cnt)
idf_temp = idf_cnt.sum(axis=0)
idf = np.zeros((document_cnt, 5000), dtype=float)

for i in range(0, document_cnt):
    idf[i] = idf_temp


idf = document_cnt/(1+idf)

write_idf = np.zeros(5000, dtype=float)
write_idf = idf[0]

result = np.zeros((document_cnt, 5000), dtype=float)
#result2 = np.zeros((document_cnt, 5000), dtype=float)

result = tf*idf #d, 5000

#result2 = result ** 2

#sum_result = np.zeros((document_cnt, 5000), dtype=float)
#temp = result.sum(axis=1)

#for i in range(0, document_cnt):
#    sum_result[i] = temp[i]
#sum_result = sum_result ** 0.5

#tf_idf = np.zeros((document_cnt, 5000))
#tf_idf = result/sum_result


# write
cnt=-1
for (path, dir, files) in os.walk("c:/term/Input_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.txt':
            fullname2 = "c:/DataMining/"+filename
            cnt+=1
            try:
                with open(fullname2, "w", encoding="utf-8") as w:
                    for j in range(0, 5000):
                        w.write(str(result[cnt][j])+"\t")
            finally:
                w.close()


w2 = open("c:/DataMining/word/word.txt", "w", encoding="utf-8")
w3 = open("c:/DataMining/word/idf.txt", "w", encoding="utf-8")

for i in range(0, 5000):
    data = fre_word[i]
    data2 = write_idf[i]
    w2.write(data+"\t")
    w3.write(str(data2)+"\t")

w2.close()
w3.close()
