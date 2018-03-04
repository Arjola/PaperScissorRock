class Game:
	def __init__(self, newPlayerName, emri2 ):
		self.playerName = newPlayerName
		self.emri2 = emri2
		self.playerHand = "NA"
		self.botHand = "NA"
		self.winner = "No winner yet"
		print("New instance of game class for " + self.playerName)
		
	def runGame(self):
		if ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 'Scissors'):
			self.winner = self.playerName +' wins'
		elif ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 'Rock'):
			self.winner = 'You guys tie.'
		elif ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 'Paper'):
			self.winner =  self.emri2 + ' wins.'
		elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 'Scissors'):
			self.winner = self.emri2 + ' wins.'
		elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 'Rock'):
			self.winner = self.playerName +' wins'
		elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 'Paper'):
			self.winner = 'You tie.'
		elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 'Scissors'):
			self.winner = 'You tie.'
		elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 'Rock'):
			self.winner = self.emri2 + ' wins.'
		elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 'Paper'):
			self.winner = self.playerName +' wins'
		else:
			self.winner = 'INVALID input, try again'

		
		
def main():
	player_1 = input('Enter the Name of Player 1:  ')
	player_2 = input('Enter the Name of Player 2:   ')
	
	myGame = Game(player_1, player_2 )
	
	Player1_input = input(player_1 +', enter your tool: ')
	Player2_input = input(player_2 +', enter your tool: ')
	
	myGame.playerHand = str(Player1_input)
	myGame.botHand = str(Player2_input)
	myGame.runGame()
	print(myGame.winner)
	
main()