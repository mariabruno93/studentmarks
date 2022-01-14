# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:04:11 2022

@author: 001027613
"""

#Read the names and marks of at least 3 students
#Rank the top three students with the highest marks
#Give cash rewards. $500 for the first rank. $300 for the second and $100 for the thrid rank. Value can not be modified
#Appreciate students who secured  9 marks and above.

import operator

def readStudentdetails():
    print()
    print("Enter the number of students:")
    numberofstudents = int(input())
    #student record es un diccionario para guarda la key: name y e value: mark
    studentrecord = {}
    for students in range (0, numberofstudents):
        print("Enter the name of the student")
        name= input()
        print("Enter the mark of this student")
        mark= int(input())
        studentrecord[name] = mark
    #return student record para que este diccionario pueda usarse en otra funcion
    print()
    return studentrecord
    
        
def rankstudents(studentrecord):
    print()
    sortedstudentrecord = sorted(studentrecord.items(), key = operator.itemgetter(1), reverse = True)
    print(sortedstudentrecord)
    print("{} has secured the first rank, scoring {} marks".format(sortedstudentrecord[0][0], sortedstudentrecord[0][1]))
    print("{} has secured the second rank, scoring {} marks".format(sortedstudentrecord[1][0], sortedstudentrecord[1][1]))
    print("{} has secured the thrird rank, scoring {} marks".format(sortedstudentrecord[2][0], sortedstudentrecord[2][1]))
    print()
    return sortedstudentrecord
    

def rewardstudents(sortedstudentrecord, reward):
    print()
    print ("{} has received a cash reward of {} USD".format(sortedstudentrecord[0][0], reward[0]))
    print ("{} has received a cash reward of {} USD".format(sortedstudentrecord[1][0], reward[1]))
    print ("{} has received a cash reward of {} USD".format(sortedstudentrecord[2][0], reward[2]))
    print()
    
def appreciatestudents(sortedstudentrecord):
    print()
    for record in sortedstudentrecord:
        if record[1] >= 9:
            print("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else: 
            break
    print()
    

studentrecord = readStudentdetails()
sortedstudentrecord = rankstudents(studentrecord)
reward = (500, 300, 100)
rewardstudents(sortedstudentrecord, reward)
appreciatestudents(sortedstudentrecord)

