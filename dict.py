#-----find most frequenct address, return number and address using dict()

newlst=list()
count=dict()
maxcount=None
maxadd=None

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for yo in handle:
    if yo.startswith('From '):
        lst=yo.split()
#        newlst= [ha for ha in lst if ha.isdigit()]
        newlst.append(lst[1])
        
        
        #lstmax1=max(newlist)
        #for ha in yo:
            #count=count(ha,0)+1
        #if lstmax1 < lstmax:
         #   lstmax=lstmax1
          #  addressmax=lst[1]         
for ha in newlst:
	count[ha]=count.get(ha,0)+1
        
            
maxcount=max(count.values()) 
for aaa,bbb in count.items():
    if bbb==maxcount:
        maxadd=aaa
print(maxadd,maxcount)
#print(lstmax)
        
