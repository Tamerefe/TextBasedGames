Ninja = {

"Guc": 516,
"Hp" : 3250,
"Heal": 0

}

Silahci = {

"Guc": 952,
"Hp" : 1402,
"Heal": 0

}

Dovuscu = {

"Guc": 291,
"Hp" : 6372,
"Heal": 0
}

Sifaci = {

"Guc": 105,
"Hp" : 2908,
"Heal":350

}

karakterler = dict(
Ninja = {
"Guc": 516,
"Hp" : 3250
},

Silahci = {
"Guc": 952,
"Hp" : 1402,
"Heal": 0
},

Dovuscu = {
"Guc": 291,
"Hp" : 6372,
"Heal": 0
},

Sifaci = {

"Guc": 105,
"Hp" : 2908,
"Heal": 350
})


menu = """
                    Dolliet'in Savas Oyununa Hosgeldiniz o7

1)1 Vs 1
2)1 Vs 2
3)2 Vs 2
4)1 Vs 9
5)Karakterlerin Ozellikleri
6)Kendi Karakterlerin Ile 1 Vs 1    (Yakinda)
7)Lol Karakterleri 1 Vs 1   (Yakinda)
8)TFT Karakterleri 1 Vs 1   (Yakinda)
9)...   (Yakinda)
Q)Cikis

"""

def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["Guc"]
    vurulan["Hp"] = vurulan["Hp"] - eksilen

def can(verilen:dict,alinan:dict):
    eklenen = verilen["Heal"]
    alinan["Hp"] = alinan["Hp"] + eklenen

def kar(karakterler:dict):
    for a,b in karakterler.items():
        print(a,b)

#while True:

print(menu)
secim = input("Islem Numarasini Giriniz :")

if secim == "1":
    imenu = """

1)Ninja Vs Silahci
2)Silahci Vs Dovuscu
3)Dovuscu Vs Ninja
4)Sifaci Vs Silahci
5)Sifaci Vs Dovuscu
6)Sifaci Vs Ninja


    """
    print(imenu)
    isecim = input("Islem Numarasini Giriniz :")

    if isecim == "1":
        while Silahci["Hp"] > 0 :
            input("Vurmak Icin Enter'a Basiniz!")
            vur(Ninja,Silahci)
            vur(Silahci,Ninja)
            print("Silahci'nin Cani:",Silahci["Hp"])
            print("Ninja'nin Cani:",Ninja["Hp"])

    if isecim == "2":
        while Silahci["Hp"] > 0 :
            input("Vurmak Icin Enter'a Basiniz!")
            vur(Dovuscu,Silahci)
            vur(Silahci,Dovuscu)
            print("Silahci'nin Cani:",Silahci["Hp"])
            print("Dovuscu'nun Cani:",Dovuscu["Hp"])

    if isecim == "3":
        while Ninja["Hp"] > 0 :
            input("Vurmak Icin Enter'a Basiniz!")
            vur(Ninja,Dovuscu)
            vur(Dovuscu,Ninja)
            print("Dovuscu'nin Cani:",Dovuscu["Hp"])
            print("Ninja'nin Cani:",Ninja["Hp"])

    if isecim == "4":
        while Sifaci["Hp"] > 0 :
            input("Vurmak Icin Enter'a Basiniz!")
            vur(Sifaci,Silahci)
            can(Sifaci,Sifaci)
            vur(Silahci,Sifaci)
            print("Silahci'nin Cani:",Silahci["Hp"])
            print("Sifaci Kendini Iyilestirdi! {} Can Artti".format(Sifaci["Heal"]))
            print("Sifaci'nin Cani:",Sifaci["Hp"])

    if isecim == "5":
        while Dovuscu["Hp"] > 0 :
            input("Vurmak Icin Enter'a Basiniz!")
            vur(Sifaci,Dovuscu)
            can(Sifaci,Sifaci)
            vur(Dovuscu,Sifaci)
            print("Dovuscu'nin Cani:",Dovuscu["Hp"])
            print("Sifaci Kendini Iyilestirdi! {} Can Artti".format(Sifaci["Heal"]))
            print("Sifaci'nin Cani:",Sifaci["Hp"])

    if isecim == "6":
        while Sifaci["Hp"] > 0 :
            input("Vurmak Icin Enter'a Basiniz!")
            vur(Sifaci,Ninja)
            can(Sifaci,Sifaci)
            vur(Ninja,Sifaci)
            print("Ninja'nin Cani:",Ninja["Hp"])
            print("Sifaci Kendini Iyilestirdi! {} Can Artti".format(Sifaci["Heal"]))
            print("Sifaci'nin Cani:",Sifaci["Hp"])

if secim == "2":
    yenimenu = """

1)Dovuscu Vs Ninja and Silahci
2)Ninja Vs Silahci and Dovuscu
3)Silahci Vs Dovuscu and Ninja
                    """
    print(yenimenu)
    yenisecim = input("Islem Numarasini Giriniz :")
    if yenisecim == "1":
        while Dovuscu["Hp"] > 0 :
            input("Vurmak Icin Enter'a Basiniz!")
            vur(Silahci,Dovuscu)
            vur(Silahci,Dovuscu)
            vur(Ninja,Dovuscu)
            vur(Ninja,Dovuscu)
            vur(Dovuscu,Silahci)
            vur(Dovuscu,Ninja)
            print("Silahci'nin Cani:",Silahci["Hp"])
            print("Dovuscu'nun Cani:",Dovuscu["Hp"])
            print("Ninja'nin Cani:",Ninja["Hp"])


if secim == "5":
    kar(karakterler)

if secim == "Q" or secim == "q":
    print("BB Daha Sonra Tekrar Bekleriz...")
    quit()
# else:
#     print("Hatali Giris Yaptiniz Kapatmak Zorundayim")
