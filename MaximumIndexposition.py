
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

marks = [1,2,1,3,5,6,4]

# Using for loop
maximum_val= marks[0]
for i in range(1, len(marks)): 
    print(marks[i]," > ",maximum_val)
    if (marks[i] > maximum_val):
        maximum_val = marks[i]
print("Maximum Index position: ",marks.index(maximum_val))
