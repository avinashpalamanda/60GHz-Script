import json
#import pyexcel as pe
import matplotlib.pyplot as plt
import os
os.system("clear")

name1 = "/home/avinash/Desktop/60ghz project/indoor/8/json"
name2 = "/home/avinash/Desktop/60ghz project/indoor/12/json"
name3 = "/home/avinash/Desktop/60ghz project/indoor/23/json"

loc1=["/15feet","/25feet","/35feet","/45feet","/55feet"]
loc2=["/15feet","/25feet","/35feet","/45feet"]
loc3=["/15feet"]

mainloc=[loc1,loc2,loc3]
mainname=[name1,name2,name3]
finallist=[]
n =0

while n < 3:

	explist=[]
	mainlist=[]
	
	name=mainname[n]
	loc=mainloc[n]
	files=["/1.json","/2.json","/3.json","/4.json","/5.json"]
	#files=["/1.json"]

	j=0
	i=0
	while i < len(loc):
		#print loc[i]
		j=0
		while j < len(files):
			#print name+loc[i]+files[j]
			handle = open(name+loc[i]+files[j]).read()
			info = json.loads(str(handle))
			data1=info["end"]["sum_received"]["bits_per_second"]
			data1=float(data1)*0.000001
			explist.append(data1)
			j=j+1
		i=i+1
		mainlist.append(sum(explist)/len(explist))
		explist=[]
	
	x = len(mainlist)
	if x < 14:
		while x < 14:
			mainlist.append(0)
			x = x+1
#	print mainlist
	finallist.append(mainlist)
	n=n+1


feet=[15,25,35,45,55,65,75,85,95,105,115,125,135,145]

print "Indoor\n"
print finallist[0]
print finallist[1]
print finallist[2]

plt.subplot(2,1,1)
plt.xlabel("Feet")
plt.ylabel("Throughput")
plt.title("Indoor")
plt.plot(feet,finallist[0],'r',feet,finallist[1],'g',feet,finallist[2],'b')
#plt.show()


##################################################################################################################################################################
name1 = "/home/avinash/Desktop/60ghz project/outdoor/8/json"
name2 = "/home/avinash/Desktop/60ghz project/outdoor/12/json"
name3 = "/home/avinash/Desktop/60ghz project/outdoor/23/json"

loc1=["/15feet/test","/25feet/test","/35feet/test","/45feet/test","/55feet/test","/65feet/test","/75feet/test","/85feet/test","/95feet/test","/105feet/test","/115feet/test","/125feet/test","/135feet/test"]
loc2=["/15feet/test","/25feet/test","/35feet/test","/45feet/test","/55feet/test","/65feet/test","/75feet/test","/85feet/test","/95feet/test","/105feet/test","/115feet/test","/125feet/test","/135feet/test"]
loc3=["/15feet/test","/25feet/test","/35feet/test","/45feet/test","/55feet/test"]

mainloc=[loc1,loc2,loc3]
mainname=[name1,name2,name3]
finallist=[]
n =0

while n < 3:

	explist=[]
	mainlist=[]
	
	name=mainname[n]
	loc=mainloc[n]
	files=["/1.json","/2.json","/3.json","/4.json","/5.json"]
	#files=["/1.json"]

	j=0
	i=0
	while i < len(loc):
		#print loc[i]
		j=0
		while j < len(files):
			#print name+loc[i]+files[j]
			handle = open(name+loc[i]+files[j]).read()
			info = json.loads(str(handle))
			data1=info["end"]["sum_received"]["bits_per_second"]
			data1=float(data1)*0.000001
			explist.append(data1)
			j=j+1
		i=i+1
		mainlist.append(sum(explist)/len(explist))
		explist=[]
	
	x = len(mainlist)
	if x < 14:
		while x < 14:
			mainlist.append(0)
			x = x+1
#	print mainlist
	finallist.append(mainlist)
	n=n+1

print "Outdoor\n"
print finallist[0]
print finallist[1]
print finallist[2]
plt.subplot(2,1,2)
r=plt.plot(feet,finallist[0],'r',feet,finallist[1],'g',feet,finallist[2],'b')
plt.xlabel("Feet")
plt.ylabel("Throughput")
plt.title("Outdoor")

plt.show()

