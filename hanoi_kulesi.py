def hanoi_coz(n, kaynak, yardimci, hedef):
    # temel durum (base case): eger tasinacak tek 1 disk kaldiysa direkt hedefe koy
    if n == 1:
        print(f"disk 1: {kaynak} -> {hedef}")
    else:
        # 1. adim: ustteki (n-1) diski yardimci cubuga tasi 
        hanoi_coz(n - 1, kaynak, hedef, yardimci)
        
        # 2. adim: en alttaki (en buyuk) diski direkt hedef cubuga tasi
        print(f"disk {n}: {kaynak} -> {hedef}")
        
        # 3. adim: yardimci cubuktaki (n-1) diski asil hedefe tasi (kaynak cubugunu yardimci olarak kullan)
        hanoi_coz(n - 1, yardimci, kaynak, hedef)

# ana program
disk_sayisi = int(input("Hanoi kulesi icin disk sayisini giriniz: "))
print(f"--- {disk_sayisi} disk icin hanoi kulesi cozum adimlari ---")
hanoi_coz(disk_sayisi, 'a', 'b', 'c')