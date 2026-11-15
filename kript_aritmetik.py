def kriptaritmetik_coz(kelime1, kelime2, sonuc):
    # her seyi kucuk harfe ceviriyoruz
    kelime1 = kelime1.lower()
    kelime2 = kelime2.lower()
    sonuc = sonuc.lower()
    
    # tum kelimelerdeki benzersiz harfleri bir kumede topla
    benzersiz_harfler = set(kelime1 + kelime2 + sonuc)
    
    # matematiksel sinir kontrolu: 10'dan fazla farkli harf varsa cozum imkansizdir
    if len(benzersiz_harfler) > 10:
        print("hata: 10'dan fazla benzersiz harf var, 0-9 rakamlari yetmez.")
        return
        
    harfler = list(benzersiz_harfler)
    
    # kelimelerin ilk harfleri 0 olamaz 
    ilk_harfler = {kelime1[0], kelime2[0], sonuc[0]}
    
    def coz(index, atananlar, kullanilan_rakamlar):
        # butun harflere birer rakam atandiysa denklemi test et
        if index == len(harfler):
            # harfleri string uzerinden rakamlara cevirip integer'a donustur
            sayi1 = int("".join(str(atananlar[h]) for h in kelime1))
            sayi2 = int("".join(str(atananlar[h]) for h in kelime2))
            sayi_sonuc = int("".join(str(atananlar[h]) for h in sonuc))
            
            if sayi1 + sayi2 == sayi_sonuc:
                print(f"cozum bulundu!\n")
                print(f"  {sayi1} ({kelime1})")
                print(f"+ {sayi2} ({kelime2})")
                print(f"---------")
                print(f"  {sayi_sonuc} ({sonuc})\n")
                
                print("harf degerleri:")
                for h, r in atananlar.items():
                    print(f"{h} = {r}")
                return True
            return False
            
        mevcut_harf = harfler[index]
        
        # 0'dan 9'a kadar tum ihtimalleri backtracking ile dene
        for rakam in range(10):
            # kural ihlali 1: ilk harf 0 olamaz
            if rakam == 0 and mevcut_harf in ilk_harfler:
                continue
                
            # kural ihlali 2: rakam baska bir harfe atanmissa atla
            if rakam not in kullanilan_rakamlar:
                atananlar[mevcut_harf] = rakam
                kullanilan_rakamlar.add(rakam)
                
                # bir sonraki harfe derine in
                if coz(index + 1, atananlar, kullanilan_rakamlar):
                    return True
                    
                # cozum bulunamadiysa, o rakami bu harften geri al (backtracking)
                kullanilan_rakamlar.remove(rakam)
                del atananlar[mevcut_harf]
                
        return False

    print(f"{kelime1} + {kelime2} = {sonuc} araniyor...\n")
    if not coz(0, {}, set()):
        print("bu problemin matematiksel bir cozumu yok.")

# testler
kriptaritmetik_coz("donald", "gerald", "robert")

print("\n" + "="*30 + "\n")
kriptaritmetik_coz("send", "more", "money")

print("\n" + "="*30 + "\n")
kriptaritmetik_coz("araba", "robot", "degil")
