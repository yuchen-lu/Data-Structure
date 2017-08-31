fname = input("Enter file name: ")

fh = open(fname)

for cheese in fh:
	cheese2=cheese.upper()
	print(cheese2.rstrip())
	
	
	
#-------------------------------------------------------------


fname = input("Enter file name: ")
count=1
sun1=0
fh = open(fname)
for line in fh:
    
	if  line.startswith("X-DSPAM-Confidence:") :
		index1=line.find(' ')
		index2=line.find(' ', index1)
		rawnum=line[index2+1:]
		
		finalnum=rawnum.rstrip()
		
		sun1=sun1+float(finalnum)
		count=count+1
	if not line.startswith("X-DSPAM-Confidence:") : 
		continue

        
    
    
    
print('Average spam confidence:', sun1/count)    
print("Done")

