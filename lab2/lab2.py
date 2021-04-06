import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 5)

#Wczytanie pliku csv
data = pd.read_csv('samochody1tys.csv')

#Stworzenie kopii danych ze zmienionymi nazwami kolumn
data_copy = data.rename(columns={"id" : "ID", "marka" : "MARKA", "model" : "MODEL", "rok_produkcji" : "ROK PRODUKCJI", "rodzaj_silnika" : "RODZAJ SILNIKA",
                                 "pojemnosc_silnika" : "POJEMNOŚĆ SILNIKA", "przebieg" : "PRZEBIEG", "cena" : "CENA", "wojewodztwo" : "WOJEWÓDZTWO"}).copy()
#print(data_copy)

#Stworzenie wykresu kołowego pokazującego sumę cen samochodów danej marki
data_copy2 = data_copy.groupby('MARKA')['CENA'].sum().plot(kind='pie')

#Pokazanie minimalnego, maksymalnego oraz sumarycznego przebiegu samochodów danej marki
data_copy3 = data_copy.groupby('MARKA')['PRZEBIEG'].agg([min, max, sum])
#print(data_copy3)

#Wybranie 20 losowych rekordów i posortowanie ich według województwa
data_copy4 = data_copy.sample(20).sort_values('WOJEWÓDZTWO')
#print(data_copy4)

#Zmiana całej zawartości kolumny na małe litery
data_copy5 = data_copy['MODEL'].map(lambda name: name.lower())
#print(data_copy5)

#Wybranie 30 rekordów i usunięcie duplikatów w kolumnie marka
data_copy6 = data_copy.sample(30).drop_duplicates('MARKA')
#print(data_copy6)

#Usunięcie wskazanych kolumn
data_copy7 = data_copy.drop(columns=['ID', 'WOJEWÓDZTWO', 'MARKA'])
#print(data_copy7)

#Zliczenie unikalnych rekordów w każdej z kolumn
data_copy8 = data_copy.nunique()
#print(data_copy8)

#Wybranie 30 samochodów z największą ceną
data_copy9 = data_copy.nlargest(30, 'CENA')
#print(data_copy9)

#Wybranie marki, modelu, ceny i województwa samochodów, których przebieg jest większy od 300000
data_copy10 = data_copy.loc[data_copy['PRZEBIEG'] > 300000, ['MARKA','MODEL', 'CENA', 'WOJEWÓDZTWO']]
print(data_copy10)
