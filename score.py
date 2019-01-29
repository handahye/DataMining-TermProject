from sklearn.metrics import *

out = []
answer = []
max_index = 0
max = 0.0

path1 = "c:/DataMining/answer.txt"
path2 = "c:/DataMining/output.txt"
f1 = open(path1, 'r', encoding='UTF8')
f2 = open(path2, 'r', encoding='UTF8')

line1 = f1.readlines()
answer = line1
line2 = f2.readlines()
out = line2

cnt = 0
for j in line2:
   i = line1[cnt].replace("\n", "")
   for k in range(0, 9):
      output = j.split("\t")
      if k == 0:
         max = output[k]
         max_index = k
      else:
         if max < output[k]:
            max = output[k]
            max_index= k
   answer[cnt] = int(i)
   out[cnt] = max_index
   cnt += 1

f1.close()
f2.close()

print("Performance")
print("- Macro_F1 = " + str(f1_score(answer, out, average='macro')))
print()
print("- Total Prediction = " + str(precision_score(answer, out, average='micro')))
print("- Total Recall = " + str(recall_score(answer, out, average='micro')))
print("- Micro_F1 = " + str(f1_score(answer, out, average='micro')))