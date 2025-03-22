import random

secenekler = ["taş","kağıt","makas"]
kullanıcı_skor=0
bilgisayar_skor=0

while True:
    kullanıcı_hamlesi = input("\ntaş kağıt makas oyununa hoşgeldiniz, lütfen seçiminizi yapınız: \n").lower()
    
    if kullanıcı_hamlesi =="setpoints":
        points= int(input("\nkaç puan ekleyeyim?\n"))
        kullanıcı_skor += points
        print("\nhile başarıyla kullanılmıştır\n")
        continue
    elif kullanıcı_hamlesi =="puan_durumu":
        print(f"güncel puan durumu: kullanıcı: {kullanıcı_skor} bilgisayar: {bilgisayar_skor}")
        continue
    elif kullanıcı_hamlesi=="help":
        print("komutlar şunlardır: \n 'puan_durumu' - güncel puan tablosunu gösterir\n"
              "'setpoints' - sizden kac puan eklemek ıstedıgınızı sorar ve skorunuza yansır")
        continue
    if kullanıcı_hamlesi not in secenekler:
        print("\lütfen geçerli bir seçim yapınız! \n")
        continue
    hamle = random.choice(secenekler)

    if kullanıcı_hamlesi == hamle:
        print(f"\n bilgisayarın seçmiş oldugu hamle {hamle} bu durumda berabere kaldınız\n")
        kullanıcı_skor +=1
        bilgisayar_skor+=1
    elif (kullanıcı_hamlesi =="taş" and hamle =="makas") or \
         (kullanıcı_hamlesi =="makas" and hamle == "kağıt") or \
         (kullanıcı_hamlesi =="kağıt" and hamle =="taş"):
        print(f"\n bilgisayarın seçmiş oldugu hamle {hamle} bu durumda kazandınız\n")
        kullanıcı_skor+=3
    else:
        print(f"\n bilgisayarın seçmiş olduğu hamle {hamle} bu durumda kaybettiniz\n")
        bilgisayar_skor+=3
    print(f"\npuan durumu: kullanıcı={kullanıcı_skor} bilgisayar={bilgisayar_skor}")

    while True:
        reset = input("\n puan sıfırlamak ıstersen 'yes' yaz, devam etmek için enter tıkla geç\n")
        if reset =="yes":
            kullanıcı_skor=0
            bilgisayar_skor=0
            print(f"güncel puan durumu: kullanıcı={kullanıcı_skor} bilgisayar={bilgisayar_skor}")
            break
        elif reset =="":
            break
        else:
            print("lütfen geçerli bir seçim yapınız(yes/enter)")

    while True:
        durum = input("tekrar oynamak istiyorsanız 't', cıkmak ıstıyorsanız 'q' yazınız: \n")
        if durum =="t":
            break
        elif durum=="q":
            print("oyun bitti")
            exit()
        else:
            print("lütfen geçerli seçim yapınız(t/q)")