# בפייתון כל דבר הוא אובייקט: משתנים, פונקציות, קבצים.
# לכל סוג של אובייקט יש: מידע (attributes): מידע של האובייקט, משתנים.
# מתודות: פונקציות המוגדרות עבור סוג זה של אובייקט ומופעלות עליו. המתודות עובדות עם המידע, משתנים.
# דוגמא: מחלקה (class): רכב (car). אובייקט (object): הרכב שלי.
# כל מחלקה יש: פעולות/פונקציות/מתודות, ומאפיינים/משתנים.
from Project.NewFile import File
from random import randint

"""class Person:
    def details(self):
        print("name:",self.name,"\n age:",self.age,"\n how many kids:",self.kids)
    def hasChildren(self):
        if self.kids==0:
            return True
        else:
            return False
    def ageGroup(self):
        if self.age>=0 and self.age<=18:
            return "Child"
        elif self.age>=19 and self.age<=60:
            return "Adult"
        elif self.age>=61 and self.age<=120:
            return "Senior"""""


class Circle:
    def area(self, pi=3.14):
        return pi * (self.radios ** 2)

    def circumference(self, pi=3.14):
        return 2 * pi * self.radios


class HardDisk:
    def __init__(self, size=100):  # constructor. מתודה שפועלת אוטומטית בעת יצירת האובייקט
        self.size = size
        self.usedspace = 0
        self.files = []

    def __str__(self):
        return f"Hard Disk size: {self.size}, Used space: {self.usedspace}, Free space: {self.freespace()}, files: {self.files}"

    def freespace(self):
        return self.size - self.usedspace

    def addfile(self, file):
        if self.freespace() < file.size:
            print("Not enough space")
            return False
        if file in self.files:
            print("File already exists")
            return False
        self.files.append(file)
        self.usedspace += file.size

    def delfile(self, filename):
        file = File(filename, 0)
        if file in self.files:
            i = self.files.index(file)
            self.usedspace -= self.files[i].size
            self.files.remove(self.files[i])


# אובייקטים תרגיל 2. סעיף 2.
class Loto:
    def get_random_numbers(self):
        self.random_numbers = []
        for i in range(6):
            self.random_numbers += [randint(1, 45)]

    def get_max(self):
        self.maxwin = int(input("enter the max win: "))

    def __init__(self):
        self.get_random_numbers()
        self.get_max()

    def check(self, number):
        if number in self.random_numbers:
            return True
        else:
            return False

    def wincheck(self, right_guesses):
        if right_guesses <= 1:
            self.win_sum = 0
        if right_guesses >= 2 and right_guesses <= 5:
            self.win_sum = (right_guesses * self.maxwin) / 6
        if right_guesses == 6:
            self.win_sum = self.maxwin
        return self.win_sum


# Python Exercises – Objects 3:
class Person:
    def __init__(self):
        self.name = input("enter a name: ")
        self.p_id = int(input("enter an id: "))
        self.age = int(input("enter age: "))

    def __str__(self):
        return f"name: {self.name}, id: {self.p_id}, age: {self.age}"

    def __eq__(self, other):
        if self.p_id == other.p_id:
            return True
        else:
            return False


class Bus:
    def __init__(self):
        self.seats = []
        for i in range(int(input("how many seats the bus have: "))):
            self.seats += [None]

    def display(self):
        for i in self.seats:
            print(i)

    def getOn(self, person):
        for i in range(len(self.seats)):
            if self.seats[i] is None:
                self.seats[i] = person
                break
            if i == len(self.seats) - 1:
                print(f"Sorry, the bus is full. {person.name} didnt get on the bus.")

    def getOff(self, personname):
        for i in range(len(self.seats)):
            if self.seats[i].name == personname:
                self.seats[i] = None
                break
            if i == len(self.seats) - 1:
                print(f"Sorry, Person {personname} is not on that bus.")


# Python Exercises – Objects 2: תרגיל קורס
# 1. ליצור תלמיד
class Student:
    def __init__(self, subs):
        self.s_id = int(input("enter id: "))
        if self.s_id == 0:
            return
        self.name = input("enter name: ")
        self.grades = {}
        k = []
        for i in subs:
            k += [i]
        for i in range(len(k)):
            self.grades[k[i]] = int(input(f"grade for {k[i]}: "))

    def add_grade(self, name, sub, grade):
        self.grades[sub] = grade

    def __repr__(self):
        return f"id: {self.s_id}, name: {self.name}, grades: {self.grades}||"

    def calc_factor(self, name, sub, precent):
        self.grades[sub] += (self.grades[sub] * precent) / 100
        if self.grades[sub] > 100:
            self.grades[sub] = 100

    def average(self):
        s = 0
        for i in self.grades.values():
            s += i
        return s / len(self.grades.values())


# 2. ליצור קורס
class Course:
    def __init__(self):
        self.coursenum = int(input("course number: "))
        self.coursename = input("course name: ")
        self.subs = {}
        for i in range(int(input("how many subs there is: "))):
            self.subs[input("sub name: ")] = input("teacher name: ")
        self.students = []
        self.maxstudents = int(input("max course students: "))

    def __str__(self):
        return f"course number: {self.coursenum}, course name: {self.coursename}, subs : teachers : {self.subs}, \
        \n students: {self.students}, max course students:{self.maxstudents}"

    def add_student(self, student):
        if len(self.students) == self.maxstudents:
            return False
        else:
            self.students += [student]
            return True

    def add_factor(self, sub, factor):
        for i in self.students:
            i.calc_factor(i.name, sub, factor)

    def del_student(self, id):
        for i in range(len(self.students)):
            if self.students[i].s_id == id:
                return self.students.pop(i)

    def calc_avg(self):
        for i in self.students:
            s = 0
            s += i.average()
        return s / len(self.students)
