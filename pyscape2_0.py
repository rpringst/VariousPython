xpcurve = { 1 : 150.0,
			2 : 450.0,
			3 : 1050.0 }

metals = { 'copper' : [1, 15.0],
		   'silver' : [2, 25.0],
		   'gold' : [3, 45.0] }

class Inventory:
	def __init__(self, items={}):
		self.items = items

class Skill:
	def __init__(self, resource, xp=0.0, level=1, invent=Inventory()):
		self.resource = resource
		self.xp = xp
		self.level = level
		self.invent = invent
	def gatherResource(self, kind):
		if self.resource[kind][0] > self.level:
			return
		else:
			self.xp += self.resource[kind][1]
			if kind in self.invent.items: self.invent.items[kind] += 1
			else: self.invent.items[kind] = 1
			if xpcurve[self.level] <= self.xp:
				self.level += 1
				
class Player:
	def __init__(self, skills, invent=Inventory()):
		self.invent = inventory
		self.skills = skills

inventory = Inventory({'copper' : 3})
mining = Skill(metals, invent=inventory)
player = Player(invent=Inventory, skills={'mining' : mining})

player.skills['mining'].gatherResource('copper')
print(player.skills['mining'].xp)
player.skills['mining'].gatherResource('copper')
print(player.skills['mining'].xp)
mining.gatherResource('silver')
print(player.skills['mining'].xp)
for i in range(8):
	player.skills['mining'].gatherResource('copper')
	print(player.skills['mining'].xp)
mining.gatherResource('silver')
print(player.skills['mining'].xp)
print(player.invent.items['copper'])
