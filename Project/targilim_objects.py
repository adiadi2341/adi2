from Project.Objects_learn import Person #אפשר להוסיף "as" ואז עוד משהו לדוגמא: "as R" ואז הקלאס תהייה R במקום Person.
from Project.Objects_learn import Circle
from Project.Objects_learn import HardDisk as H
from Project.NewFile import * #מביא את הכל
from Project.Objects_learn import Loto
from Project.Objects_learn import Bus
from Project.Objects_learn import Student
from Project.Objects_learn import Course
#Python Exercises – Objects 1:
#1. ליצור איש:
"""p = Person()
p.name = "Sagi"
p.age = 13
p.kids = 7
p.details()
print("have kids? ", p.hasChildren())
print("hes age group is: ", p.ageGroup())"""
#2. ליצור עיגול:
"""c = Circle()
c.radios = int(input("Radios: "))
print(c.area())
print(c.circumference())"""
#5. ליצור הארדיסק
"""hd = H()
hd.size=100
hd.usedspace = 0
hd.files = 0
for i in range(5):
    size = int(input("enter file size: "))
    hd.addfile(size)
hd.showdetails()
size = int(input("enter file size for delete: "))
hd.delfile(size)
hd.showdetails()"""
#תרגיל למידה חדש עם שינויים של קלאס ההארדיסק
"""file1=File("aa",30)
file2=File("bbb",40)
file3=File("aa", 50)
print(file1)
print(file2)
hd = H(200)
print(hd)
hd.addfile(file1)
print(hd)
hd.addfile(file2)
print(hd)
hd.addfile(file3)
print(hd)
print(file3>file1)
print(file3<file1)
hd.delfile(file1.name)
print(hd)"""

#Python Exercises – Objects 2:
# תרגיל 2. הגרלות לוטו
"""a = Loto()
rightguess = 0
print(a.random_numbers)
for i in range(6):
    n = int(input("enter a guess: "))
    if n >= 1 or n <= 45:
        if a.check(n):
            rightguess+=1
            n=2
    else:
        print("sorry, not available number")
        break
if n < 1 or n > 45:
    print("win: 0")
else:
    print(a.wincheck(rightguess))""" #שאלו מה יכול להשתבש, אם אני בודק 6 פעמים את אותו המספר זה עושה שצדקתי 6 פעמים.

#Python Exercises – Objects 3:
"""a = Bus()
action = int(input("what u want to do? 1 for get on, 2 for get off, 0 for end: "))
while action !=0:
    if action == 1:
        a.getOn(Person())
    if action == 2:
        a.getOff(input("enter the name of the person that you want to remove: "))
    action = int(input("what u want to do? 1 for get on, 2 for get off, 0 for end: "))
a.display()"""

#Python Exercises – Objects 2: תרגיל קורס
c = Course()
while True:
    s = Student(c.subs)
    if s.s_id == 0:
        break
    if c.add_student(s) == False:
        print(f"{s.name} has not get in.")
        break

c.add_factor(input("enter factor sub: "), int(input("enter the factor: ")))
avaraged={}
for i in c.students:
    avaraged[i.s_id] = i.average()
ids = []
mingrade = 100
for i in avaraged:
    if avaraged[i] <mingrade:
        mingrade = avaraged[i]
        ids = [i]
    elif avaraged[i] == mingrade:
        ids += [i]
print(c)
for i in range(len(ids)):
    print(c.del_student(ids[i]), "was removed from course because he sucks.")
print(c)