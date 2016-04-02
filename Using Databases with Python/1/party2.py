# The constructor and destructor are optional.
# The constructor is typically used to set up variables.
# The destructor is seldom used.

# class PartyAnimal:
# 	x = 0

# 	def __init__(self):                 #constructed
# 		print "I am constructed", self.x

# 	def party(self):
# 		self.x = self.x + 1
# 		print "So far", self.x

# 	def __del__(self):                  #destructed
# 		print "I am destructed", self.x

# an = PartyAnimal()
# an.party()
# an.party()
# an.party()

class PartyAnimal:
	x = 0
	name = ""

	def __init__(self, z):
		self.name = z
		print self.name, "constructed"

	def party(self):
		self.x = self.x + 1
		print self.name, "party count", self.x

class FooballFan(PartyAnimal):
	points = 0

	def touchdown(self):
		self.points = self.points + 7
		self.party()
		print self.name, "points", self.points

s = PartyAnimal("Sally")
s.party()

j = FooballFan("Jim")
j.party()
j.touchdown()



















