import Oyun


def YapımcılarMenusu():
    print("\n")
    print("-----------------")
    print("Yapımcılar \nUğur Can Yıldız\nMuhammed Raşit Özgün")
    print("------------------")
    while 1 :
        print("Geri Çıkmak için b tuşuna basınız.")
        print("Programı Sonlandırmak İçin e tuşuna basınız.")
        cevap = input("Seciminiz : ")
        cevap = cevap.upper()
        if cevap == 'B':
            print("Menüye Yönlendiriliyosunuz...")
            Oyun.OyunMenusu()
            break
        elif cevap == 'E':
            print("Programdan Çıkılıyor..")
            exit()
        else :
            print("Yanlış Tuşlama Yaptınız")
            print("Tekrar Deneme Yapınız")
