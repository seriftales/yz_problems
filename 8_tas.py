import heapq

class Dugum:
    def __init__(self, durum, ebeveyn, hamle, g, h):
        self.durum = durum
        self.ebeveyn = ebeveyn
        self.hamle = hamle
        self.g = g  # derinlik
        self.h = h  # sezgisellik
        self.f = g + h
    
    # min-heap'in f(n) degerine gore siralama yapabilmesi icin 
    def __lt__(self, diger):
        return self.f < diger.f

def yanlis_yerdeki_tas_sayisi(durum, hedef_durum):
    yanlis_sayisi = 0
    for i in range(9):
        if durum[i] != 0 and durum[i] != hedef_durum[i]:
            yanlis_sayisi += 1
    return yanlis_sayisi

def olasi_hamleler(durum):
    hamleler = []
    bosluk_idx = durum.index(0)
    y, x = divmod(bosluk_idx, 3)
    
    #(dy, dx, yon_adi)
    operatorler = [
        (-1, 0, "bosluk_yukari"),
        (1, 0, "bosluk_asagi"),
        (0, -1, "bosluk_sola"),
        (0, 1, "bosluk_saga")
    ]
    
    for dy, dx, yon_adi in operatorler:
        yeni_y, yeni_x = y + dy, x + dx
        
        # harita sinirlari kontrolu
        if 0 <= yeni_y < 3 and 0 <= yeni_x < 3:
            hedef_idx = yeni_y * 3 + yeni_x
            yeni_durum = list(durum)
            
            # bosluk ile hedefteki tasi takas et
            yeni_durum[bosluk_idx], yeni_durum[hedef_idx] = yeni_durum[hedef_idx], yeni_durum[bosluk_idx]
            
            hamleler.append((tuple(yeni_durum), yon_adi))
            
    return hamleler

def a_star_8_tas_cozum(baslangic, hedef):
    acik_liste = []
    kapali_liste = set()
    
    # baslangic dugumunu olusturup acik listeye ekliyoruz
    h_baslangic = yanlis_yerdeki_tas_sayisi(baslangic, hedef)
    baslangic_dugumu = Dugum(baslangic, None, "baslangic", 0, h_baslangic)
    heapq.heappush(acik_liste, baslangic_dugumu)
    
    taranan_dugum_sayisi = 0

    while acik_liste:
        mevcut_dugum = heapq.heappop(acik_liste)
        
        # dugum daha once islendiyse atla
        if mevcut_dugum.durum in kapali_liste:
            continue
            
        kapali_liste.add(mevcut_dugum.durum)
        taranan_dugum_sayisi += 1
        
        # hedefe ulastik mi?
        if mevcut_dugum.durum == hedef:
            yol = []
            gecici = mevcut_dugum
            while gecici:
                yol.append((gecici.hamle, gecici.durum))
                gecici = gecici.ebeveyn
            # yolu bastan sona dogru dondur
            return yol[::-1], taranan_dugum_sayisi
            
        # mevcut dugumden uretilebilecek yeni durumlari genislet
        for yeni_durum, hamle_adi in olasi_hamleler(mevcut_dugum.durum):
            if yeni_durum not in kapali_liste:
                yeni_g = mevcut_dugum.g + 1
                yeni_h = yanlis_yerdeki_tas_sayisi(yeni_durum, hedef)
                yeni_dugum = Dugum(yeni_durum, mevcut_dugum, hamle_adi, yeni_g, yeni_h)
                
                heapq.heappush(acik_liste, yeni_dugum)
                
    return None, taranan_dugum_sayisi

# --- test senaryosu ---
baslangic_durumu = (4, 1, 3, 2, 8, 5, 7, 0, 6)
hedef_durumu = (1, 2, 3, 4, 5, 6, 7, 8, 0)

cozum, sayac = a_star_8_tas_cozum(baslangic_durumu, hedef_durumu)

if cozum:
    print(f"cozum bulundu! taranan toplam dugum sayisi: {sayac}\n")
    for adim, (hamle, durum) in enumerate(cozum):
        print(f"adim {adim} ({hamle}):")
        print(f"[{durum[0]}] [{durum[1]}] [{durum[2]}]")
        print(f"[{durum[3]}] [{durum[4]}] [{durum[5]}]")
        print(f"[{durum[6]}] [{durum[7]}] [{durum[8]}]\n")
else:
    print("cozum bulunamadi.")