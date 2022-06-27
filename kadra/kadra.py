import pandas as pd

class Kadra():
  pracownicy = []

  def __init__(self):
    self.load_data()

  def load_data(self):
    data = pd.read_csv('plik2.csv')
    for index, row in data.iterrows():
      self.dodaj_pracownik(row['imie'], row['nazwiska'], row['placa'], row['numer_telefonu'], row['adres'], True)


  def dodaj_pracownik(self, imie, nazwisko, placa, numer_telefonu, adres, skip_print=False):
    pracownik = {
        'imie': imie,
        'nazwisko': nazwisko,
        'placa': placa,
        'numer_telefonu': numer_telefonu,
        'adres': adres
    }
    if not skip_print:
      print("Dodano pracownika: {}".format(pracownik))
    self.pracownicy.append(pracownik)

  def usun_pracownik(self, imie, nazwisko):
    tmp = [i for i in self.pracownicy if not (i['imie'] == imie and i['nazwisko'] == nazwisko)]
    print("Usunięto pracownika: {} {}".format(imie, nazwisko))
    self.pracownicy = tmp

  def licz_srednia_plac(self):
    avg = float(sum(d['placa'] for d in self.pracownicy)) / len(self.pracownicy)
    print("Średnia płac to: {}".format(avg))
    return avg

  def zmien_wynagrodzenie(self, imie, nazwisko, nowe_wynagrodzenie):
    tmp = []
    for i in self.pracownicy:
      if i['imie'] == imie and i['nazwisko'] == nazwisko:
          i['placa']=nowe_wynagrodzenie
      tmp.append(i)
    print("Zmieniono wynagrodzenie pracownika {} {} na {}".format(imie, nazwisko, nowe_wynagrodzenie))
    self.pracownicy = tmp