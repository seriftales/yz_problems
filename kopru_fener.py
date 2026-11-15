import heapq
from itertools import combinations

class Dugum:
    def __init__(self, fener_sagda, sol_kiyi, sag_kiyi, ebeveyn, hamle_adi, maliyet):
        self.fener_sagda = fener_sagda  # 0: fener solda, 1: fener sagda
        
        # kiyidaki kisileri siralayip tuple yap
        self.sol_kiyi = tuple(sorted(sol_kiyi))
        self.sag_kiyi = tuple(sorted(sag_kiyi))
        
        # mevcut durumu tek bir paket haline getir
        self.durum = (self.fener_sagda, self.sol_kiyi, self.sag_kiyi)
        
        self.ebeveyn = ebeveyn
        self.hamle_adi = hamle_adi
        self.maliyet = maliyet  # g(n): baslangictan buraya kadar gecen toplam sure

    def __lt__(self, diger):
        return self.maliyet < diger.maliyet

def olasi_hamleler(mevcut):
    hamleler = []
    
    # fener soldaysa, saga 1 veya 2 kisi gecebilir
    if mevcut.fener_sagda == 0:
        mevcut_kiyi = mevcut.sol_kiyi
        hedef_fener = 1
        yon_mesaji = "saga gecti"
    # fener sagdaysa, sola feneri getirmek icin 1 veya 2 kisi donebilir
    else:
        mevcut_kiyi = mevcut.sag_kiyi
        hedef_fener = 0
        yon_mesaji = "sola dondu"
        
    # kiyidaki kisilerden 1'li ve 2'li kombinasyonlari uret
    kombinasyonlar = list(combinations(mevcut_kiyi, 1)) + list(combinations(mevcut_kiyi, 2))
    
    for gecenler in kombinasyonlar:
        # gecis maliyeti: gruptaki en yavas kisinin hizidir 
        gecis_suresi = max([kisi[1] for kisi in gecenler])
        yeni_maliyet = mevcut.maliyet + gecis_suresi
        
        yeni_sol = list(mevcut.sol_kiyi)
        yeni_sag = list(mevcut.sag_kiyi)
        
        isimler = []
        for kisi in gecenler:
            isimler.append(kisi[0])
            if hedef_fener == 1:  # saga geciliyorsa
                yeni_sol.remove(kisi)
                yeni_sag.append(kisi)
            else:                 # sola donuluyorsa
                yeni_sag.remove(kisi)
                yeni_sol.append(kisi)
                
        hamle_mesaji = f"{','.join(isimler)} {yon_mesaji} ({gecis_suresi} dk)"
        hamleler.append((hedef_fener, yeni_sol, yeni_sag, hamle_mesaji, yeni_maliyet))
            
    return hamleler

def dijkstra_kopru_cozumu(kisiler):
    # kisiler formati list of tuples olmali
    acik_liste = []
    kapali_liste = set()
    
    # baslangic dugumunu olustur (herkes solda, fener solda, sure = 0)
    baslangic = Dugum(0, kisiler, [], None, "baslangic", 0)
    heapq.heappush(acik_liste, baslangic)
    
    while acik_liste:
        mevcut = heapq.heappop(acik_liste)
        
        # eger bu kiyi dizilimine daha once daha hizli bi yoldan ulasmissak atla
        if mevcut.durum in kapali_liste:
            continue
            
        kapali_liste.add(mevcut.durum)
        
        # hedef kontrolu: sol kiyida kimse kalmadiysa islem tamamdir
        if len(mevcut.sol_kiyi) == 0:
            yol = []
            gecici = mevcut
            while gecici:
                yol.append((gecici.hamle_adi, gecici.maliyet))
                gecici = gecici.ebeveyn
            # yolu bastan sona dogru dondur
            return yol[::-1]
            
        # yeni durumlari genislet ve min-heap kuyruguna it
        for fener, sol, sag, mesaj, yeni_sure in olasi_hamleler(mevcut):
            yeni_durum = (fener, tuple(sorted(sol)), tuple(sorted(sag)))
            if yeni_durum not in kapali_liste:
                yeni_dugum = Dugum(fener, sol, sag, mevcut, mesaj, yeni_sure)
                heapq.heappush(acik_liste, yeni_dugum)
                
    return None

def sonuclari_yazdir(senaryo_adi, kisiler):
    print(f"--- {senaryo_adi} ---")
    cozum = dijkstra_kopru_cozumu(kisiler)
    if cozum:
        for adim, (hamle, toplam_sure) in enumerate(cozum):
            if adim == 0:
                continue
            print(f"adim {adim}: {hamle} -> toplam sure: {toplam_sure}")
        print(f"\n=> optimal sonuc: {cozum[-1][1]} dakika\n")

# test 1: standart senaryo
kisiler_1 = [('A', 1), ('B', 2), ('C', 5), ('D', 10)]
sonuclari_yazdir("standart ornek (1,2,5,10)", kisiler_1)

# test 2: zorlu senaryo
kisiler_2 = [('A', 1), ('B', 4), ('C', 5), ('D', 10)]
sonuclari_yazdir("zor ornek(1,4,5,10)", kisiler_2)