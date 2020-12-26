# Create un oggetto CSVFile che rappresenti un file CSV. e che:
# 1 - venga inizializzata sul nome del file CSV
# 2 - abbia un attributo "name" che ne contenga il nome
# 3 - abbia un metodo "get_data" che torni i dati dal file CSV come numeri di una lista.
# PROVATELO SUL FILE "shampoo_sales.csv"



#Creo un oggetto CSVFile
class CSVFile():

    # Inizializzo l'oggetto con il nome del file - l'attributo contiene 'name'
    def __init__(self, name):
        self.name = name

    #Creo un metodo get_data che torni i dati dal file CSV
    def get_data(self):
        # Creo una lista vuota dove aggiungere tutti gli elementi del file
        elements_list = []
        # Creo una lista vuota dove aggiungere tutti i valori del file
        values_list = []
        # Apro il file
        mio_file = open(self.name, 'r')
        # Aggiungo tutti gli elementi del file alla lista vuota (all'interno della riga li separo sulla virgola)
        for line in mio_file:
            elements_list.extend(line.split(','))
        # Se il valore può essere convertito in un float lo aggiungo alla lista valori, altrimento lo scarto
        for item in elements_list:
            try:
                values_list.append(float(item))
            except ValueError:
                pass
        return values_list

myfile = CSVFile('shampoo_sales.csv')
print(myfile.name)
print(myfile.get_data())