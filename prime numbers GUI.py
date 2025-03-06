import tkinter as tk
from tkinter import messagebox

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes():
    try:
        n = int(entry.get())
        if n < 2:
            messagebox.showerror("Error", "กรุณาใส่ค่าที่มากกว่าหรือเท่ากับ 2")
            return
        
        primes = [str(num) for num in range(2, n + 1) if is_prime(num)]
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, " ".join(primes))
    except ValueError:
        messagebox.showerror("Error", "กรุณาใส่ตัวเลขที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมหาจำนวนเฉพาะ")
root.geometry("400x300")

# สร้าง Label และ Entry
label = tk.Label(root, text="ใส่ค่าตัวเลขสูงสุด: ")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# ปุ่มกด
button = tk.Button(root, text="หาจำนวนเฉพาะ", command=find_primes)
button.pack(pady=10)

# กล่องแสดงผลลัพธ์
result_text = tk.Text(root, height=10, width=40)
result_text.pack(pady=5)

# เรียกใช้งาน Tkinter mainloop
root.mainloop()
