import sys  #Importing sys library


print("\t\t\t  Welcome to Humber College")
print("\n")

Num_attempts=0


while True:  #Initialize an infinite loop
    pwlist = input("Please enter your password: ")    #Asking the user for password


    i = 0
    countnumeric = 0
    countupper = 0
    countspecial = 0
    countalpha = 0
    specialchar = "'!@#$%^&*()_-+={}[]:;|\~`<>,./?"
    

    for i in range(len(pwlist)):   
        
        if pwlist[i].isnumeric():
            countnumeric += 1
        elif pwlist[i].isupper():
            countupper += 1
        elif pwlist[i] in specialchar:
             countspecial += 1
        else:  countalpha += 1   

    #Checking if the entered password meets the mentioned criteria
    if countupper >= 1 and countspecial == 1 and (countnumeric == 2 or countnumeric == 3) and len(pwlist)>=10: 
        print("\n")
        print("\t\tWelcome to Admission Portal of Humber College\n\n")
        
        
        break

    else:
        Num_attempts+=1
    if Num_attempts==3:
        print("You are out of tries to enter password. Please try after sometime again.")
        sys.exit()   #Ending the program after 3 wrong attempts

    print("\nPlease try again\n")

Num_attempts2=0  #For check on attempts of Number of students

while True:   #Infinite loop

    studentno = int(input("Please enter number of students "))  #asking user for number of students

    if studentno<1 or studentno>50: 
        Num_attempts2+=1
        if Num_attempts2<3:
            print("\nPlease enter correct number\n")
            continue
        else:
            print("You are out of tries to enter student numbers")
            sys.exit()  #Ending the program after 3 wrong attempts
    else:  
        break

def Names(studentno):    #defining function "Names" for the user to enter names
    names=[]
    for i in range(studentno):  #Running loop through Number of students entered
        names.append(input(f"Please enter the name of student {i+1}: "))
    return names #Returning the list with names of students

print("\n")

names=Names(studentno) #calling function names

def GPA(studentno):    
    grade=[]
    
    for i in range(studentno):
        math = float(input(f"\nInput marks of {names[i]} in Math, Credit hours = 4: "))
        science = float(input(f"Input marks of {names[i]} in Science, Credit hours = 5: "))
        language = float(input(f"Input marks of {names[i]} in Language, Credit hours = 4: "))
        drama = float(input(f"Input marks of {names[i]} in Drama, Credit hours = 3: "))
        music = float(input(f"Input marks of {names[i]} in Music, Credit hours = 2: ")) 
        biology = float(input(f"Input marks of {names[i]} in Biology, Credit hours = 4: "))
        print("\n")
        gpa = ((math*4)+(science*5)+(language*4)+(drama*3)+(music*2)+(biology*4))/22  #Calculation of gpa according the marks entered in each subject
        grade.append(gpa)
    return grade #Returning grade of each student

grades=GPA(studentno)   

def school(grades):
    School=[]
    for i in range(len(grades)):
        if grades[i] >= 90:
           School.append('School of Engineering')
        elif grades[i] >= 80 and grades[i]<90:
           School.append('School of Business')
        elif grades[i] >= 70:
           School.append('Law School')
        else:
           School.append('Not accepted')
    return School  #Returning the list of assigned school of students according to their grades

name_school=school(grades)


#Description of reports
print("\n")
print("Report 1: Name and School of students")
print("Report 2: Number of accepted students in Humber college showing students distribution per each school")
print("Report 3: Number of students not accepted")
print("Report 4: Grades of students\n")


                                                                
while True:
    x=int(input("Enter the input 1,2 or 3 or 4 to open any of the above reports. Press 0 to exit. ")) #Asking the user for which report to be opened
    print("\n")


                                                                #Report1
    if x!=0:
        if x==1:
           for i in range(studentno):
               print(i+1, ".", names[i],"\t",name_school[i]) 
           print("\n")
    

 

                                                                #Report2
        
        if x==2:
           print("Number of Students accepted in Law School= ",name_school.count("Law School"))
           print("Number of Students accepted in School of Business= ",name_school.count("School of Business"))
           print("Number of Students accepted in School of Engineering= ",name_school.count("School of Engineering"))
           print("\n")
    

        
                                                                #Report3
        
        if x==3:
            print("Number of students not accepted: ", name_school.count("Not accepted"))
            print("\n")

                                                                #Report4
            
        if x==4:
            print("Total percentage of students in School of Engineering is", (name_school.count("School of Engineering")/studentno)*100, "%" )
            print("Total percentage of students in Law School is", (name_school.count("Law School")/studentno)*100, "%"  )
            print("Total percentage of students in School of Business is", (name_school.count("School of Business")/studentno*100), "%" )
            print("Total", (name_school.count("Not accepted")/studentno)*100, "% of students could not make it to Humber College this year.\n" )
      



        elif x not in (0,1,2,3,4):
            print("Please enter correct input\n")       #Condition check on the Report input
           

    else: break




print("\t\t\t  Thank you")
               
    

                                                                


    





        


         
    
    






        
