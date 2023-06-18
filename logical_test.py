
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

def ThaiBaht(txt):
    bahtTxt, n, bahtTH = "", "", ""
    try:
        amount = float(txt)
    except:
        amount = 0.00
    try:
        df = "{:.2f}".format(amount)
        bahtTxt = df
        num = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ"]
        rank = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        temp = bahtTxt.split(".")
        intVal = temp[0]
        decVal = temp[1]
        if float(bahtTxt) == 0:
            bahtTH = "ศูนย์บาทถ้วน"
        else:
            for i in range(len(intVal)):
                n = intVal[i]
                if n != "0":
                    if (i == (len(intVal) - 1)) and (n == "1"):
                        bahtTH += "เอ็ด"
                    elif (i == (len(intVal) - 2)) and (n == "2"):
                        bahtTH += "ยี่"
                    elif (i == (len(intVal) - 2)) and (n == "1"):
                        bahtTH += ""
                    else:
                        bahtTH += num[int(n)]
                    bahtTH += rank[(len(intVal) - i) - 1]
            bahtTH += "บาท"
            if decVal == "00":
                bahtTH += "ถ้วน"
            else:
                for i in range(len(decVal)):
                    n = decVal[i]
                    if n != "0":
                        if (i == len(decVal) - 1) and (n == "1"):
                            bahtTH += "เอ็ด"
                        elif (i == (len(decVal) - 2)) and (n == "2"):
                            bahtTH += "ยี่"
                        else:
                            bahtTH += num[int(n)]
                        bahtTH += rank[(len(decVal) - i) - 1]
                bahtTH += "สตางค์"
    except:
        pass
    return bahtTH
number = str(input("Enter a value : "))    
print("Convert Number : ",number," to Thai Text : ", ThaiBaht(number)) 