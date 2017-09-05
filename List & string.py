# sort list, split string, append list

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