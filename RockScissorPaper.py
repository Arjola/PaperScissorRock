class Game:
	def __init__(self, newPlayerName, emri2 ):
		self.playerName = newPlayerName
		self.emri2 = emri2
		self.player1Hand = "NA"
		self.player2Hand = "NA"
		self.winner = "No winner yet"
		print("New instance of game class for " + self.playerName)
		
	def runGame(self):
		if ((self.player1Hand == 'rock' or self.player1Hand == 'Rock') and (self.player2Hand == 'Scissors' or self.player2Hand == 'scissors')):
			self.winner = self.playerName +' wins'
		elif ((self.player1Hand == 'rock' or self.player1Hand == 'Rock') and (self.player2Hand == 'Rock' or self.player2Hand == 'rock')):
			self.winner = 'You guys tie.'
		elif ((self.player1Hand == 'rock' or self.player1Hand == 'Rock') and (self.player2Hand == 'Paper' or self.player2Hand == 'paper')):
			self.winner =  self.emri2 + ' wins.'
		elif ((self.player1Hand == 'paper' or self.player1Hand == 'Paper') and (self.player2Hand == 'Scissors'or self.player2Hand == 'scissors')):
			self.winner = self.emri2 + ' wins.'
		elif ((self.player1Hand == 'paper' or self.player1Hand == 'Paper') and (self.player2Hand == 'Rock' or self.player2Hand == 'rock')):
			self.winner = self.playerName +' wins'
		elif ((self.player1Hand == 'paper' or self.player1Hand == 'Paper') and (self.player2Hand == 'Paper' or self.player2Hand == 'paper')):
			self.winner = 'You tie.'
		elif ((self.player1Hand == 'scissors' or self.player1Hand == 'Scissors') and (self.player2Hand == 'Scissors'or self.player2Hand == 'scissors')):
			self.winner = 'You tie.'
		elif ((self.player1Hand == 'scissors' or self.player1Hand == 'Scissors') and (self.player2Hand == 'Rock' or self.player2Hand == 'rock')):
			self.winner = self.emri2 + ' wins.'
		elif ((self.player1Hand == 'scissors' or self.player1Hand == 'Scissors') and (self.player2Hand == 'Paper' or self.player2Hand == 'paper')):
			self.winner = self.playerName +' wins'
		else:
			self.winner = 'INVALID input, try again'

		
		
def main():
	player_1 = input('Enter the Name of Player 1:  ')
	player_2 = input('Enter the Name of Player 2:   ')
	
	myGame = Game(player_1, player_2 )
	
	Player1_input = input(player_1 +', enter your tool: ')
	Player2_input = input(player_2 +', enter your tool: ')
	
	myGame.player1Hand = str(Player1_input)
	myGame.player2Hand = str(Player2_input)
	myGame.runGame()
	print(myGame.winner)
	
main()