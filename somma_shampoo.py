# Scrivete uno script che sommi tutti i valori delle vendite degli shampoo del file "shampoo_sales.csv". Poi, committate il file in cui l'avete scritto

# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
my_file = open("shampoo_sales.csv", "r")
for line in my_file:
# Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
    # Se il primo valore è diverso da 'Date' ...
    if elements[0] != 'Date':
# Setta la data e il valore
        date  = elements[0]
        value = elements[1]
# Aggiungi alla lista dei valori gli elementi di value
        values.append (float(value))
#Definisco una funzione somma
def somma (lista):
    somma = 0
    for item in lista:
        somma = somma + item
    return somma
#Somma tutti i valori presenti nella lista Values
print("Le vendite totali degli Shampoo ammontano a: {0:.2f}".format(somma(values)))