gArray=[]
nGrades=int(input("How many grades do you have? "))
for  i in range(0,nGrades,1):
	grade=float(input("Enter you grade: "))
	gArray.append(grade)
print("Your grades are:")
for  i in range(0,nGrades,1):
	print(gArray[i])
print("")
bucket=0
for  i in range(0,nGrades,1):
	bucket=bucket+gArray[i]
av=bucket/nGrades
print("Your Average Is: ",av)
lowGrade=100
highGrade=0
for i in range(0,nGrades,1):
	if gArray[i]>highGrade:
		highGrade=gArray[i]
	if gArray[i]<lowGrade:
		lowGrade=gArray[i]
print("")
print('Your high grade is: ',highGrade)
print('Your low grade is: ',lowGrade)
breadCrumb=1
while (breadCrumb==1):
	breadCrumb=0
	for i in range(0,nGrades-1,1):
		if gArray[i]>gArray[i+1]:
			swap=gArray[i]
			gArray[i]=gArray[i+1]
			gArray[i+1]=swap
			breadCrumb=1
print('')
print('Your sorted grades are: ')
for i in range(0,nGrades,1):
	print(gArray[i])

