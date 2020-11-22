import random
from random import shuffle
from random import randint
"""r = random.randint(1,100)
print(r)
min = 1
max = 100
text = input("H (higher) / L (lower) / S (success)? \n")
while text != "S":
    if text == "H":
        min = r
        r = random.randint(r,max)
        print(r)
        text = input("H (higher) / L (lower) / S (success)? \n")
    elif text == "L":
        max = r
        r = random.randint(min,r)
        print(r)
        text = input("H (higher) / L (lower) / S (success)? \n")
print("NOICE")"""
"""תרגילים מחרוזת 10.11.20 1.
word =input("something: \n")
newword=""
for i in word:
    if i != "a" or i != "A":
        newword = newword + i
print(newword)
פיתרון שני:
name = input("enter name: ")
name = name.replace("A","")
name = name.replace("a","")
print(name)"""

"""2.
username = input("username: \n")
password = ""
for i in range(6):
    password = password + random.choice(username)
print(password)"""

"""3. עדיין לא עובד!!!
w1 = input("enter something: ")
w2 = input("enter other something: ")
k=0
for i in w1:
    if w2.find(i) != -1:
        k1 = w1.count(i)
        k2 = w2.count(i)
        if k1 != 1:
            k = k-1
        k = k + 1
print(k)"""

"""תרגיל 2.3 מהמצגת בעמוד
all = input("write street house nm and town: \n")
all=all.replace(" ", "\n")
print(all)"""
"""street = ""
nm = ""
l = all.split()
for i in l:
    street += i
print(street)"""
#מהקישורים שהיא שמה בכיתת גוגל
#1. שלוש מספרים אמצעיים
"""w = input("put something: ")
length = 0
for i in w:
    length+=1
if length<7 or length%2==0:
    print("not good for u")
else:
    print(w[(length//2)-1:(length//2)+2])"""
#2. לשים סטרינג אחד באמצע סטרינג אחר
"""w = input("put something: ")
middle = input("the thing that will be middle: ")
new=""
for i in range(len(w)):
    if i == len(w)//2:
        new+=middle[0:len(middle)]
    new+=w[i]
print(new)"""
#עוד דרך לעשות את 2.
"""w = input("put something: ")
w2 = input("the thing that will be middle: ")
middle = len(w)//2
left = w[:middle]
right = w[middle:]
print(left+w2+right)"""
#3. אות ראשונה אמצעית ואחרונה משני סטרינגים אחד אחרי השני
"""w = input("put something: ")
w2 = input("the thing that will be middle: ")
middle1 = w[len(w)//2]
middle2 = w2[len(w2)//2]
print(w[0]+w2[0]+middle1+middle2+w[len(w)-1]+w2[len(w2)-1])"""
#4. לסדר סטרינג עם אותיות קטנות קודם
"""w = input("put something: ")
ordered = ""
for i in w:
    if ord(i) >= 97 and ord(i) <= 122:
        ordered += i
for i in w:
    if ord(i) >= 65 and ord(i) <= 90:
        ordered+= i
print(ordered)"""
#5. לספור את כל הכמויות אותיות, ספרות, וסמלים בשורה
"""w = input("put something: ")
chars = 0
digits = 0
symbol = 0
for i in w:
    if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
        chars+=1
    elif ord(i) >= 48 and ord(i) <= 57:
        digits+=1
    else:
        symbol+=1
        if i == " ":
            symbol-=1
print(f"chars = {chars}\n digits = {digits}\n symbols = {symbol}")"""
#7. בדיקה האם סטרינג 1 בתוך סטרינג 2
"""w = input("put something: ")
w2 = input("put another something: ")
a=""
for i in w:
    if i in w2:
        continue
    else:
        a= "False"
        print(a)
if a!="False":
    print("True")"""
"""l=[1,2,3,4,5]
print(l.pop())""" #פופ היא פונקציה אשר מחזירה את הערך של התא אותו היא מחקה. (בוחרים לה אינדקס/מיקום של תא, והיא מוחקת אותו, אם לא בחרת כלום - מוחקת את התא האחרון.)
#מבנה ליצירת ליסט רנדומלי בשורה אחת:
#list = [i for i in range(10)]
#לפני הלולאה אומרים איזה ערך רוצים שישב בתוך הליסט, ובסוף אומרים איזו אורך רוצים את הרשימה
