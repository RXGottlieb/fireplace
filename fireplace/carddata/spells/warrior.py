import random
from fireplace.enums import Zone
from ..card import *


# Charge
class CS2_103(Card):
	action = buffTarget("CS2_103e2")

class CS2_103e2(Card):
	Atk = 2
	Charge = True


# Rampage
class CS2_104(Card):
	action = buffTarget("CS2_104e")

class CS2_104e(Card):
	Atk = 3
	Health = 3


# Heroic Strike
class CS2_105(Card):
	action = buffSelf("CS2_105e")

class CS2_105e(Card):
	Atk = 4


# Execute
class CS2_108(Card):
	action = destroyTarget


# Cleave
class CS2_114(Card):
	def action(self):
		targets = random.sample(self.controller.opponent.field, 2)
		for target in targets:
			self.hit(target, 2)


# Slam
class EX1_391(Card):
	def action(self, target):
		self.hit(target, 2)
		if target.zone == Zone.PLAY:
			self.controller.draw()


# Battle Rage
class EX1_392(Card):
	def action(self):
		for target in self.controller.getTargets(TARGET_FRIENDLY_CHARACTERS):
			if target.damage:
				self.controller.draw()


# Whirlwind
class EX1_400(Card):
	def action(self):
		for target in self.controller.getTargets(TARGET_ALL_MINIONS):
			self.hit(target, 1)


# Brawl
class EX1_407(Card):
	def action(self):
		board = self.controller.getTargets(TARGET_ALL_MINIONS)
		for minion in random.sample(board, len(board) - 1):
			minion.destroy()


# Mortal Strike
class EX1_408(Card):
	def action(self, target):
		self.hit(target, 6 if self.controller.hero.health <= 12 else 4)


# Upgrade!
class EX1_409(Card):
	def action(self):
		if self.controller.hero.weapon:
			self.controller.hero.weapon.buff("EX1_409e")
			self.controller.hero.weapon.durability += 1
		else:
			self.controller.summon("EX1_409t")

class EX1_409e(Card):
	Atk = 1


# Shield Slam
class EX1_410(Card):
	def action(self, target):
		self.hit(target, self.controller.hero.armor)


# Shield Block
class EX1_606(Card):
	def action(self):
		self.controller.hero.armor += 5
		self.controller.draw()


# Inner Rage
class EX1_607(Card):
	def action(self, target):
		target.buff("EX1_607e")
		self.hit(target, 1)

class EX1_607e(Card):
	Atk = 2
