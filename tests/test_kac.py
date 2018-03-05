from utils import *

def test_dark_pact():
	game = prepare_game()
	vulgar = game.player1.give("LOOT_013").play()
	pact = game.player1.give('LOOT_017')
	assert game.player1.hero.health == 28
	pact.play(target=vulgar)
	assert game.player1.hero.health == 30

def test_psychic_scream():
	game = prepare_game()
	decksize = len(game.player1.deck)
	wisp1 = game.player1.give(WISP).play()
	wisp2 = game.player1.give(WISP).play()
	wisp3 = game.player1.give(WISP).play()
	wisp4 = game.player1.give(WISP).play()
	wisp5 = game.player1.give(WISP).play()
	wisp6 = game.player1.give(WISP).play()
	wisp7 = game.player1.give(WISP).play()
	game.end_turn()
	
	wisp8 = game.player2.give(WISP).play()
	wisp9 = game.player2.give(WISP).play()
	wisp10 = game.player2.give(WISP).play()
	wisp11 = game.player2.give(WISP).play()
	wisp12 = game.player2.give(WISP).play()
	wisp13 = game.player2.give(WISP).play()
	wisp14 = game.player2.give(WISP).play()
	assert len(game.player1.field)==7
	assert len(game.player2.field)==7
	game.player2.give("LOOT_008").play()
	assert len(game.player1.field)==0
	assert len(game.player2.field)==0
	assert len(game.player1.deck)==decksize+14

def test_vulgar_homunculus():
	game = prepare_game()
	assert game.player1.hero.health == 30
	game.player1.give("LOOT_013").play()
	assert game.player1.hero.health == 28

