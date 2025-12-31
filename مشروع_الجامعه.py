# To fix the ModuleNotFoundError, install the 'colorama' library
#!pip install colorama

#*---------------*
#Requirements
#- Python 3.x
#- colorama

## How to Run
#1. Install colorama:
#   pip install colorama
#2. Run the project:
#   python main.py
#*------------------*
'''
This project was made by
1. Student Name : yazan abushareefih
   Student ID : 193336
2. Student Name : Mohamad Alqudah
   Student ID :  185892
3. Student Name : Omar Duraidi
   Student ID : 190872
   university -------> Jordan University of Science and Technology (JUST)
'''

import os
from colorama import Fore,Style
# Unrequired functions


def main_menu():
    '''
    This function displays the main menu

    Returns
    -------
    user_inp : String
        Represents the user choice

    '''
    user_inp = input('1. Existing students\n2. New student\n3. Exit\n')
    return user_inp

def sub_menu(in_students,student_id):
    '''
    This function display the secondary menu

    Parameters
    ----------
    in_students : Dictionary
        You should bypass the main dictionary
    student_id : String
        You should by pass the student id entered by the user

    Returns
    -------
    None.

    '''
    msg11 = '1. Enroll Courses\n'
    msg12 = '1. Update Courses\n'

    msg21 = '2. Add grades\n'
    msg22 = '2. Update grades\n'

    msg31 = '3. View student report\n'

    msg41 = '4. Exit\n'

    mymsg = '' #this is the variable that controls the the text in the list

    while True:
        os.system('cls')

        if 'courses' not in  in_students[student_id]:
            mymsg = msg11
            mymsg += disabled_msgs(msg21)
            mymsg += disabled_msgs(msg31)
            mymsg += msg41
            mode = 1 #This variable manipulates the state of the message or text being displayed

        elif 'grades' not in in_students[student_id]:
            mymsg = msg12
            mymsg += msg21
            mymsg += disabled_msgs(msg31)
            mymsg += msg41
            mode =2 #This variable manipulates the state of the message or text being displayed
        else:
            mymsg = disabled_msgs(msg12)
            mymsg += msg22
            mymsg += msg31
            mymsg += msg41

            mode = 3 #This variable manipulates the state of the message or text being displayed


        match input(f'{mymsg}').strip():#asks the user to enter input and match it with 3 cases

            case '1':
                if mode == 1 :
                    enroll_courses(in_students,student_id)

                elif mode == 2 :
                    update_courses(in_students,student_id)

                else :
                   print('You can\'t update courses after adding the grades\n')
                   continue



            case '2':
                if mode == 1:
                    print('You cant\'t add grades before being enrolled on courses\n')
                    continue

                elif mode == 2:
                    add_grades(in_students,student_id)

                else:
                    update_grades(in_students,student_id)




            case '3':
                if mode == 1 :
                    print('You can\'t view courses before being enrolled in them\n')
                    continue

                elif mode == 2:
                    print('You cant\'t view grades before adding them\n ')
                    continue

                else:
                    generate_report(in_students, student_id)

            case '4':
                print('Heading to the main menu........\n')
                break

            case _:
                print('Invalid input .......\n')

def get_student_id (in_students_ids):
    '''
    This function takes the student id as input and checks if it's duplicated or not
    If its duplicated it will return nothing (None)
    Otherwise it will return the student_id entered


    Parameters
    ----------
    in_students_ids : Set
        student_ids are stored here to prevent duplication

    Returns
    -------
    student_id : string
        this is the unique student id that the user entered

    '''

    student_id = input('Enter student id:\t')

    if student_id not in in_students_ids :
        print(f'{student_id} was not found\n\
              \rHead to the university adminstration to add your ID\n')
        return None

    print(f'{student_id} was found\n')

    return student_id

def update_grades (in_students , student_id):

     '''
     this is an inner function used in the secondry menu to update the grades if condtions are met.

     Parameters
     ----------
        in_students : Dictionary
            You should bypass the main dictionary
        student_id : String
            You should by pass the student id entered by the user

     Returns
     -------
     None.

     '''

     courses = list(set(input('\nEnter the courses you want to update seperated by commas --->\t').split(',')))
     for course in courses :

         if course not in in_students[student_id]['courses']:
             print(f'{course} was not found')
             continue

         grade_inp = input(f'Enter the {course} grade\n')

         print(f"course: {course}",f" grade : {grade_inp}")

         if grade_inp.lower().strip() == '':
             grade_inp = '0'

         while not grade_inp.isdecimal():
             print('\nError......\n you can only enter postive integers\n')
             grade_inp = input(f'Enter the {course} grade\n')

         in_students[student_id]['grades'][in_students[student_id]['courses'].index(course)]  = int(grade_inp)
         print(f'{grade_inp} was add successfuly')

def update_courses (in_students, student_id):
    '''
    Tthis is an inner function that is used the secondary menu (sub_menu) to update the courses if the conditions are met

    Parameters
    ----------
    in_students : Dictionary
        You should bypass the main dictionary
    student_id : String
        You should by pass the student id entered by the user


    Returns
    -------
    None.

    '''


    current_courses = in_students[student_id]['courses']

    new_courses = set(input('\nEnter the courses seperated by commas --->\t').split(','))

    final_courses =set(new_courses.union(current_courses))

    in_students[student_id]['courses'] = list(final_courses)

    print(f'The courses {list(new_courses)} were added successfuly')

def disabled_msgs(msg):
    return Fore.WHITE + Style.DIM + msg +Style.RESET_ALL

# Required functions

def add_student(in_students, in_students_ids):
    '''
      This function is used to add students entered by user
      Each student id is unique
      And if the student id is duplicated the function with return nothing


      Parameters
      ----------
    in_students : Dictionary
    You should bypass the main dictionary
    student_id : String
    You should by pass the student id entered by the user


      Returns
      -------
      None.

      '''

    stu_id = input('\nEnter the student id--->\t')

    if stu_id in in_students_ids:
        print('Error.....\nStudent id already exists\nDuplication is not allowed\n')
        return

    in_students_ids.add(stu_id) #to store a value in a set we use .add() method

    stu_name = input('\nEnter the student name--->\t')

    in_students[stu_id] = {'name' : stu_name}

    print(f'\nStudent id: {stu_id} was added successfuly\nStudent name: {stu_name} was added successfuly\n')

def enroll_courses (in_students,student_id):
     '''
     This function is used in the secondry menu (sub_menu)
     Enrolls the student in courses for the first time if the condtions were ment

     Parameters
     ----------
    in_students : Dictionary
        You should bypass the main dictionary
    student_id : String
        You should by pass the student id entered by the user


     Returns
     -------
     None.

     '''

     in_students[student_id].update({'courses' : []})

     new_courses = set(input('\nEnter the courses seperated by commas --->\t').split(','))

     in_students[student_id]['courses'] = list(new_courses)

     print(f'The courses {list(new_courses)} were added successfuly')

def add_grades (in_students,student_id):
    '''
    This function is used in the secondery menu (sub_menu) to add grades if the conditions are met



    Parameters
    ----------
    in_students : Dictionary
        You should bypass the main dictionary
    student_id : String
        You should by pass the student id entered by the user

    Returns
    -------
    None.

    '''

    in_students[student_id].update({'grades': []})

    for course in in_students[student_id]['courses']:

        grade_inp = input(f'\nEnter the {course} grade\n')

        if grade_inp.strip() == '':
            grade_inp = '0'

        while not grade_inp.isdecimal(): #to validate if the output is numeric or not
            print('\nError......\n you can only enter postive integers\n')
            grade_inp = input(f'Enter the {course} grade\n')

        grade_inp =int(grade_inp)
        in_students[student_id]['grades'].append(grade_inp)
        print(f'{grade_inp} was add successfuly\n')

def generate_report(in_students,student_id):
     '''
     This functions is used in the secondary meny (sub_menu) to generate a report
     if condtions are met


     Parameters
     ----------
    in_students : Dictionary
        You should bypass the main dictionary
    student_id : String
        You should by pass the student id entered by the user


     '''

     average , MaximumGrade , MinimumGrade = calculate_average(in_students[student_id]['grades'])
     print(f'Student ID : {student_id}')
     print(f'Student Name : {in_students[student_id]["name"]}')
     print(f'Courses : {in_students[student_id]["courses"]}')
     print(f'Grades : {in_students[student_id]["grades"]}')
     print(f'Average : {average}')
     print(f'Highest grade : {MaximumGrade}')
     print(f'Lowest grade : {MinimumGrade}')

def calculate_average(grades):
    '''
    this function is an inner function that has been used only in the generate_report function
    to do sym calculations

    Parameters
    ----------
    grades : list
        DESCRIPTION.

    Returns
    -------
    avg : int
        average grades
    maxi : int
        maximum grade
    mini : int
        minimum grade

    '''
    avg = sum(grades)/len(grades)
    maxi = max(grades)
    mini = min(grades)
    return (avg,maxi,mini)


if __name__ == '__main__': #this sentence equals int main()

    students ={} #required from prof.
    students_ids = set() #required from prof.


    while True: #Your program must include a loop-based menu
        os.system('cls')

        match main_menu().strip(): #returns the user input to use the menu

            case '1':
                os.system('cls')

                student_id = get_student_id(students_ids)

                if student_id :
                    sub_menu(students, student_id)

            case '2':

                os.system('cls')

                add_student(students,students_ids)

            case '3':

                os.system('cls')

                print('Exiting system........\n')

                break

            case _:
                os.system('cls')
                print('\nInvalid input\nChoose from the list from 1 to 5\n')