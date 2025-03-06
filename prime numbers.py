n = 20  # กำหนดค่าตัวเลขสูงสุดที่ต้องการหาจำนวนเฉพาะ

for num in range(2, n+1):  # วนลูปตั้งแต่ 2 ถึง n (รวม n)
    is_prime = True  # ตั้งค่าเริ่มต้นให้ num เป็นจำนวนเฉพาะ
    
    for i in range(2, int(num ** 0.5) + 1):  # ตรวจสอบตัวหารเฉพาะค่าถึง sqrt(num)
        if num % i == 0:  # ถ้า num หาร i ลงตัว แสดงว่า num ไม่ใช่จำนวนเฉพาะ
            is_prime = False  # กำหนดค่าเป็น False เพื่อบอกว่าไม่ใช่จำนวนเฉพาะ
            break  # ออกจากลูปทันทีเมื่อพบว่ามีตัวหาร
    
    if is_prime:  # ถ้า is_prime ยังเป็น True แสดงว่า num เป็นจำนวนเฉพาะ
        print(num, end=' ')  # พิมพ์ค่าของ num ออกมาโดยคั่นด้วยช่องว่าง