#===========================================================
# Classe Model (Valutazione di un Modello Lezione 10)
#===========================================================


class Model(object):

	def fit (self, data):
		pass

	def predict(self):
		pass


class IncrementModel(Model):

	def fit (self, data):
		raise NotImplementedError('Questo modello non prevede un fit')

	def predict(self, prev_months):

		# Se prev_months non è una lista sollevo un eccezione
		if not isinstance(prev_months, list):
			raise Exception ("L'argomento prev_months deve essere una lista di valori")

		# Se i dati contenuti in prev_months non sono interi o float, sollevo un eccezione
		for item in prev_months :
			if type(item) == float or type(item) == int:
				pass
			else:
				raise Exception ('I valori contenuti in prev_months devono essere interi o float')
				
		# Se prev_months contiene più di tre valori prendo gli utlime tre
		if len(prev_months) > 3:
			last_three_months = prev_months[-3:]
		
		# Se prev_months è inferiore a 3 elementi sollevo un eccezione
		elif len(prev_months) < 3:
			raise Exception('prev_months per la predizione del mese t+1 deve contenere almeno tre elementi')
		
		# Se prev_months contiene precisamente 3 elementi
		else:
			last_three_months = prev_months

		# Dichiaro una variabile di supporto per calcolare l'incremento medio
		total_increment = 0
		
		# Dichiaro una variabile che parta dall'ultimo valore della lista
		i = -1 
		
		# Dichiaro una variabile per i possibili confronti tra elementi
		compare = (len(last_three_months)-1) 

		# Fino a quando ci sono elementi nella lista 
		while compare > 0 :
	
			# Faccio la differenza tra l'ultimo elemento e il penultimo
			increment_months = last_three_months[i] - last_three_months[i-1]

			# Questa differenza (incremento mensile) lo aggiungo al totale degli incrementi
			total_increment += increment_months
	
			# Mi sposto sull'elemento precedente
			i-=1

			# Tolgo un elemento dalla lista
			compare-=1

		# Calcolo la media dell'incremento
		media = total_increment/(len(last_three_months)-1)

		# Calcolo la predizione del mese t+1
		prediction = last_three_months[-1] + media  
       
		return prediction


class FittableIncrementModel(Model):


	def fit(self, data):

		# Se data non è una lista sollevo un eccezione
		if not isinstance(data, list):
			raise Exception ("L'argomento prev_months deve essere una lista di valori")

		# Se i dati sono minori di due sollevo un eccezione
		if len(data) < 2:
			raise Exception ('Il dataset non contiene abbastanza elementi per fare il fit con i dati storici')

		# Se i dati contenuti in sdata non sono interi o float, sollevo un eccezione
		for item in data :
			if type(item) == float or type(item) == int:
				pass
			else:
				raise Exception ('I valori contenuti in data devono essere interi o float')
				
		# Dichiaro una variabile di supporto per calcolare l'incremento medio
		total_increment = 0
		
		# Dichiaro una variabile che parta dall'ultimo valore della lista
		i = -1 
		
		# Dichiaro una variabile per i possibili confronti tra elementi
		compare = (len(data)-1) 

		# Fino a quando ci sono elementi nella lista 
		while compare > 0 :
	
			# Faccio la differenza tra l'ultimo elemento e il penultimo
			increment_months = data[i] - data [i-1]

			# Questa differenza (incremento mensile) lo aggiungo al totale degli incrementi
			total_increment += increment_months
	
			# Mi sposto sull'elemento precedente
			i-=1

			# Tolgo un elemento dalla lista
			compare-=1

		# Calcolo la media dell'incremento
		self.fit_prediction = total_increment/(len(data)-1)


       

	def predict(self, prev_months):

		# Se prev_months non è una lista sollevo un eccezione
		if not isinstance(prev_months, list):
			raise Exception ("L'argomento prev_months deve essere una lista di valori")

		# Se i dati contenuti in prev_months non sono interi o float, sollevo un eccezione
		for item in prev_months :
			if type(item) == float or type(item) == int:
				pass
			else:
				raise Exception ('I valori contenuti in prev_months devono essere interi o float')
				
		# Se prev_months contiene più di tre valori prendo gli utlime tre
		if len(prev_months) > 3:
			last_three_months = prev_months[-3:]
		
		# Se prev_months è inferiore a 3 elementi sollevo un eccezione
		elif len(prev_months) < 3:
			raise Exception('prev_months per la predizione del mese t+1 deve contenere almeno tre elementi')
		
		# Se prev_months contiene precisamente 3 elementi
		else:
			last_three_months = prev_months

		# Dichiaro una variabile di supporto per calcolare l'incremento medio
		total_increment = 0
		
		# Dichiaro una variabile che parta dall'ultimo valore della lista
		i = -1 
		
		# Dichiaro una variabile per i possibili confronti tra elementi
		compare = (len(last_three_months)-1) 

		# Fino a quando ci sono elementi nella lista 
		while compare > 0 :
	
			# Faccio la differenza tra l'ultimo elemento e il penultimo
			increment_months = last_three_months[i] - last_three_months[i-1]

			# Questa differenza (incremento mensile) lo aggiungo al totale degli incrementi
			total_increment += increment_months
	
			# Mi sposto sull'elemento precedente
			i-=1

			# Tolgo un elemento dalla lista
			compare-=1

		# Calcolo la media dell'incremento
		prediction = total_increment/(len(last_three_months)-1)


		return (prev_months[-1] + (prediction + self.fit_prediction)/2)
       


#====================
# Corpo del programma
#====================

mylist = [8,19,31,41,50,52,60]
second_list = [289.9, 421.6, 264.5,]

shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]


# Setto il punto di divisione tra i dati di training e test set
train_test_cutoff = 24

# Ricavo la lunghezza del test set che mi sevrira' dopo
test_set_len = len(shampoo_sales)-train_test_cutoff

# Imposto la finestra usata per il predict (quanti prev_months)
window = 3

# Istanzio il modello senza fit
increment_model = IncrementModel()

# Istanzio il modello con fit e chiamata alla funzione fit
fittable_increment_model = FittableIncrementModel()
fittable_increment_model.fit(shampoo_sales[0:train_test_cutoff])

# Metto entrambi i modelli in una lista
models = [increment_model, fittable_increment_model]

# Swicth per il plot
plot = False

for model in models:

    error_sum = 0
    print('') # Lascio una riga bianca
    print('Sto valutando il modello "{}"'.format(model))

    # Lista di supporto
    predictions = []
    
    # Cicolo sul test set
    for i in range(test_set_len):
        
        # Calcolo gli indici di inizio e fine della finestra che uso per la predizione per l'indice "i" del test set
        window_start =  train_test_cutoff+i-window-1
        window_end = train_test_cutoff+i-1
        
        # Chiamo il predict e aggiungo al predizione alle predizioni (che mi serviranno tutte assieme in caso voglia graficarle)
        prediction = model.predict(shampoo_sales[window_start:window_end])
        predictions.append(prediction)
        
        # Stampo qualche informazione su cosa sta succedendo
        print('"{}" vs "{}"'.format(int(prediction), int(shampoo_sales[train_test_cutoff+i])))

        # Calcolo l'erorre tra il valore reale e quello della predizione e lo aggiungo alla somma degli errori
        error_sum += abs(prediction - shampoo_sales[train_test_cutoff+i])
    
    # Calclolo la media dell'errore
    error = error_sum / test_set_len

    print('Errore medio: "{}"'.format(error))

    # Scommentate le righe qui sotto se volete vedere i plot. Siccome non tutti gli ambienti 
    # supportano il plot, ho preferito disabilitirle i plot commentandole "di default"
    #from matplotlib import  pyplot
    #pyplot.plot(shampoo_sales[0:24] + predictions, color='tab:red')
    #pyplot.plot(shampoo_sales, color='tab:blue')
    #pyplot.show()






