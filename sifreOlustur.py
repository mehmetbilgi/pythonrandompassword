#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Dışarıya da verilebilecek şifre üretimi
"""

import random
dizi = []

# -----------------------------------------------------------------------------
# Şifre üretimi harici olarak istenecek ise debug = False kalacak ve ekranda
# çıktı olmayacak.
def sifreUret(p1, debug = False):
    sifre = ""
    try:
        sifreUzunlugu = int(p1)
    except ValueError:
        return False
# -----------------------------------------------------------------------------
    # Şifre üretilecek karakter dizisinin oluşturulması
    # Özel karakterler
    # d dizisine başka karakterler de ilave edilebilir.
    d = ["Ğ", "ğ", "İ", "ı", "Ü", "ü", "Ş", "ş", "Ö", "ö", "Ç", "ç"]
    for i in d:
        i = str(i)
        dizi.append(unicode(i, "utf-8"))
        # 0 - 9 arası sayılar
        for i in range(ord('0'), ord('9') + 1):
            dizi.append(chr(i))
        # a - z arası harfler
        for i in range(ord('a'), ord('z') + 1):
            dizi.append(chr(i))
        # A - Z arası sayılar
        for i in range(ord('A'), ord('Z') + 1):
            dizi.append(chr(i))
    # -----------------------------------------------------------------------------
    # Şifre oluşturulacak dizi, debug değişkeni True ise yazdırılıyor
    if(debug == True):
        j = 0
        print("*" * 50)
        for i in dizi:
            if (j >= 10):
                print("\n")
                j = 0
            print(i),
            j += 1
        print("\n")
        print("*" * 50)
    # -----------------------------------------------------------------------------
    # Girilen uzunluk kadar şifre üretiliyor
    for i in range(sifreUzunlugu):
        sifre += random.choice(dizi)
    return sifre

# -----------------------------------------------------------------------------
# Modül olarak çağırılmamışsa alttakiler çalışacak
if __name__ == "__main__":
# -----------------------------------------------------------------------------
    girUzunluk = unicode(raw_input("Şifre uzunluğu :: "), "utf-8")
    sif = sifreUret(girUzunluk, debug = True)
    if(sif == False):
        print("Şifre uzunluğu rakam olmalı...\n")
    else:
        print(u"\n%s haneli üretilen şifre :: %s\n" % (girUzunluk, sif))
        print("*" * 50)

        # Oluşturulan şifre kontrol ediliyor
        girSifre = unicode(raw_input("Şifreyi girin :: "), "utf-8")
        if (girSifre == sif):
            print(u"Girilen şifre doğru...\n")
        else:
            print(u"Şifre hatalı...\n")
# -----------------------------------------------------------------------------