#תרגילים פונקציות
#10.1 להגדיר פונקציה שמקבלת שלושה מספרים ומחזירה את המקסימום
"""def maxnum(n1,n2,n3):
    l=[n1,n2,n3]
    return max(l)
print(maxnum(6,141,-259))"""
#10.2 מקבלת ליסט ומחזירה את הסכום של כל הערכים
"""def sumnum(list1):
    return sum(list1)
l = [8,2,3,0,7]
print(sumnum(l))"""
#10.3. לקבל רשימה של ערכים, ולהכפיל בינהם
"""def kaful(list1):
    tozaa = 1
    for i in list1:
        tozaa = tozaa*i
    return tozaa
l = [7,-1,3,2,8]
print(kaful(l))"""
#10.4 מקבלת מחרוזת, והופכת אותה
"""def backlist(string):
    string = string[::-1]
    return string
s=input("put a sentence: ")
print(backlist(s))"""
#10.5 פונקציה הבודקת אם מספר הוא בטווח ערכים. מקבלת 3 פרמטרים, True או False
"""def check(num,min,max):
    if num > min and num < max:
        return True
    else:
        return False
print(check(int(input("the num u want to check: ")),int(input("\n the minimum: ")),int(input("\n the maximum: "))))"""
#10.6 מקבלת מחרוזת ומחשבת את מספר הפעמים שיש אות גדולה ואות קטנה.
"""def check(string):
    countsmall = 0
    countbig = 0
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            countbig+=1
        if ord(i) >= 97 and ord(i) <= 122:
            countsmall+=1
    print(f"how many big letters: {countbig} , how many small letters: {countsmall}")
s=input("enter what u want: ")
check(s)"""
#10.7 מקבלת רשימה ומחזירה את אותה רשימה בלי כפילויות
"""def nodouble(list1):
    list1 = set(list1)
    list1 = list(list1)
    return list1
l = [1,2,3,3,3,3,4,5]
print(nodouble(l))"""
#10.8 מקבלת מספר בודקת אם הוא ראשוני.
"""def rishoni(num):
    for i in range(2,10):
        if num%i == 0 and num!=i:
            return False
        else:
            r = True
    return r
print(rishoni(int(input("enter a number for check if rishoni: "))))"""
#10.9 מקבלת רשימת מספרים סוכמת רק מספרים זוגיים
"""def sumzugi(list1):
    sum1=0
    for i in list1:
        if i%2==0:
            sum1+=i
    return sum1
l = [1,2,3,4,5,6,7]
print(f"the sum of zugi is: {sumzugi(l)}")"""
#10.10 מקבלת מחרוזת ובודקת אם היא פלינדרום.
"""def polindrom(string):
    s1=""
    for i in string:
        if i != " ":
            s1 += i
    string = s1[::-1]
    if s1==string:
        return True
    else:
        return False
s=input("enter word: ")
print(f"polindrom? : {polindrom(s)}")"""
#תרגילי פונקציות 3:
#1. פונקציית len
"""def length(list1):
    c = 0
    for i in list1:
        c +=1
    return c
l=[1,2,3,4,5,6,7,8,9,7,5,4,32,5,]
print(length(l))"""
#2.עושה count למספר שמבקשים בתוך רשימה
"""def countnum(list1, num):
    count=0
    for i in list1:
        if num == i:
            count+=1
    return count
l = [1,2,21,2,3,54,1,3,1,1,45,52,25]
print(countnum(l,1))"""
#3. עושה find למספר בתוך ליסט עם מיקום אופוציונלי לתחילת חיפוש
"""def findnum(list1,num,start=0):
    place = 0
    for i in range(start,len(list1)):
            if list1[i] == num:
                place = i
                return place
l = [1,2,3,4,5,6,7,8,9]
print(findnum(l,3,5))"""
#4. עושה max, מקבלת רשימה מחזירה ערך הכי גבוה
"""def maxnum(list1):
    maximum = list1[0]
    for i in list1:
        if i > maximum:
            maximum=i
    return maximum
l=1,1354,56,2,1,54,6,6,134421589275,2,56,6,36,256,35225252
print(maxnum(l))"""
#5. עושה list מקבלת ערך dic\set\str\tuple ומחזירה המרה לlist. אם dic יחזיר ליסט של הkeys. אם מתקבל משהו אחר מציג שגיאה ומחזיר None.
"""def makelist(something):
    list1=[]
    if ((type(something) == str or type(something) == set) or type(something) == dict) or type(something) == tuple:
        for i in something:
            list1 += [i]
        return list1
    return None, "error"
s="hey wassap" #נבדק על כל המשתנים, עובד.
print(makelist(s))"""
#6. עושה remove מקבלת רשימה וערך, מחפש את הערך ומחזיר את אותה רשימה (אותה כתובת) ללא הערך.
# def removenum(list1,num): #עובד אך לא אותו idת צריך לשאול את אורלי
#     list1
#     list2=[]
#     for i in range(len(list1)):
#         if list1[i] != num:
#             list2 += [list1[i]]
#     list1=list2
#     return list1
# l=[1,2,3,4,5,6,7,8]
# print(id(l))
# print(id(removenum(l,5)), removenum(l,5))
#7. תעשה keys: תקבל dic ותחזיר רשימה של הkeys.
"""def listkeys(dic):
    list1=[]
    for i in dic:
        list1+=[i]
    return list1
dic={1:30,2:20,3:40,5:40,52:30}
print(listkeys(dic))"""
#8.