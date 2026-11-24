import tkinter as tk

# Fungsi saat tombol ditekan
def klik(angka):
    layar.insert(tk.END, angka)

# Fungsi menghitung hasil
def hitung():
    try:
        hasil = eval(layar.get())
        layar.delete(0, tk.END)
        layar.insert(0, str(hasil))
    except:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")

# Fungsi clear
def clear():
    layar.delete(0, tk.END)

# Membuat window
root = tk.Tk()
root.title("Kalkulator racing")
root.geometry("300x400")

# Entry (layar)
layar = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
layar.pack(fill="both", ipadx=8, pady=10, padx=10)

# Frame tombol
frame = tk.Frame(root)
frame.pack()

# Tombol angka dan operator
tombol = [
    ('7', '8', '9', '+'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '*'),
    ('0', 'C', '=', '/')
]

for baris in tombol:
    f = tk.Frame(frame)
    f.pack()
    for t in baris:
        if t == "=":
            btn = tk.Button(f, text=t, width=5, height=2, font=("Arial", 18), command=hitung)
        elif t == "C":
            btn = tk.Button(f, text=t, width=5, height=2, font=("Arial", 18), command=clear)
        else:
            btn = tk.Button(f, text=t, width=5, height=2, font=("Arial", 18),
                            command=lambda x=t: klik(x))
        btn.pack(side="left", padx=5, pady=5)

root.mainloop()