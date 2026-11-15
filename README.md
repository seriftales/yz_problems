# Yapay Zeka Problemleri

Bu depo yapay zeka derslerinde işlenen klasik arama, kısıtlamalı optimizasyon ve durum uzayı problemlerinin Python implementasyonlarını içermektedir. Problemler brute force yöntemleriyle değil; BFS, DFS, Dijkstra ve A* gibi arama algoritmaları kullanılarak arama uzayının budanması ve sezgisel maliyet hesaplamalarıyla çözülmüştür.


### 1. Turistler ve Yamyamlar Problemi
*   **Algoritma:** Genişlik Öncelikli Arama (BFS - Breadth-First Search)
*   **Yaklaşım:** Bütün geçişlerin maliyeti eşit olduğu için en kısa yolu garanti eden BFS kullanılmıştır. Durumlar `(sol_turist, sol_yamyam, tekne_yonu)` şeklinde modellenmiş, yamyam sayısının turist sayısını geçtiği "çatışmalı durumlar" anında budanarak arama ağacının RAM'i şişirmesi engellenmiştir.

### 2. 8-Taş Problemi
*   **Algoritma:** A* Algoritması
*   **Yaklaşım:** Arama uzayının faktöriyel büyüklüğe ulaşmasını engellemek için sezgisel maliyet fonksiyonu ($f(n) = g(n) + h(n)$) kullanılmıştır. 
    *   Durumlar 3x3 matris yerine $O(1)$ hash süresi için tek boyutlu *Tuple* olarak tutulmuştur.
    *   Operatörler taşlara değil, sistemdeki otonom ajan kabul edilen "boşluğun (0)" hareketine bağlanmıştır.
    *   Düğümler `heapq` (Min-Heap) kullanılarak maliyete göre sıralanmıştır.

### 3. Kurt-Kuzu-Lahana Problemi
*   **Algoritma:** Genişlik Öncelikli Arama (BFS)
*   **Yaklaşım:** 4 bağımsız varlığın kıyı durumu 0 ve 1'lerden (sol/sağ) oluşan 4-bitlik bir yapı `(ciftci, kurt, kuzu, lahana)` ile modellenmiştir. Av-avcı kısıtlamaları kontrol edilerek geçersiz kombinasyonlar elenmiş, sistem güvenli rotayı bulana kadar sığdan derine taranmıştır.

### 4. Köprü ve Fener Problemi
*   **Algoritma:** Dijkstra Algoritması
*   **Yaklaşım:** Önceki problemlerin aksine bu grafikte her hamlenin maliyeti birbirinden farklıdır. Bu nedenle BFS yerine geçiş sürelerini minimize eden Dijkstra kurulmuştur. *Hard-code* sezgisel kurallar yazmak yerine, `itertools.combinations` ile dinamik eylem uzayı oluşturulmuş, algoritmanın en hızlı rotayı otonom olarak bulması sağlanmıştır.

### 5. Hanoi Kulesi Problemi
*   **Algoritma:** Recursive Derinlik Araması / AND-OR Ağacı
*   **Mühendislik Yaklaşımı:** Problem, Parçala ve Fethet mantığıyla daha küçük alt problemlere indirgenmiştir. Çözüm uzayında fiziksel olarak $O(2^n)$ karmaşıklığa sahip olan bu sistem, İşletim Sisteminin *Call Stack* belleği üzerinden minimum kodla yönetilmiştir.

### 6. Kriptaritmetik Kelime Çözücü
*   **Algoritma:** Derinlik Öncelikli Arama (DFS) ve Geriye İz Sürme (Backtracking)
*   **Mühendislik Yaklaşımı:** Harflere 0-9 arası rakamlar atanarak dinamik bir durum uzayı yaratılmıştır. Kural ihlali görüldüğünde ya da denklemin tutmadığı çelişki düğümleri, sistem bellekteki atamayı silip bir üst düğüme geri dönerek iterasyonlarını optimize eder. Sistem girilen her türlü toplama kelime kurgusuna adapte olabilecek şekilde tasarlanmıştır.

## 🚀 Kurulum ve Çalıştırma

Projeyi bilgisayarınıza klonlayın ve klasör içine girin:

```bash
git clone [https://github.com/KULLANICI_ADIN/yz_problems.git](https://github.com/KULLANICI_ADIN/yz_problems.git)
cd yz_problems
```
İlgili problemi çalıştırmak için Python 3 yüklü sisteminizde komutu kullanın.Örneğin:

```bash
python3 8_tas.py
```
