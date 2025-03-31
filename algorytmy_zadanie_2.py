#przesuniecie liczb ujemnych na poczatek:

tablica = [145, -7, 32, 449, -56, 124, -1999, -200, 86]
def przesuwanie_na_poczatek(tab):
    wynik = []                  #tworzymy nowa tablice
    for liczba in tab:
        if liczba < 0:
            wynik.append(liczba)  # dodajemy na początek jesli ujemna
    for num in tab:
        if liczba >= 0:
            wynik.append(liczba)  # jesli dodatnia dodajemy pozniej
    return wynik


print(przesuwanie_na_poczatek(tablica)) 

#Złożoność czasowa: O(n) — przechodzimy przez cala tablice 
#Złożoność pamięciowa: O(n) — poniewaz tworzymy nowa tablice



#znalezienie brakujacej liczby:
tabl = [1,2,3,5,6, 7,8,9,10]
n = 10
def szukaj(tab2, n):
    suma_liczb = n * (n + 1) // 2  #suma od 1 do n
    suma_tablica = 0                 # suma liczb w tablicy 
    for l in tab2:
        suma_tablica += l
    return suma_liczb - suma_tablica  #roznica miedzy obiema sumami daje wynik

print(szukaj(tabl, n)) 

#złożoność czasowa: O(n) — przechodzimy przez tablicę
# zlozonosc pamieciowa O(1)— prosta operacja odejmowania dwoch zminneych

array = [7, 6,4,3, 2, 4, 4, 2, 5, 3, 5, 5, 2, 9, 11, 7]
def znajdz_duplikaty(tab3):
    duplikaty = []
    for i in range(len(tab3)):
        for j in range(i + 1, len(tab3)):
            if tab3[i] == tab3[j] and tab3[i] not in duplikaty:
                duplikaty.append(tab3[i]) 
    return duplikaty

print(znajdz_duplikaty(array))  

# zlożoność czasowa: O(n^2) -- zagnieżdżone pętle
# zlożoność pamięciowa: O(m)-- gdzie m to liczba duplikatów


#obracanie tablicy
Array = [7, -120, -13, 4, 5, 99, 651, 1440]
def obracanie(A):
    n = len(A)
    result = [0] * n
    for i in range(n):
        result[i] = A[n - i - 1]  
    return result
print(obracanie(Array)) 

# zlożoność czasowa: O(n) -- przechodzimy przez cala tablice
# zlożoność pamięciowa: O(n)-- bo tworzymy nowa tablice