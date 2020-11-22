from random import randint
# t=(1,2,3)
# t2=10, 20, 30
# print(t2)
# print(t[1],",", t2[2])
# t+=4,5,6
# print(t)
# t+=7,
# print(t)
# a,b=5,6
# print(a,b)
# a,b=b,a
# print(a,b)
# for i in t:
#     print(i)
# d = {1:10,2:20,3:30,4:40,4:400}
# print(d)
# print(d[2])
# d[2] = 3813
# print(d[2])
# d[90]="why"
# print(d)
# d.update({6:22, "die":2})
# print(d)
# print(d.items())
# for i in d.items():
#     if i[1] == "why":
#         print(i[0])

#         Python Exercises - Tuples:
#         #1. ליצור טאפל שמכיל חמישה מספרים, לקלוט מספר ולבדוק כמה פעמים הוא קיים.
"""t=(1,2,3,4,5,4,2,3,6,3,1,3,5,23,2)
count=0
n = int(input("put a number: "))
for i in t:
    if i == n:
        count+=1
print(f"the num exists {count} times")"""
#2. ליצור טאפל שמכיל 3 מספרים, פרק אותם לשלושה ערכים שונים
"""t=()
for i in range(3):
    n= int(input("put a number: "))
    t+=(n,)
a,d,i=t
print(a,d,i)"""
#3. ליצור טאפל של חמש אותיות ולהפוך אותם לסטרינג
"""t=()
for i in range(5):
    n= input("put a letter: ")
    t+=(n,)
print("".join(t))"""
#4. ליצור רשימה של 10 מספרים רנדומליים בין 1-100 ולהפוך את הליסט לטאפל
"""l=[]
for i in range(10):
    l+=[randint(1,101)]
l=tuple(l)
print(l)
#5. על אותו הטאפל מסעיף 4 קבל מספר וצרף אותו לטאפל
n=int(input("enter a num: "))
l+=(n,)
print(l)
#6. ממשיך על 4, ליצור טאפל חדש מה4 אלמנטים הראשונים וה4 האחרונים
t=()
t = l[:4] + l[7:]
print(t)"""
#7. לעשות תוכנה שמוחקת תא מטאפל
"""t=()
n=int(input("enter how much numbers u want: "))
for i in range(n):
    n= int(input("put a number: "))
    t+=(n,)
print(t)
t=list(t)
n=int(input("enter what u want to remove: "))
if n in t:
    t.remove(n)
    print("removed!")
else:
    while n not in t:
        print("i dont have it here.")
        n=int(input("enter what u want to remove: "))
        if n in t:
            t.remove(n)
            print("removed!")
t=tuple(t)
print(t)
print(type(t))"""
#Python Exercises - Dictionaries:
#1. סתם לחבר dics
"""dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)"""
#2. לבדוק אם key שניתן כבר קיים
"""d={}
for i in range(int(input("how much keys you want: "))):
    k=input("enter key: ")
    v=input("enter value: ")
    d2={k:v}
    d.update(d2)
n=input("\n what key you want to check?: ")
k=""
for i in d:
    if n == i:
        print("this key already exists")
        k=i
        break
if k!=n:
    print("key not  exists")"""
#3. לקלוט מספר שמ1 עד המספר הזה זה יעשה dics של המפתח:הריבוע שלו
"""n=int(input("how much keys you want: "))
d={}
for i in range(n):
    d2={i+1:(i+1)**2}
    d.update(d2)
print(d)"""
#4. לחשב את סכום הערכים בdics
"""d={}
sum=0
for i in range(int(input("how much keys you want: "))):
    k=input("enter key: ")
    v=input("enter value: ")
    d[k]=v
for j in d:
    sum += int(d[j])
print("sum of values is: ", sum)"""
#5.להכפיל ב2 את כל הערכים
"""d={}
sum=0
for i in range(int(input("how much keys you want: "))):
    k=input("enter key: ")
    v=input("enter value: ")
    d[k]=v
print(d)
for j in d:
    d[j] = int(d[j])*2
print(d)"""
#6. מקבל מפתח ומוחק אותו מהדיק
"""d={}
for i in range(int(input("how much keys you want: "))):
    k=input("enter key: ")
    v=input("enter value: ")
    d[k]=v
print(d)
delete = input("what key you want to delete: ")
for j in d:
    if j == delete:
        del d[j]
        break
print(d)"""
#7. ליצור ליסט של 5 שמות ואחת של 5 ציונים, להפוך אותם לdic.
"""names = ["a","b","c","d","e"]
grades = [70,80,90,50,60]
d={}
for i in range(5):
    d[names[i]] = grades[i]
print(d)"""
#8. לקבל את הערך מקסימום והמינימום בכל דיק
"""d={}
for i in range(int(input("how much keys you want: "))):
    k=input("enter key: ")
    v=input("enter value: ")
    if i == 0:
        max = v
        min = v
    d[k]=v
for j in d:
    if d[j] < min:
        min = d[j]
    if d[j] > max:
        max = d[j]
print("min is: ", min)
print("max is: ", max)"""
#9. למחוק ערכים כפולים, לא גמור!!!!!
"""d={}
for i in range(int(input("how much keys you want: "))):
    k=input("enter key: ")
    v=input("enter value: ")
    d[k] = v
v = d.values()
v=list(v)
for j in v:
    v.remove(j)
    if j in v:
        del d[j]
print(d)"""

