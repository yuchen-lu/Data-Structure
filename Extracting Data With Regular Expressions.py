import re

ha=list()
final2=list()
str1=str()
str2=str()

datafile =open('C:\\New folder\\regex_sum_26580.txt')

for yo in datafile:
  print(yo)
  yo2=re.findall('[0-9]+',yo)
 # print(yo2)
#  str1=''.join(yo2)
#    if lo !=' '
  for yolo in yo2:
      ha.append(yolo)
 # ha.append(str1)
  #print(str1)
#print(ha)  

for final in ha:
  final2.append(float(final))
  
finalsum=sum(final2)
print(finalsum)




  
