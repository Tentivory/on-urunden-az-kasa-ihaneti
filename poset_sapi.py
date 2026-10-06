#!/usr/bin/env python3
"""Poset sapi kopma komisyonu. Yardimci daire."""

ESIK = 7


def sap_dayanir_mi(agirlik_kg: float, delik_sayisi: int) -> str:
    if agirlik_kg < 0 or delik_sayisi < 0:
        return "Negatif poset evrende yok. Kasaya donun."
    skor = agirlik_kg * 1.4 + delik_sayisi * 0.8
    if skor < ESIK:
        return f"Sap dayanir (skor {skor:.1f}). Bu bilimsel bir mucize degil, sadece hafif alisveris."
    if skor < 12:
        return f"Sap dusunuyor (skor {skor:.1f}). Merdivende kopma ihtimali artistik."
    return f"Sap istifa etti (skor {skor:.1f}). Iki poset, bir onur."


if __name__ == "__main__":
    print(sap_dayanir_mi(3.2, 2))
    print(sap_dayanir_mi(6.5, 4))
