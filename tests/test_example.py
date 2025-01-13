import unittest

# הפונקציה לה נרצה לכתוב test
def add(a, b):
    return a + b

# יצירת מחלקת test
class TestMathOperations(unittest.TestCase):

    # בדיקת פונקציית add
    def test_add(self):
        self.assertEqual(add(2, 3), 5)    # בדיקה שהפונקציה מחזירה את התוצאה הנכונה
        self.assertEqual(add(-1, 1), 0)   # בדיקה עם מספרים שליליים
        self.assertEqual(add(0, 0), 0)    # בדיקה עם אפס
        self.assertEqual(add(-2, -3), -5) # בדיקה עם שני מספרים שליליים

# הרצת הבדיקות
if __name__ == '__main__':
    unittest.main()
