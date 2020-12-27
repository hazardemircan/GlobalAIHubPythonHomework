import random
import time

isim=input("Lütfen isminizi giriniz: ")
print(f"Merhaba {isim}")
while (True):
    oyun = input("Yeni Oyun [E/H] :")
    if (oyun == "E"):
        print("OYUN OLUŞTURULUYOR...")
        time.sleep(2)
        
        print(""" ***ADAM ASMACA OYUNU*** 
        > KELİME TAHMİNİ İÇİN: 1
        > ÇIKIŞ İÇİN: 2""")
        
        kelime_list = ["hazar","python","aihub","anaconda"]
        gizli = random.choice(kelime_list)
        can=len(gizli)+1
        liste=list()
        sifre="_" * len(gizli)
        liste.extend(sifre)
        print(liste)
        bilinen=0
        harfler=""
        
        
        
        while (can>0):
            analiz = True
            tahmin=input("Tahmin: ")
            if len(tahmin)>1:
                print("Hatalı değer girdiniz, giriş için 1, çıkış için 2 .")
                print(liste)
            elif (tahmin==1):
                k_tahmin = input("Tahmininizi giriniz: ")
                if (k_tahmin == gizli):
                    liste.clear()
                    liste.extend(gizli)
                    print(liste)
                    print("KAZANDINIZ!!!")
                    break
                else:
                    print(">Yanlış Tahmin")
                    can-=1
                    print(f"Can:{can}")
                    print(liste)
                    if can==0:
                        print("KAYBETTİNİZ!!!")
                        break
                    continue
            elif (tahmin=="2"):
                    print("Çıkış Yapılıyor...")
                    time.sleep(2)
                    print("Çıkış Yapıldı")
                    break
            elif not(tahmin):
                    print("Lütfen harf giriniz...")
            else:
                    if tahmin in harfler:
                        print("Bu karakter girildi!")
                        print(liste)
                        continue
                    else:
                        harfler +=tahmin
                        for i in enumerate (gizli):
                            if tahmin in i[1]:
                                liste.insert(i[0], i[1])
                                liste.pop(i[0]+1)
                                bilinen+=1
                                analiz=False
                        print(liste)
                        if(bilinen == len(gizli)):
                            print("KAZANDINIZ!!!")
                            break
                        if(analiz):
                            print("Yanlış tahmin!!!")
                            can-=1
                            print(f"Can:",can)
                            if (can==0):
                                print("KAYBETTİNİZ!!!")
            
    
    elif (oyun == "H"):
        print("ÇIKIŞ YAPILIYOR...")
        break
    else:
        print("Lütfen [E/H] seçiniz")