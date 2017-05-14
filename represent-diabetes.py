# import needed libraries 
import csv
import numpy as np
import matplotlib.pyplot as plt

# function that loads the data set from csv file
def loadCSV():
	path = "diabetes.csv"
	data = [[] for x in xrange(9)]
	with open(path, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			rowSectors = row[0].split(',')
			for i in xrange(0,9):
				data[i].append(float(rowSectors[i]))		
	return data


def main():
	# load data from csv file
	dataset = loadCSV() 
	# subsets needed
	pregrnancies = dataset[0]
	glucose = dataset[1]
	bloodPressure = dataset[2]
	skinThickness = dataset[3]
	insulin = dataset[4]
	bMI = dataset[5]
	diabetesPedigreeFunction = dataset[6]
	age = dataset[7]
	label = dataset[8]
	# lets plot 2D age vs pregrnancies
	#plt.figure(figsize=(10, 6), dpi=80)
	#plt.plot(age, pregrnancies, 'bo', color="blue")
	#plt.plot(age, label,'bo' ,color="red")
	# -----------------
	# lets make sub groups as has diabetes and dont have diabetas
	sickAge =[]
	not_sickAge=[]
	sickPreg =[]
	not_sickPreg=[]
	sickSkin=[]
	not_sickSkin = []
	sickGlo=[]
	not_sickGlo=[]
	for s in range (0,len(age)):
		if (label[s] ==0):
			not_sickAge.append(age[s])
			not_sickPreg.append(pregrnancies[s])
			not_sickSkin.append(skinThickness[s])
			not_sickGlo.append(glucose[s])
		else:
			sickAge.append(age[s])
			sickPreg.append(pregrnancies[s])
			sickSkin.append(skinThickness[s])
			sickGlo.append(glucose[s])
	# lets now make another sub groups with the size 
	# of the point as size of glocose or skinthikness
	plt.figure(figsize=(74, 50), dpi=70)
	for i in range (0, len(not_sickSkin)):
		plt.plot(not_sickAge[i], not_sickPreg[i], 'bo', markersize=not_sickSkin[i], markeredgecolor='black', color="blue")
	for j in range (0, len(sickSkin)):
		plt.plot(sickAge[j], sickPreg[j],'bo' ,markersize=sickSkin[j], markeredgecolor='black',color="red")
	# ------------------
	plt.xlabel('Women Age')
	plt.ylabel('Number of pregrnancies')
	plt.title('Age vs #pregrnancies vs Sick or not vs Skinthikness')
	plt.grid(True)
	plt.xlim((15,90))
	plt.ylim((-4,20))
	#def onclick(event):
    #print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #      (event.button, event.x, event.y, event.xdata, event.ydata))
	#cid = fig.canvas.mpl_connect('button_press_event', onclick)
	#plt.canvas.mpl_disconnect(cid)

	# Save figure using 72 dots per inch
	# plt.savefig("exercice_2.png", dpi=72)
	
	# Show result on screen
	plt.show()






main()


#['Pregrnancies'],row['Glucose'],row['BloodPressure'],row['SkinThickness'],row['Insulin'],row['BMI'],row['DiabetesPedigreeFunction'],row['Age'],row['Outcome',row