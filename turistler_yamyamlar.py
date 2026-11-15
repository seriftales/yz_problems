from collections import deque

def durum_gecerli_mi(sol_turist, sol_yamyam):
    # 1. fiziksel sinir kontrolleri
    if sol_turist < 0 or sol_yamyam < 0 or sol_turist > 3 or sol_yamyam > 3:
        return False
    
    # 2. sag kiyi durumunu hesapla
    sag_turist = 3 - sol_turist
    sag_yamyam = 3 - sol_yamyam
    
    # 3. catismali durum kontrolu 
    if sol_turist > 0 and sol_turist < sol_yamyam:
        return False
        
    if sag_turist > 0 and sag_turist < sag_yamyam:
        return False
        
    return True

def bfs_cozum_bul():
    baslangic_durumu = (3, 3, 0)
    hedef_durumu = (0, 0, 1)
    
    # bfs kuyrugu: (mevcut_durum, izlenen_yol)
    kuyruk = deque([(baslangic_durumu, [baslangic_durumu])])
    
    # sonsuz donguyu onlemek icin set
    ziyaret_edilenler = set()
    ziyaret_edilenler.add(baslangic_durumu)
    
    # operatorler: tekneye binen [turist, yamyam]
    hamleler = [[1, 0], [2, 0], [0, 1], [0, 2], [1, 1]]
    
    while kuyruk:
        mevcut_durum, yol = kuyruk.popleft()
        sol_turist, sol_yamyam, tekne = mevcut_durum
        
        # hedefe ulasildi mi?
        if mevcut_durum == hedef_durumu:
            return yol
            
        # operatorleri uygula
        for t_hamle, y_hamle in hamleler:
            # tekne yonune gore sol kiyidaki nufusu guncelle
            if tekne == 0:
                yeni_sol_turist = sol_turist - t_hamle
                yeni_sol_yamyam = sol_yamyam - y_hamle
                yeni_tekne = 1
            else:
                yeni_sol_turist = sol_turist + t_hamle
                yeni_sol_yamyam = sol_yamyam + y_hamle
                yeni_tekne = 0
                
            yeni_durum = (yeni_sol_turist, yeni_sol_yamyam, yeni_tekne)
            
            # gecerli ve yeni durumu kuyruga ekle
            if durum_gecerli_mi(yeni_sol_turist, yeni_sol_yamyam):
                if yeni_durum not in ziyaret_edilenler:
                    ziyaret_edilenler.add(yeni_durum)
                    kuyruk.append((yeni_durum, yol + [yeni_durum]))
                    
    return None

# kodu calistir
cozum_yolu = bfs_cozum_bul()

if cozum_yolu:
    print("bulunan cozum yolu:\n (sol turist, sol yamyam, tekne yonu)\n")
    for adim, durum in enumerate(cozum_yolu):
        print(f"adim {adim}: {durum}")
else:
    print("cozum bulunamadi.")