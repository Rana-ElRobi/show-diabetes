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
	for s in range (0,len(age)):
		if (label[s] ==0):
			not_sickAge.append(age[s])
			not_sickPreg.append(pregrnancies[s])
		else:
			sickAge.append(age[s])
			sickPreg.append(pregrnancies[s])
	# plot data as sick and not sick 
	plt.figure(figsize=(10, 6), dpi=80)
	plt.plot(not_sickAge, not_sickPreg, 'bo', color="blue")
	plt.plot(sickAge, sickPreg,'bo' ,color="red")

	# Save figure using 72 dots per inch
	# plt.savefig("exercice_2.png", dpi=72)
	
	# Show result on screen
	plt.show()






main()


#['Pregrnancies'],row['Glucose'],row['BloodPressure'],row['SkinThickness'],row['Insulin'],row['BMI'],row['DiabetesPedigreeFunction'],row['Age'],row['Outcome',row