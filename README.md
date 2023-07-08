# Python Group Final Project 2022 -- Humber College

#### Introduction:
We are asked to create a Python program for the admission department of Humber College. The system should store information about the newly admitted students and assign them to schools according to their GPA. The system must prompt the user to enter the name of each student, and the grades of the courses they completed in the high school. Then, the system should calculate the GPA and use it to assign students the schools.

<img width="1001" alt="image" src="https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/b090be25-200b-46d6-a258-1572f4fd895b">


#### System Requirements:
1) When the program starts, a welcoming message will appear: "Welcome to Humber College."

[image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/627042ee-5a97-4ef5-8097-8153d0654872)

2) Allow the user to login using a password with following rules:
    + Should not be less than 10 characters.
    + Should contain at least one upper case letter.
    + Should contain two or three numbers.
    + Should contain one special character.
    Check points:
    + If the password is incorrect, the system must ask the user to enter new password. The system must allow the user only three attempts.
    + If the password is align with all above conditions, the system will continue.

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/2162b734-f0e5-4938-a0a9-196f299e6e27)

3) After password checking, the system must ask the user to enters any other number, the system must allow the user only three attempts, otherwise the program will stop.

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/84d27351-b801-4c2e-97e8-35f76e708ef3)

4) After the above step, the system must ask the user to enter the name of students

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/54113301-a7af-4d42-973d-2cf4702e12a7)

5) The system must prompt the user to enter grades of each student as follows:
    + Math         >> Credit hours = 4
    + Science      >> Credit hours = 5
    + Language     >> Credit hours = 4
    + Drama        >> Credit hours = 3
    + Music        >> Credit hours = 2
    + Biology      >> Credit hours = 4

6) The system must calculate the GPA of each student based on the grades that were entered in the previous step according to the following function.

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/f91c8eb9-e168-44cf-a18a-8e38e0629685)

7) The system must assign students to schools based on the following matrix:
    + School of Engineering    90 >= GPA <= 100
    + School of Business       80 >= GPA <= 90
    + School of Law            70 >= GPA <= 80
    + Not accepted             GPA < 70

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/5c36df0d-c3c8-4ec3-9b4e-a6953eba54f6)

8) The system must be able to print the following reports:

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/b8039f2f-94f6-4830-94e0-b06281e22bd8)

+ Report1: Student Name, School Name

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/123fcc72-019c-433d-bf53-047f070659e1)

+ Report2: Number of accepted students in Humber College showing students distribution per each school

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/999c3041-b5bf-4346-b58b-ef3672c9caaf)

+ Report3: Number of Students that not accepted

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/9aa9f49c-86f7-4a54-ac83-04a4e4d485dd)

+ Report4: Percentage of students who are accepted to each school and not accepted

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/c0b30cc1-c279-479e-8690-2054cd9766da)


#### Test Cases & Steps

<img width="1002" alt="image" src="https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/82485bf7-e3d0-4bbe-b693-28f5ed64e516">


Example of Report4: The percentage of students who are accepted to each school and not accepted.

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/74429b0d-958f-455b-8842-61601beac37d)
