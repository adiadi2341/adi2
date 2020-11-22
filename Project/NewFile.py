# __ge__ >=
# __le__ <=
# __it__ <
# __eq__ ==
# __gt__ >
# __ne__ !=
# כל המתודות האלו אלה מתודות קבועות אשר מקבלות את עצמן ומשתנה אחר (other) ומה שהן עושות זה משוות בין האובייקטים עצמם. (מה שאני מבקש מהן בפנים)
#לדוגמא, לבקש מהן שמתי שאני משווה שני אובייקטים, שישווה את האורך או את הגודל שלהם.

class File:
    def __init__(self, name, size): #constructor. מתודה שפועלת אוטומטית בעת יצירת האובייקט
        self.name=name
        self.size=size
    def __str__(self): #מתודה שמחזירה מחרוזת של צורת ההדפסה
        return f"File name: {self.name}, File size: {self.size}" #כל פעם שאני עושה פרינט לfile כלשהו, זה ידפיס את כל הפרטים שאני ביקשתי שידפיס
    def __repr__(self): #חכמה יותר מstr. מתודה חברה של str, פועלת על ליסטים. הstr פועלת רק על אלמנט ספציפי.
        return f"{self.name} : {self.size}"
    def __eq__(self, other): #מתודה שעושה השוואה בין ערכים ספציפיים של אובייקט. חייבת לקבל משהו מאותו הסוג.
        if self.name == other.name: #פועל כשאני משווה בתוך הפונקציה הראשית את האובייקט שמתודה כתובה בו.
            return True
        else:
            return False

    def __gt__(self, other): # מתודה שעושה השוואה (greater) בין מה שאני מבקש ממנו. בדיוק כמו בeq.
        if self.size > other.size:
            return True
        else:
            return False