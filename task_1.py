"""ClearCode Python
Zadanie 1 Gracjan Grochowski"""


def group_by(stream,field, success=None):
    """Funkcja sprawdzająca ilość wylotów w danym roku oraz status misji(Fail or Success) w danym miesiącu"""
    licznik = 0
    if len(field)==4:   #warunek jeśli field=rok
        with stream as f:
             for line in f:   #pętla po lini w pliku
                if field in line[40:48]:    # szukanie elementu początkowego w kolumnie
                    licznik +=1     # dodawanie licznika po każdym wystąpieniu roku w kolumnie
        print(field, " : ",licznik)
    elif len(field)==3: #warunek dla miesiąca
        ## Przypisanie chara zależnego od wprowadzonego stanu success
        if success==False:
            success='F'
        else:
            success='S'
        with open("launch.txt") as f:
            for line in f:  #pętla po liniach w pliku
                if success=="F":    #warunek przy znalezieniu F w kolumnie suc
                    if success in line[193:194] and field in line[18:21]:   #szukanie po kolumnach Suc oraz Date
                        licznik += 1    #dodanie licznika jeśli warunek zostanie spełniony
                elif success=='S':  #warunnek dla podania S
                    if success in line[193:194] and field in line[18:21]:   #szukanie po kolumnach Suc oraz Date
                        licznik += 1    #dodanie liczby 1 jeśli znajdzie Sukcess zależny od miesiąca
        print(field, " : ", licznik)

group_by(open("launch.txt"), 'Jun', True)   #wywołanie funkcji

