class Restas:
	def __init__(self,divisor,dividendo):
		self.divisor = float(divisor)
		self.dividendo = float(dividendo)
	def division(self):
		bucles = 0
		decimal = 0.0
		dividendo = self.dividendo
		divisor = self.divisor
		if divisor == 0:
			print "Imposible Dividir por 0"
		if dividendo < divisor:
			print "El dividendo debe ser mayor al divisor"

		while (dividendo >= divisor):
			dividendo = dividendo - divisor
			bucles = bucles + 1
		
		decimal = ((dividendo*100)/divisor)
		print "Bucles Utilizados %d",bucles,dividendo,decimal
		
restar = Restas(6,10)
restar.division()
