
# class PartyAnimal 
class PartyAnimal:

	x = 10

	def party(self):
		self.x = self.x + 1
		print "So far", self.x

	def brark1(self):
		print "gua gua gua"

	def brakr2(self):
		print "mmiau mmiau mmiau"

an = PartyAnimal() # create object

an.party() # use to method party

print "Type", type(an)
print "Dir", dir(an)

an.party()
an.brark1()
an.brakr2()

