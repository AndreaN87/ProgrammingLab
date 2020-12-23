# Scrivete uno script che sommi tutti i valori delle vendite degli shampoo del file "shampoo_sales.csv". Poi, committate il file in cui l'avete scritto

#Dichiaro una variabile vuota
element_list = []
float_list = []

#Apro il file
file = open('shampoo_sales.csv', 'r')

#Per ogni riga del file splitto sulla virgola
for line in file:
    element = line.split(',')
    #Inserisco ogni elemnteo del file nella lista vuota
    for item in element:
        element_list.extend(element)
    # Se l'elemento è convertibile in float lo aggiungo ad una lista
    try:
        float_list.append(float(item))
    except ValueError:
        pass
# Sommo i valori delle vendite
total_sales = sum (float_list)
#Stampo il totale delle vendite arrotondado le cifre decimali
print(f'Il totale delle vendite ammonta a:{round(total_sales,2)}')