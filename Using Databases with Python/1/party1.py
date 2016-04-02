class PartyAnimal:

	x = 10

	def party(self):
		self.x = self.x + 1
		print "So far", self.x

an = PartyAnimal()

an.party()

print "Type", type(an)
print "Dir", dir(an)