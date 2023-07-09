Python Group Final Project 2022 -- Humber College

#### Introduction:
We are asked to create a Python program for the admission department of Humber College. The system should store information about the newly admitted students and assign them to schools according to their GPA. The system must prompt the user to enter the name of each student, and the grades of the courses they completed in the high school. Then, the system should calculate the GPA and use it to assign students the schools.

<img width="1001" alt="image" src="https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/b090be25-200b-46d6-a258-1572f4fd895b">


#### System Requirements:
1) When the program starts, a welcoming message will appear: "Welcome to Humber College."

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/5e074fd5-1eed-4365-b376-27f5129ad4c4)

2) Allow the user to login using a password with following rules:
    + Should not be less than 10 characters.
    + Should contain at least one upper case letter.
    + Should contain two or three numbers.
    + Should contain one special character.
    Check points:
    + If the password is incorrect, the system must ask the user to enter new password. The system must allow the user only three attempts.
    + If the password is align with all above conditions, the system will continue.

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/0bc50fc4-4a06-4366-ad7c-04b646ded9f0)

3) After password checking, the system must ask the user to enters any other number, the system must allow the user only three attempts, otherwise the program will stop.

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/8c5249d5-7048-4fbe-82c8-21f606c28f9c)

4) After the above step, the system must ask the user to enter the name of students

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/ec83e295-cf37-4307-b202-7627624997d3)

5) The system must prompt the user to enter grades of each student as follows:
    + Math         >> Credit hours = 4
    + Science      >> Credit hours = 5
    + Language     >> Credit hours = 4
    + Drama        >> Credit hours = 3
    + Music        >> Credit hours = 2
    + Biology      >> Credit hours = 4

6) The system must calculate the GPA of each student based on the grades that were entered in the previous step according to the following function.

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/9a521c47-dc7d-4520-a881-34317fc6c2f4)

7) The system must assign students to schools based on the following matrix:
    + School of Engineering    90 >= GPA <= 100
    + School of Business       80 >= GPA <= 90
    + School of Law            70 >= GPA <= 80
    + Not accepted             GPA < 70

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/d73a27b7-3f77-4767-bec9-e7f889d1af12)

8) The system must be able to print the following reports:

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/ab9d5ec1-000e-4975-9587-c6b0cd0dd3f2)

+ Report1: Student Name, School Name

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/eba800dc-f7db-447b-a75e-264bc957c115)

+ Report2: Number of accepted students in Humber College showing students distribution per each school

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/16280d46-f0d7-4bc3-b3c2-0037d57199fd)

+ Report3: Number of Students that not accepted

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/832053b0-2015-4804-9c97-291a34da839d)

+ Report4: Percentage of students who are accepted to each school and not accepted

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/1c806298-ca24-4005-abc9-5e9060f20b01)


#### Test Cases & Steps:

<img width="1002" alt="image" src="https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/3f1a7fb0-ea2b-4c0e-8f3d-59ce2a285377">


#### Example of Report4: 
The percentage of students who are accepted to each school and not accepted.

![image](https://github.com/vcmeghan/Python-Admission-Program/assets/100189862/e89fd96c-50b3-4cee-8977-da2f0b6238a5)

