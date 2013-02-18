class Restas:
	def __init__(self,divisor,dividendo):
		self.divisor = float(divisor)
		self.dividendo = float(dividendo)
	def division(self):
		self.getInfoDivi()
		bucles = 0
		dividendo = self.dividendo
		divisor = self.divisor
		if divisor == 0:
			print "Imposible Dividir por 0"
		if dividendo < divisor:
			print "El dividendo debe ser mayor al divisor"

		while (dividendo >= divisor):
			dividendo = dividendo - divisor
			bucles = bucles + 1
		

		print "Cosciente: ",bucles
		print "Reciduo: ", dividendo
	def getInfoDivi(self):
		print str(self.dividendo) + " / " + str(self.divisor)
		
restar = Restas(6,10)
restar.division()
