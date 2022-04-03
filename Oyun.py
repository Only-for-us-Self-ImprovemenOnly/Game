import Oyun
import Yapimcilar
import Yol

def OyunMenusu():
        print("\n")
        print(" --> Oyun Menüsüne Gitmek İçin 's' e bas")
        print(" --> Yapımcıları Görmek İçin 'y' ye bas")
        print(" --> Programdan Çıkmak İçin 'q' ye bas")

        while 1:
            secim = input("Seciminiz : ")
            secim = secim.upper()
            if secim == 'S':
                print("Oyuna Başladınız...")
                Oyun.OyunBaslama()

            elif secim == 'Y':
                print("\n")
                Yapimcilar.YapımcılarMenusu()
                break

            elif secim == 'Q':
                print("Programdan Çıkılıyor..")
                exit()

            else:
                print("Yanlış Tuşlama Yaptınız.")


def OyunBaslama():
    print("*Oyuna Hoşgeldin*")
    print("Karakter Seçmen Gerekicek (Dikkatli Seç)")
    print("\n")
    print("Herolar")
    print("--------------")
    print("1-) Samuray, Str : 5 , Agl : 4 , Hlt : 2")
    print("2-) Okçu   , Str : 7 , Agl : 2 , Hlt : 1")
    print("3-) Ucube  , Str : 5 , Agl : 4 , Hlt : 2")
    print("--> Menu Gitmek İçin '0' Rakamına Bas")

    while 1 :
        secim = int(input("Seçimini yap (1,2,3,0) : "))
        if secim == 1 :
            print("Samuray Hikayesi.......")
            Yol.YolUzeri()
            break
        elif secim == 2 :
            print("Okçu Hikayesi..........")
            Yol.YolUzeri()
            break
        elif secim == 3 :
            print("Ucube Hikayesi..........")
            Yol.YolUzeri()
            break
        elif secim == 0  :
            print("Menuye Donuluyor..")
            Oyun.OyunMenusu()
            break
        else :
            print("Yanlış Tuşlama Yaptın ! ")
            print("Tekrar Dene : ")
