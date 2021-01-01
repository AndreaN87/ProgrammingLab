#=================================================
# Classe Model (Creazione di un modello Lezione 8)
#=================================================


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
		if type(prev_months) != list:
			raise Exception ("L'argomento dataset deve essere una lista di valori")

		# Se i dati contenuti in prev_months non sono interi o float, sollevo un eccezione
		for item in prev_months :
			if type(item) == float or type(item) == int:
				pass
			else:
				raise Exception ('I valori nel dataset devono essere interi o float')
				
		# Se prev_months contiene più di tre valori prendo gli utlime tre
		if len(prev_months) > 3:
			last_three_months = prev_months[-3:]
		
		# Se prev_months è inferiore a 3 elementi sollevo un eccezione
		elif len(prev_months) < 3:
			raise Exception('Il dataset per la predizione del mese t+1 deve contenere almeno tre elementi')
		
		# Se prev_months contiene precisamente 3 elemnti
		else:
			last_three_months = prev_months

		# Dichiaro  tre variabili, una che contenga l'incremento totale, una per calcolare l'incremento da mese a mese ed una per lo stop del ciclo while.
		total_increment = 0
		i = -1
		item = (len(prev_months)-1)

		# Fino a quando ci sono elementi nella lista 
		while item > 0 :
	
			# Faccio la differenza tra l'ultimo elemento e il penultimo
			increment_months = prev_months[i] - prev_months[i-1]

			# Questa differenza (incremento mensile) lo aggiungo al totale degli incrementi
			total_increment += increment_months
	
			# Mi sposto sull'elemento precedente
			i-=1

			# Tolgo un elemento dalla lista
			item-=1

		# Calcolo la media dell'incremento
		media = total_increment/(len(prev_months)-1)


		# Calcolo la predizione del mese t+1
		prediction = prev_months[-1] + media  
       
		return prediction


#====================
# Corpo del programma
#====================

mylist = [50,52,60]
sales_shampoo = IncrementModel()
print (f"Previsione del mese t+1 (Media incrementi ultimi 3 mesi)\nt+1: {round(sales_shampoo.predict(mylist),1)}")
