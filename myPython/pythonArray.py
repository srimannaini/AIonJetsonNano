gradeArray=[]
numGrades=int(input("How many grades do you have? "))
for i in range(0,numGrades,1):
	grade=float(input("input the grade:"))
	gradeArray.append(grade)
for i in range(0,numGrades,1):
	print("Your ",i+1," grade is ",gradeArray[i])
print("Thank you for playing")

