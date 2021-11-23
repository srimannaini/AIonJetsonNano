gradeArray=[]
numGrades=int(input("How many grades do you have: "))
for i in range(0,numGrades,1):
	newGrade=float(input("Enther the next grade: "))
	gradeArray.append(newGrade)
print("")
print("Your grades are: ")
for i in range(0,numGrades,1):
	print(gradeArray[i])
bucket=0
for i in range(0,numGrades,1):
	bucket=bucket+gradeArray[i]
average=bucket/numGrades
print("")
print("Your average is: ",average)
print("")
highGrade=0
lowGrade=100
for i in range(0,numGrades,1):
	if gradeArray[i]<lowGrade:
		lowGrade=gradeArray[i]
	if gradeArray[i]>highGrade:
		highGrade=gradeArray[i]
print("Your high gradeis: ",highGrade)
print("Your Low Grade is: ",lowGrade)
