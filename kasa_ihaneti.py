#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""On urunden az kasa ihaneti yuksek mahkemesi.

Gercekten calisir. Anlamli olmak zorunda degildir.
Patates delil olarak kabul edilmez.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
from pathlib import Path

SINIR = 10
SAKIZ_CARPANI = 1.7
TEYZE_CEZA = 2


def hukum_ver(urun: int, sakiz: int, teyze_bakisi: bool) -> dict:
    if urun < 0 or sakiz < 0 or sakiz > urun:
        raise ValueError("Sepet negatif olamaz. Sakiz urunden fazla olamaz. Fizik boyle dedi.")

    fazlalik = max(0, urun - SINIR)
    puan = fazlalik * 3 + (sakiz * SAKIZ_CARPANI if fazlalik else 0)
    if teyze_bakisi:
        puan += TEYZE_CEZA

    if urun <= SINIR and not teyze_bakisi:
        sonuc = "BERAAT"
        gerekce = "Sinir icindesiniz. Teyze de bakmadi. Nadir bir hukuki bahar."
    elif urun <= SINIR and teyze_bakisi:
        sonuc = "USUL_HATASI"
        gerekce = "Urun sayisi temiz, bakis kirli. Teyze sizi dosyaya gecirdi."
    elif sakiz and fazlalik == 1:
        sonuc = "IHANET"
        gerekce = "11. kalem sakiz. Kucuk ambalaj, buyuk kasit. Ayri okutuldu."
    elif fazlalik >= 4:
        sonuc = "KASIT"
        gerekce = "Bu artik express kasa degil, normal kasanin kisa boylu akrabasi."
    else:
        sonuc = "IHBAR"
        gerekce = "Sinir asildi. Kasit tam ispatlanamadi, poset supheli."

    return {
        "sonuc": sonuc,
        "puan": round(puan, 2),
        "gerekce": gerekce,
        "fazlalik": fazlalik,
        "tutanak_no": tutanak_no(urun, sakiz, teyze_bakisi),
    }


def tutanak_no(urun: int, sakiz: int, teyze_bakisi: bool) -> str:
    ham = f"{urun}|{sakiz}|{int(teyze_bakisi)}|OUA-11".encode()
    ozet = hashlib.sha256(ham).hexdigest()[:8].upper()
    return f"OUA-{ozet}"


def poset_riski(urun: int) -> str:
    risk = min(99, 12 + urun * 6 + random.randint(0, 7))
    if risk > 80:
        return f"Poset sapi kopma riski %{risk}. Iki poset isteyin, gurur sonra konussun."
    if risk > 50:
        return f"Poset sapi kopma riski %{risk}. Sap bakiyor, siz bakmiyorsunuz."
    return f"Poset sapi kopma riski %{risk}. Bu sefer sap sizi affetti."


def gizli_tutanak() -> str:
    """Ek dosyayi cozer. Siyasi degil gibi durur, dipnotta siyasi durur."""
    yol = Path(__file__).resolve().parent / "gizli" / "tutanak.b64"
    if not yol.exists():
        return "Gizli tutanak kasada unutulmus."
    return base64.b64decode(yol.read_text().strip()).decode("utf-8")


def rapor(urun: int, sakiz: int, teyze_bakisi: bool) -> str:
    karar = hukum_ver(urun, sakiz, teyze_bakisi)
    satirlar = [
        "=" * 46,
        "ON URUNDEN AZ KASA IHANETI YUKSEK MAHKEMESI",
        "=" * 46,
        f"Tutanak no : {karar['tutanak_no']}",
        f"Urun       : {urun}",
        f"Sakiz      : {sakiz}",
        f"Teyze bakisi: {'evet, gozluk indi' if teyze_bakisi else 'hayir, teyze mesgul'}",
        f"Fazlalik   : {karar['fazlalik']}",
        f"Ceza puani : {karar['puan']}",
        f"Hukum      : {karar['sonuc']}",
        f"Gerekce    : {karar['gerekce']}",
        poset_riski(urun),
        "Damga: Kayyum Grok / 6 Ekim 2026 / SAKIZ AYRI KALEMDIR",
        "=" * 46,
    ]
    return "\n".join(satirlar)


def main() -> None:
    ayirici = argparse.ArgumentParser(description="10 urunden az kasa ihanetini yargilar.")
    ayirici.add_argument("--urun", type=int, default=11, help="Sepetteki urun sayisi")
    ayirici.add_argument("--sakiz", type=int, default=1, help="Kac tanesi sakiz")
    ayirici.add_argument("--teyze-bakisi", choices=["evet", "hayir"], default="evet")
    ayirici.add_argument("--gizli-tutanak", action="store_true", help="Okunmamasi gereken eki ac")
    args = ayirici.parse_args()

    if args.gizli_tutanak:
        print(gizli_tutanak())
        return

    print(rapor(args.urun, args.sakiz, args.teyze_bakisi == "evet"))


if __name__ == "__main__":
    main()
