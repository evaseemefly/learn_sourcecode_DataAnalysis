names =input("Enter names separated by commas: ").title().split(",")
assignments=int(input("Enter assignment counts separated by commas: ").split(",")
grades=input("Enter grades separated by commas: ").split(",")

for i in range(len(names)):
    print("Hi "+ str(2*assignments[i]+grades[i]))
          #+names[i]+",\nThis is a reminder that you have "+assignments[i]+"assignments left to submit before you can graduate. Your current grade is "+grades[i]+" and can increase to "+str(eval(2*assignments[i]+grades[i]))+" if you submit all assignments before the due date.")

