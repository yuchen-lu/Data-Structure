# -------sort list, split string, append list

fname = input("Enter file name: ")
fh = open(fname)
read = list()
read2=list()

for line in fh:
	read = line.split()
	index1=len(read)
	for i in range (0,index1):
		if read[i] not in read2 :
			read2.append(read[i])
            
	
	
read2.sort()
print(read2)



#------------print without string format, count, find keywords



fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst2=list()
lst=list()
for line in fh:
	
	if line.startswith('From '):
		lst=line.split()
		lst2.append(lst[1])
		print(lst2[count])
		count=count+1

print("There were", count, "lines in the file with From as the first word")
