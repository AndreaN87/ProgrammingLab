#==================================================
# Esercizio classe CSVFile con argomenti star e end
#==================================================

class CSVFile:

    def __init__(self, name):

        #Setto il nome del file
        self.name = name

        # Sollevo un eccezione se il nome del file inserito non è una stringa
        if self.name != str(self.name):
            raise Exception ('Errore -> il nome del file inserito "{}", non appartiene al tipo stringa ma appartiene al tipo {}'.format(self.name, type(self.name)))


    def get_data(self, start = None, end = None):
       
        # Inizializzo una lista vuota per salvare i valori
        values = []
        
        # Provo ad aprire il file per estrarre i dati. 
        try:
            file = open(self.name)

            # Leggo e restuisce l’intero contenuto del file come lista di righe
            list_lines = file.readlines()

            # Chiudo il file
            file.close()

            # Leggo quante righe contiene il file
            total_lines = len(list_lines)

            # Se ho dei valori in start o in end...
            if start != None or end != None:

                # Se l'assegnazione dell'argomento e solo per start o per end sollevo un eccezione
                if start != None and end == None or start == None and end != None:
                    raise Exception("L'argomento start o end non sono stati assegnati")

                    # Esco dalla funzione tornando "niente"
                    return None
                
                # Se l'argomento end è inferiore a start sollevo un eccezione
                if end <= start:
                    raise Exception("L'argomento end non puo' essere inferiore a start, se end è uguale a start si rammenta che che il valore inserito in end è ESCLUSO") 

                    # Esco dalla funzione tornando "niente"
                    return None

                # Se start è minore di 1 sollevo un eccezione
                if start < 1:
                    raise Exception("L'argomento start non puo' essere inferiore a 1 in quanto prima di questo valore non ci sono dati ma intestazioni di file non convertibili") 
                
                    # Esco dalla funzione tornando "niente"
                    return None

                # Se end supera il totale delle righe del file alzo un eccezzione
                if end > total_lines:
                    raise Exception("L'argomento end non puo' essere maggiore delle righe del file. Il file contiene {} righe".format(total_lines))

                    # Esco dalla funzione tornando "niente"
                    return None

                # Estraggo i dati dalla linea start alla linea end
                my_file = list_lines[start:end]

            # Se gli argomenti start e end non sono definiti
            else:
                my_file = list_lines

        # Se non riesco ad aprire il file avverto dell'errore e abbortisco.
        except Exception as e:

            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))

            # Esco dalla funzione tornando "niente"
            return None

        # Ora inizio a leggere il file linea per linea
        for line in my_file:

            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')
            
            # Se non sto processando l'intestazione ...
            if elements[0] != 'Date':

                # Setto la data ed il valore
                date = elements[0]
                value = elements[1]
              
                # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo,
                # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
                # un errore "recoverable", posso proseguire (sempolicemente salto linea).
                try:
                    value = float(value)
                except Exception as e:

                    # Stampo l'errore
                    print('Errore nella conversione a float: "{}"'.format(e))

                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue

                # Infine aggiugni alla lista dei valori questo valore
                values.append(value)

        # Quando ho processato tutte le righe, ritorno i valori
        return values


#====================
# Corpo del programma
#====================

mio_file = CSVFile(name = 'shampoo_sales.csv')

print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))

