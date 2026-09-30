acilis = 65
km = 40
indi_bindi = 200

kmsor = float(input("Kac kilometre gideceksiniz?"))
ucret = kmsor * km + acilis

if ucret <= indi_bindi:
    ucret = indi_bindi
    print("Kısa mesafede indi bindi ücreti alınır o yüzden",ucret,"tl")

elif ucret > indi_bindi:
    ucret = kmsor * km + acilis
    print(ucret, "tl")

input("İyi yolculuklar")
