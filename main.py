import os
import tkinter as tk
from tkinter import filedialog, messagebox

def dosya_sec():
    klasor = filedialog.askdirectory()
    if klasor:
        klasor_entry.delete(0, tk.END)
        klasor_entry.insert(tk.END, klasor)

def dosya_uzanti_degistir():
    klasor = klasor_entry.get()
    eski_uzanti = eski_uzanti_entry.get()
    yeni_uzanti = yeni_uzanti_entry.get()

    if not os.path.isdir(klasor):
        messagebox.showerror("Hata", "Geçersiz klasör!")
        return

    cevap = messagebox.askquestion("Onay", f"{klasor} klasöründeki .{eski_uzanti} dosyalarını .{yeni_uzanti} olarak değiştirmek istiyor musunuz?")
    if cevap == "yes":
        for dosya in os.listdir(klasor):
            if dosya.endswith(f".{eski_uzanti}"):
                dosya_yolu = os.path.join(klasor, dosya)
                yeni_dosya_adi = dosya[:-(len(eski_uzanti))] + yeni_uzanti
                yeni_dosya_yolu = os.path.join(klasor, yeni_dosya_adi)
                os.rename(dosya_yolu, yeni_dosya_yolu)
        messagebox.showinfo("Bilgi", "Dosya uzantıları başarıyla değiştirildi.")

# Kullanıcı arayüzü oluşturma
pencere = tk.Tk()
pencere.title("Dosya Uzantı Değiştirme")
pencere.geometry("400x200")

klasor_label = tk.Label(pencere, text="Klasör:")
klasor_label.pack()

klasor_entry = tk.Entry(pencere, width=40)
klasor_entry.pack()

klasor_sec_button = tk.Button(pencere, text="Klasör Seç", command=dosya_sec)
klasor_sec_button.pack()

eski_uzanti_label = tk.Label(pencere, text="Eski Uzantı:")
eski_uzanti_label.pack()

eski_uzanti_entry = tk.Entry(pencere, width=10)
eski_uzanti_entry.pack()

yeni_uzanti_label = tk.Label(pencere, text="Yeni Uzantı:")
yeni_uzanti_label.pack()

yeni_uzanti_entry = tk.Entry(pencere, width=10)
yeni_uzanti_entry.pack()

degistir_button = tk.Button(pencere, text="Uzantıları Değiştir", command=dosya_uzanti_degistir)
degistir_button.pack()

pencere.mainloop()