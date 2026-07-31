class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        # 1. Adım: Kendimize boş bir hafıza defteri açıyoruz.
        # Bu deftere "Gördüğümüz Sayı : Hangi Sırada (İndeks)" şeklinde kayıt yapacağız.
        hafiza_defteri = {} 

        # 2. Adım: Masadaki paralara (sayılara) sırayla bakmaya başlıyoruz.
        # enumerate() fonksiyonu bize hem sayının kendisini hem de kaçıncı sırada (i) olduğunu verir.
        for i, sayi in enumerate(nums):
            
            # 3. Adım: Hedefe ulaşmak için bize gereken eksik parçayı buluyoruz (Tek matematik burası!)
            aranan_sayi = target - sayi 
            
            # 4. Adım: Hafıza defterine bakıyoruz. Bu aranan sayıyı daha önce gördük mü?
            if aranan_sayi in hafiza_defteri:
                                # Defterdeki sayının sırasını ve elimizdeki sayının sırasını teslim edip işi bitiriyoruz.
                return [hafiza_defteri[aranan_sayi], i]
            
            # 5. Adım: Eğer aranan sayı defterde yoksa, şu an elimizde tuttuğumuz sayıyı 
            # sırası (indeksi) ile birlikte deftere kaydediyoruz ki sonraki sayılar aradığında bulabilsin.
            hafiza_defteri[sayi] = i