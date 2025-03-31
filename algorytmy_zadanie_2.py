#przesuniecie liczb ujemnych na poczatek

tablica = [145, -7, 32, 449, -56, 124, -1999, -200, 86]
def przesuwanie_na_poczatek(tab):
    wynik = []                  #tworzymy nowa tablice
    for liczba in tab:
        if liczba < 0:
            wynik.append(liczba)  # Dodajemy na początek jesli ujemna
    for num in tab:
        if liczba >= 0:
            wynik.append(liczba)  # jesli dodatnia dodajemy pozniej
    return wynik


print(przesuwanie_na_poczatek(tablica)) 


