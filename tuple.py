#----items() return tuple, sorted function 

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
newerlst=list()
count=dict()
newlist=list()

for yo in handle:
	if yo.startswith('From '):
		lst=yo.split()
		istring=lst[5]
		newlst=istring.split(':')
		newerlst.append(newlst[0])
		
for ha in newerlst:
	count[ha]=count.get(ha,0)+1
	
yolo=sorted(count.items())
for x,y in yolo:
	print (x,y)
