import random
def hangmann(letter,word,mistakes, theguess, saving): #פונקציה שאמורה לעשות את הבדיקה והוספה עד שאתה מצליח לגלות את כל האות, לספור טעויות וכו'
    if letter in word: #אם האות בתוך המילה
        saving = theguess
        theguess = ""
        for i in range(len(word)): #תרוץ על האינדקסים של המילה עצמה
            if letter == word[i]: #אם האות היא אותה אות כמו האות שבאינדקס
                theguess += word[i] #הניחוש מקבל את האות
            else: #אם זה לא האות
                theguess += saving[i] #הוא יקבל את השמירה במקום הi שזה או אות או "_"
    else:
        mistakes +=1
        print(f"a mistake. mistakes = {mistakes}")
        if mistakes == 10:
            return "False",mistakes
    return theguess, mistakes
l = ["microsoft", "word", "something", "hello","conterstrike"] #מאגר מילים
word=random.choice(l) # המילה הרנדומלית שהמשתמש צריך לנחש
saving ="" # משתנה לשמירת words ולקבלת ההתחלה של _
mistakes = 0 #כמות השגיאות
for i in word: # הבנייה הראשונה של המילה עם קו תחתון
    saving += "_"
print(saving)
letter = input("guess a letter: ") # האות אותה המשתמש ניחש
theprint = "" # מה שהמשתמש רואה כשמדפיסים
if letter in word:
    for i in word:
        if letter == i:
            theprint += letter
        else:
            theprint += "_"
else:
    theprint = saving
    mistakes+=1
    print(f"srry, a mistake. mistakes = {mistakes}")
print(theprint)
saving = theprint
while word != theprint:
    letter = input("put another letter: ")
    theprint,mistakes = hangmann(letter , word , mistakes , theprint , saving)
    if theprint == "False":
        print("K.O. U DEAD.")
        print("the word was :", word)
        break
    print(theprint)
if word == theprint:
    print("wow dude! u made it! u WON!")