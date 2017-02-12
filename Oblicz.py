class Wielokat:
	def __init__(self):
		self.wierzcholki = []
		self.iloscWierzcholkow = 0

	def ustaw_wierzcholki(self, lista = []):
		if (lista == []):
			ilosc = int(raw_input("Podaj ilosc wierzcholkow: "))
			self.wierzcholki = []
			for i in range(ilosc):
				x = float(raw_input("Podaj x {:d} wierzcholka: ".format(i+1)))
				y = float(raw_input("Podaj y {:d} wierzcholka: ".format(i+1)))
				self.wierzcholki.append([x,y])
		else:
			self.wierzcholki = lista
		self.iloscWierzcholkow = len(self.wierzcholki)	
		if (self.iloscWierzcholkow < 3):
			print "Za malo wierzcholkow"
			return -1

		return 1

	def oblicz_pole(self):
		pole = 0.
		for i in range(self.iloscWierzcholkow):
			temp = self.wierzcholki[(i+1)%self.iloscWierzcholkow][1]
			temp2 = self.wierzcholki[(i-1)%self.iloscWierzcholkow][1]
			pole += self.wierzcholki[i][0] * (temp2 - temp)
		pole = abs(pole)*(0.5)
		return pole

