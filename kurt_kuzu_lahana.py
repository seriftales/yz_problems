from collections import deque

def durum_gecerli_mi(ciftci, kurt, kuzu, lahana):
    # kural 1: ciftci yokken kurt kuzuyu yer 
    if kurt == kuzu and ciftci != kurt:
        return False
        
    # kural 2: ciftci yokken kuzu lahanayi yer
    if kuzu == lahana and ciftci != kuzu:
        return False
        
    # kisitlamalara takilmayan durum gecerlidir 
    return True

def bfs_kurt_kuzu_lahana():
    # durum formati: (ciftci, kurt, kuzu, lahana)
    # 0: baslangic kiyisi, 1: karsi kiyi (hedef)
    baslangic = (0, 0, 0, 0)
    hedef = (1, 1, 1, 1)
    
    # bfs motoru
    kuyruk = deque([(baslangic, [baslangic])])
    
    # sonsuz donguyu onle
    ziyaret_edilenler = set()
    ziyaret_edilenler.add(baslangic)
    
    while kuyruk:
        mevcut_durum, yol = kuyruk.popleft()
        c, w, k, l = mevcut_durum
        
        # hedefe ulastik mi?
        if mevcut_durum == hedef:
            return yol
            
        # operatorlerin uretilmesi
        # ciftci her hamlede yer degistirir: 1 - c islemi 0'i 1, 1'i 0 yapar (kiyi degisimi)
        yeni_durumlar = []
        
        # operator 1: ciftci tek basina gecer
        yeni_durumlar.append((1 - c, w, k, l))
        
        # operator 2: ciftci kurt ile gecer 
        if c == w:
            yeni_durumlar.append((1 - c, 1 - w, k, l))
            
        # operator 3: ciftci kuzu ile gecer
        if c == k:
            yeni_durumlar.append((1 - c, w, 1 - k, l))
            
        # operator 4: ciftci lahana ile gecer
        if c == l:
            yeni_durumlar.append((1 - c, w, k, 1 - l))
            
        # uretilen durumlari test et ve kuyruga at
        for yeni_d in yeni_durumlar:
            if durum_gecerli_mi(*yeni_d): # catismali durumlari at
                if yeni_d not in ziyaret_edilenler:
                    ziyaret_edilenler.add(yeni_d)
                    kuyruk.append((yeni_d, yol + [yeni_d]))
                    
    return None


cozumler = bfs_kurt_kuzu_lahana()

if cozumler:
    print("cozum yolu bulundu (0: baslangic, 1: karsi kiyi):")
    print("(ciftci, kurt, kuzu, lahana)\n")
    for adim, durum in enumerate(cozumler):
        print(f"adim {adim:2d}: {durum}")
else:
    print("cozum bulunamadi.")