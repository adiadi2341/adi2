#בפייתון כל דבר הוא אובייקט: משתנים, פונקציות, קבצים.
#לכל סוג של אובייקט יש: מידע (attributes): מידע של האובייקט, משתנים.
#מתודות: פונקציות המוגדרות עבור סוג זה של אובייקט ומופעלות עליו. המתודות עובדות עם המידע, משתנים.
#דוגמא: מחלקה (class): רכב (car). אובייקט (object): הרכב שלי.
#כל מחלקה יש: פעולות/פונקציות/מתודות, ומאפיינים/משתנים.
class Person:
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
            return "Senior"
class Circle:
    def area(self,pi=3.14):
        return pi*(self.radios**2)
    def circumference(self,pi=3.14):
        return 2*pi*self.radios