#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Mehmet Bilgi
# 45/2017
# GNU/GPLv3
# https://www.gnu.org/licenses/gpl-3.0.en.html


# Ana proje:
# Kendi başına çalışabilen şifre oluşturma modülünü
# buraya ekledik.
# sifreUret(sifreUzunlugu)
# fonksiyonu ile ilgili modülden istenilen uzunlukta
# şifremizi alıp gui içerisinde kullanıyoruz.


from Tkinter import *
from sifreOlustur import *
import sys

#------------------------------------------------------------------------------
def sifreOlustur(event = None):
    sifreUzunlugu = girisKutusu3.get()
    try:
        int(sifreUzunlugu)
        s = sifreUret(sifreUzunlugu) #eklenen harici moduldeki şifre üretme fonksiyonu
        etiket4.config(text = s,
                       fg = "black",
                       font = "bold"
                       )
    except ValueError:
        etiket4.config(text = "Şifre uzunluğu rakam olmalı!",
                       fg = "blue",
                       font = "bold"
                       )
    girisKutusu3.delete(0, END)

#------------------------------------------------------------------------------
pencere1 = Tk()
pencere1.resizable(width = True, height = False)
pencere1.geometry("400x130-500+100")
baslik1 = pencere1.title("Şifre üretme")
#pencere1.overrideredirect(True)
pencere1.config(bg = "gray25")

pencere1.bind("<Return>", sifreOlustur)
pencere1.bind("<KP_Enter>", sifreOlustur)
pencere1.bind("<Escape>", sys.exit)

etiket1 = Label(pencere1,
                text = "Şifre Uzunluğunu giriniz.",
                font = "bold"
                )

girisKutusu3 = Entry(pencere1)
girisKutusu3.focus_set()

buton5 = Button(pencere1,
                text = "Sifre olustur",
                command = sifreOlustur,
                font = "bold"
                )

etiket4 = Label(pencere1)

buton1 = Button(pencere1,
                text = "Çıkış",
                command = pencere1.destroy, #çıkış
                font = "bold"
                )

etiket1.pack()
girisKutusu3.pack()
buton5.pack()
etiket4.pack()
buton1.pack()
pencere1.mainloop()
#------------------------------------------------------------------------------