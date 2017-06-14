

#słownik z wymaganymi wartościami
dictionary = {"fe": 1, "je": 2, "jee": 3, "ain": 3, "dai": 5, "ne": 2, "ai": 2}
correct = [False, False]  # Sprawdza czy tekst jest porawny - z zalozenia - nie jest

#spell = 'fexxxxxxxxxxai' przykładowy spell
punktyMocy = [] ## pusta tablica w której będą przechowywane punkty


def damage(spell, points):
    """Funkcja rekurencyjna sprawdzająca i obliczająca moc zaklęcia"""
    opcja = False  # to oznacza czy znalezlismy jakas opcje, jak nie to -1
    if len(spell) < 1:  #warunek kończący funkcje i wpisujący punkty w tablicę
        punktyMocy.append(points)
        return
    for x in dictionary:    #pętla po słowach ze słownika
        if spell.startswith(x): #warunek gdy czar zaczyna się od wyrazu ze słownika
            opcja = True
            #tutaj dzieje się cała magia
            #rekurencja odbywa się na zasadzie odcięcia o długość znalezionego słowa w słowniku
            #oraz w jednym wykonaniu pętli dodawanie punktu przypisanego temu wyrazowi w słowniku
            damage(spell[len(x):], points=points + dictionary[x])
    damage(spell[1:], points=points - 1) ##odjęcie punktu jeśli nie zostanie znalezione słowo ze słownika

def wypisz(punktyMocy):
    '''Funkcja wypisująca moc zaklęcia'''
    if max(punktyMocy) < 0 or punktyMocy==0:
        print("Najwieksza moc zaklecia: ", 0)
    else:
        print("Najwieksza moc zaklecia: ", max(punktyMocy))

def main(punktyMocy,spell,points):
    """Skrypt rozwiązujący założenia zadania dla czaru"""
    for x, y in enumerate(spell): #pętla wypisująca wartość dla znaku
        if spell[x:].startswith('fe'): #sprawdzenie w którym miejscu znajduje się pierwszy wyraz
            spell = spell[x:]   #odcięcie reszty wyrazów (np. xxxxxxfejeeai)
            correct[0] = True   #zmiana 1 wyrazu na True==dobry
            if spell[:x].endswith('ai')==False: #sprawdzenie po odcięciu czy w wyrazie znajduje się na końcu 'ai'
                correct[1] = False     #zwrócenie złego wyrazu
                punktyMocy.append(0)   #dodanie wartosci zero do mocy czaru
                break
    if spell.endswith('ai'):    #sprawdzenie gdy wyraz konczy się na ai
        correct[1] = True       #zwrócenie dobrego wyrazu
    if spell.count("fe") !=1 or spell.count("fe") ==0: #sprawdzenie czy występuje więcej niż 1 raz 'fe' oraz czy w ogóle jest
        correct[0]=False        #zwrócenie złego wyrazu
        punktyMocy.append(0)    #wartośc punktów 0
    else:       #po odcięciu i sprawdzeniu początku i końca
        for x, y in enumerate(spell):
            if correct[0] == True and correct[1] == True: #warunek gdy jest już fe i ai w wyrazie(w odpowiednich miejscach)
                damage(spell, 0)    #wywołanie funkcji obliczającej moc
                wypisz(punktyMocy)
                break
            elif spell[:-x].endswith('ai'): #warunek jeśli występuje 'ai' gdzieś w wyrazie np.fexxxaixx
                spell = spell[:-x]  #odcięcie reszty
                correct[1] = True   #ostatni przycisk dobry
                if correct[0] == True and correct[1] == True: #warunek obliczania gdy już jest dobry 1 i ostatni wyraz
                    damage(spell, 0)
                    wypisz(punktyMocy)
                    break

main(punktyMocy,'fexxxxxxxxxxaixx',0)