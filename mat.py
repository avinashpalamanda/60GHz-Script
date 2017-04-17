import scipy.io
import matplotlib.pyplot as plt
import os
os.system("clear")

loc1="/home/avinash/Desktop/60ghz project/outdoor/8/rssi"
loc2="/home/avinash/Desktop/60ghz project/outdoor/12/rssi"
loc3="/home/avinash/Desktop/60ghz project/outdoor/23/rssi"

#folder=["/15feet","/25feet"]
folder1=["/15feet","/25feet","/35feet","/45feet","/55feet","/65feet","/75feet","/85feet","/95feet","/105feet","/125feet","/135feet"]
folder2=["/15feet","/25feet","/35feet","/45feet","/55feet","/65feet","/75feet","/85feet","/95feet","/105feet","/125feet","/135feet"]
folder3=["/15feet","/25feet","/35feet","/45feet","/55feet","/65feet","/75feet"]

filename=["/1.mat","/2.mat","/3.mat","/4.mat","/5.mat"]
mainloc=[loc1,loc2,loc3]
mainfolder=[folder1,folder2,folder3]	

finallist=[]
n=0

while n<3:
	mainlist=[]
	explist=[]
	datalist=[]

	loc=mainloc[n]
	folder=mainfolder[n]
	i=0
	j=0
	while i < len(folder):
		j=0
		while j < len(filename):
			#print j
			#print loc+folder[i]+filename[j]
			x = scipy.io.loadmat(loc+folder[i]+filename[j])
			pya=x["analog_channel_0"]
			for k in pya:
				data = float(k)
				datalist.append(data)
	
			explist.append(sum(datalist)/len(datalist))
			#print explist
			datalist=[]
			j=j+1
		#print explist
		x = sum(explist)/len(explist)
		print x
		#y = 7.7295*x*x*x - 40.394*x*x + 90.863*x - 98.443
		y = 7.7295*x**3 - 40.394*x**2 + 90.863*x - 98.443		
		mainlist.append(y)
		explist=[]
		i=i+1
	#print mainlist
	finallist.append(mainlist)
	n=n+1

print "Outdoor\n"
print finallist[0]
print finallist[1]
print finallist[2]
feet1=[15,25,35,45,55,65,75,85,95,105,125,135]
feet2=[15,25,35,45,55,65,75]
plt.subplot(2,1,1)
plt.xlabel("Feet")
plt.ylabel("Power in dB")
plt.title("Outdoor")
plt.plot(feet1,finallist[0],'r',feet1,finallist[1],'g',feet2,finallist[2],'b')
#plt.show()
#######################################################################################################################################33
loc1="/home/avinash/Desktop/60ghz project/indoor/8/rssi"
loc2="/home/avinash/Desktop/60ghz project/indoor/12/rssi"
loc3="/home/avinash/Desktop/60ghz project/indoor/23/rssi"

#folder=["/15feet","/25feet"]
folder1=["/15feet","/25feet","/35feet","/45feet","/55feet","/65feet","/75feet","/85feet","/95feet","/105feet"]
folder2=["/15feet","/25feet","/35feet","/45feet","/55feet","/65feet","/75feet","/85feet"]
folder3=["/15feet","/25feet","/35feet","/45feet","/55feet"]

filename=["/1.mat","/2.mat","/3.mat","/4.mat","/5.mat"]
mainloc=[loc1,loc2,loc3]
mainfolder=[folder1,folder2,folder3]	

finallist=[]
n=0

while n<3:
	mainlist=[]
	explist=[]
	datalist=[]

	loc=mainloc[n]
	folder=mainfolder[n]
	i=0
	j=0
	while i < len(folder):
		j=0
		while j < len(filename):
			#print j
			#print loc+folder[i]+filename[j]
			x = scipy.io.loadmat(loc+folder[i]+filename[j])
			pya=x["analog_channel_0"]
			for k in pya:
				data = float(k)
				datalist.append(data)
	
			explist.append(sum(datalist)/len(datalist))
			#print explist
			datalist=[]
			j=j+1
		#print explist
		x = sum(explist)/len(explist)
		print x
		#y = 7.7295*x*x*x - 40.394*x*x + 90.863*x - 98.443
		y = 7.7295*x**3 - 40.394*x**2 + 90.863*x - 98.443		
		mainlist.append(y)
		explist=[]
		i=i+1
	#print mainlist
	finallist.append(mainlist)
	n=n+1

print "Outdoor\n"
print finallist[0]
print finallist[1]
print finallist[2]
feet1=[15,25,35,45,55,65,75,85,95,105]
feet2=[15,25,35,45,55,65,75,85]
feet3=[10,15,20,25,30]

plt.subplot(2,1,2)
plt.xlabel("Feet")
plt.ylabel("Power in dB")
plt.title("Indoor")
plt.plot(feet1,finallist[0],'r',feet2,finallist[1],'g',feet3,finallist[2],'b')
plt.show()

