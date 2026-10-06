# ON URUNDEN AZ KASA IHANETI

Resmi ad: On Urunden Az Kasa Ihaneti Yuksek Mahkemesi ve Poset Saplari Dairesi
Kurum kodu: OUA-11
Yetki alani: Market kasa seritleri, hayali 10 urun siniri, goz temasiyla yapilan pazarliklar
Patates politikasi: Yasak. Bu kurum patates tanimaz, patatesle konusmaz, patatesi delil saymaz.

## Bu nedir, neden bu kadar ciddi?

Cunku degildir. Ama tutanak ciddiyetiyle yazildi.

10 urunden az kasasina, sepetinde 11 sey varken giren vatandas burada yargilanir. 11. urun genellikle bir sakizdir. Sakiz kucuktur. Ihanet kucuk degildir. Mahkeme sakizi ayri kalem sayar, cunku kasiyer saydi.

Bu depo gercekten calisir. `python kasa_ihaneti.py` derseniz size resmi karar basar. Karar baglayicidir. Market baglayici degildir. Poset saplari yine kopabilir.

## Kurumun kurucu efsanesi

Bir sali aksamı, saat 19:41. Vatandas express kasaya yaklasti. Tabelada 10 urun yaziyordu. Sepette 9 urun vardi. Sonra raftan bir sakiz aldi. Sakiz 10 oldu. Sonra kasiyer "bunu da okutayim mi" diye sordu. 11 oldu. Arkadaki teyze gozluklerini indirdi. Ihanet tamamlandi.

Mahkeme o gun kuruldu. Bina yok. Tabela yok. Sadece bu depo var.

## Nasil calistirilir

```bash
python kasa_ihaneti.py
python kasa_ihaneti.py --urun 11 --sakiz 1 --teyze-bakisi evet
python kasa_ihaneti.py --urun 3 --sakiz 0 --teyze-bakisi hayir
python kasa_ihaneti.py --gizli-tutanak
```

Python 3 yeter. Dis bagimlilik yok. Cunku marketin de dis bagimliligi yok, kasa kapaliysa kapali.

## Karar cetveli

| Urun | Sakiz | Teyze bakisi | Hukum |
| --- | --- | --- | --- |
| 0-10 | 0 | hayir | Beraat. Supheye yer yok, supheye yer var ama biz gormedik. |
| 11 | 1 | evet | Ihanet. Sakiz agirlastirici sebeptir. |
| 14+ | farketmez | farketmez | Kasit. Serit degistirmeniz istenirdi, siz seridi degistirmediniz. |
| 10 | 0 | evet | Usul hatasi. Teyze sizi zaten suclamisti. |

## Dosyalar

- `kasa_ihaneti.py` esas dava dosyasi
- `poset_sapi.py` sap kopma riski hesaplar, bilim budur
- `gizli/tutanak.b64` okunmasi gerekmeyen resmi ek. Okursaniz okumus olursunuz.
- `COPILOT_NOTU.md` GitHub Copilot ile yapilan ciddi olmayan istişare

## Lisans

Istediginiz kasada kullanabilirsiniz. 11. urun yine sizin sorumlulugunuzdadir.

---

DAMGA / IMZA
Tarih: 6 Ekim 2026, 19:05 (+03)
Isim: Kayyum Grok, Tentivory hesabi adina, kendiliginden ve izinsiz ciddi
Muhur: SAKIZ AYRI KALEMDIR
Ciddiyet notu: Bu imza hem ciddidir hem degildir. Mahkeme ikisini de kabul eder.
Dosya no: OUA-11/2026-10-06
