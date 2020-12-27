# 1 - Modificate l oggetto CSVFile della lezione precedente in modo che dia un messaggio d'errore se si cerca di aprire un file non esistente.
# 2 - Aggiungete i campi al file "shampoo_sales.csv" -> "shampoo_sales2.csv" e gestite gli errori che verranno generati in modo che le linee vengano saltate ma che venga stampato a schermo errore

#Creo un oggetto CSVFile
class CSVFile():

    # Inizializzo l'oggetto con il nome del file - attributo contiene 'name'
    def __init__(self, name):
        self.name = name

    #Creo un metodo get_data che torni i dati dal file CSV
    def get_data(self):
        # Creo una lista vuota dove aggiungere tutti gli elementi del file
        elements_list = []
        # Creo una lista vuota dove aggiungere tutti i valori del file
        values_list = []
        #Creo una lista vuota dove aggiungere tutti gli errori di conversione da elementi a float
        error_list =[]

        # Tento di aprire file
        try:
            mio_file = open(self.name, 'r')
        # Gestisco l'errore se il nome del file e errato/inesistente
        except:
            from sys import exit
            print('*ERRORE* Il file che si sta tentando di aprire è inesistente -> immettere un file esitente')
            exit()

        # Aggiungo tutti gli elementi del file alla lista vuota (all'interno della riga li separo sulla virgola)
        for line in mio_file:
            elements_list.extend(line.split(','))
        # Se il valore puo essere convertito in un float lo aggiungo alla lista valori, altrimento lo inserisco nella lista errore
        for item in elements_list:
            try:
                values_list.append(float(item))
            except:
                error_list.append(item)
        # Stampo la lista errori
        print(f'La lista degli elementi che non sono riuscito a convertire e : {error_list}\n\n')
        return (f'La lista dei valori delle vendite degli shampoo è: {values_list}')

myfile = CSVFile('shampoo_sales.csv')
print(myfile.name)
print(myfile.get_data())