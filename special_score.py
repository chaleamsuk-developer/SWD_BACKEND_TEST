"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ

"""

"โปรแกรมการตัดตัวแรกของคำเพื่อนำมาต่อกัน"
text = str(input("Enter a string\n"))
text = text.split()
acronym = ""
for i in text:
    acronym = acronym+str(i[0]).upper()
print(acronym)

"โปรแกรมการสุ่มสร้างรหัสผ่านจากจำนวนที่ user กำหนด"
import random
passlen = int(input("Enter the length of password : "))
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen))
print("Random Password : ",p)