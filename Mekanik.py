def Iskelet(hasar , ceviklik , can):
    damage = 2.0
    agility = 1.0
    health = 10
    while 1 :
        print("----------------------")
        print("İskeletin {} canı var..." .format(health))
        print("İskelet Sana Vurmaya Hazırlanıyor..")
        can = can - damage
        print("{} canın kaldı ..".format(can))
        print("Iskeletin Canı : {}" .format(health))
        print("Heronun Canı : {}" .format(can))
        print(" Sen vuruyorsun...")
        health = health - hasar

        if health == 0 :
            print("Tebrikler Canavarı Öldürdün")
            break
        elif can == 0 :
            print("Game Over")
            exit()
        else :
            print("----------")

