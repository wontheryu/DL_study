

import random
import tkinter as tk


def generate_number():
    n = random.randint(1, 5)
    abcdef = random.randint(0, 999999)
    result = f"{n}조 {abcdef:06d}"
    result_var.set(result)


root = tk.Tk()
root.title("연금복권 번호 생성기")
root.geometry("300x150")

result_var = tk.StringVar()
result_var.set("버튼을 눌러 번호 생성")

label = tk.Label(root, textvariable=result_var, font=("Arial", 18))
label.pack(pady=20)

button = tk.Button(root, text="번호 생성", command=generate_number, font=("Arial", 12))
button.pack()

root.mainloop()