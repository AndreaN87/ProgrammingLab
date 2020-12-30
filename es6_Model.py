#=================================================
# Classe Model (Creazione di un modello Lezione 8)
#=================================================


# Creo una Superclasse Modello
class Model():

	# Inizzializzo la classe con una lista dati
	def __init__ (self, dataset):
		self.dataset = dataset

		# Se dataset non è una lista sollevo un eccezione
		if type(dataset) != list:
			raise Exception ("L'argomento dataset deve essere una lista di valori")

		# Se i dati contenuti in dataset non sono interi o float, sollevo un eccezione
		for item in dataset:
			if type(item) == float or type(item) == int:
				pass
			else:
				raise Exception ('I valori nel dataset devono essere interi o float')

	#  Definisco un metodo che calcoli l'incremento totale
	def compute_avg_increment (self, dataset):
		
		# Dichiaro una varaibile che contenga l'incremento totale, una per calcolare l'incremento da mese a mese ed una per lo stop del ciclo while.
		total_increment = 0
		i = -1
		item = (len(dataset)-1)

		# Fino a quando ci sono elementi nella lista 
		while item > 0 :
	
			# Faccio la differenza tra l'ultimo elemento e il penultimo
			increment_months = dataset[i] - dataset[i-1]

			# Questa differenza (incremento mensile) lo aggiungo al totale degli incrementi
			total_increment += increment_months
	
			# Mi sposto sull'elemento precedente
			i-=1

			# Tolgo un elemento dalla lista
			item-=1

		# Calcolo la media dell'incremento
		media = total_increment/(len(dataset)-1)

		# Istanzio la media cosi da poterla richiamare successivamente
		self.media = media

		return media



# Creo una sottoclasse per il calcolo degli incrementi
class IncrementModel(Model):

	# Definisco un metodo per il calcolo della media degli incrementi sui dati precedenti alle ultime tre mensilità
	def fit(self):

		# Se dataset contiene più di quattro valori prendo i dati storici
		# Se i dati fossero quattro avrei solo un valore come dato storico pertanto non potrei calcolare un incremento
		if len(self.dataset) > 4:
			historical_months = self.dataset[:-3]
		
		# Se i dati sono minori o uguali a quattro sollevo un eccezione
		if len(self.dataset) <= 4:
			raise Exception ('Il dataset non contiene abbastanza elementi per fare il fit con i dati storici')
			pass

		
		# Calcolo la media degli incrementi
		avg_historical_increment = self.compute_avg_increment(historical_months)

		#Istanzio la media cosi da poterla richiamare successivamente		
		self.avg_historical_increment = avg_historical_increment

		# Calcolo la predizione del mese t+1
		next_months_predict = self.dataset[-1] + ((avg_historical_increment+self.avg_three_months_increment)/2)

		return next_months_predict	

	# Definisco un metodo per il calcolo della media degli incrementi sulle ultime tre mensilità
	def predict(self):

		# Se dataset contiene più di tre valori prendo gli utlime tre
		if len(self.dataset) > 3:
			last_three_months = self.dataset[-3:]
		
		# Se dataset è inferiore a 3 elementi sollevo un eccezione
		elif len(self.dataset) < 3:
			raise Exception('Il dataset per la predizione del mese t+1 deve contenere almeno tre elementi')
		
		# Se dataset contiene precisamente 3 elemnti
		else:
			last_three_months = self.dataset

		# Calcolo la media degli incrementi
		avg_three_months_increment = self.compute_avg_increment(last_three_months)

		#Istanzio la media cosi da poterla richiamare successivamente		
		self.avg_three_months_increment = avg_three_months_increment

		# Calcolo la predizione del mese t+1
		next_months_predict = self.dataset[-1] +avg_three_months_increment 
       
		return next_months_predict

	# Definisco un metodo per il calcolo della media degli incrementi sulle mensilità totali
	def total(self):

		increment_total_months = self.dataset[-1] + self.media 

		return increment_total_months







#====================
# Corpo del programma
#====================

sales_shampoo = IncrementModel([8,19,31,41,50,52,60])

print (f"Previsione del mese t+1 (Media incrementi ultimi 3 mesi)\nt+1: {sales_shampoo.predict()}")
print (f"Previsione del mese t+1 ( Media incrementi mesi precedenti + Media incrementi ultimi 3 mesi)\nt+1: {sales_shampoo.fit()}")
print (f"Previsione del mese t+1 (totale dei dati)\nt+1: {round(sales_shampoo.total(),1)}")