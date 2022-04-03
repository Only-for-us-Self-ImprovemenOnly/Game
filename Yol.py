import Oyun

def YolUzeri():
    print("Vadiye Hoş Geldin..")
    print("Dikkatli Ol Yol Üstünde Gizli Düşmanların Var")
    print("Bir Yolcuya Denk Geldin...")
    print("Yolcu :: Hikayesi .......")
    #2 Yol Olucak Savas Ve Menüye Don Savası = 1' e  Menuye Donu 2' ye  aldım..
    while 1 :
        print("Savasmak İçin 1 'e Geri Dönnmek için 2 ' ye bas ")
        secim = int(input("Seçimin : "))
        if secim == 1 :
            print("Burada Savas Alanına Gidicek")
        elif secim == 2 :
            Oyun.OyunBaslama()
            break
        else :
            print("Yanlıs Tuslama Yaptın")
            print("Tekrar Dene ")

