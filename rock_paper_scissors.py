import random


class Game(): 
    def __init__(self):
        self.player_score = 0
        self.cpu_score = 0
        self.weapons = ['rock', 'paper', 'scissors']
        self.cpu_move = None
        self.player_move = None
    
    def run(self):
        running = True
        while running:
            #getting the machine and player move
            self.cpu_move = self.weapons[random.randint(0, len(self.weapons)-1)]
            print('Please type rock, paper or scissors')
            self.get_move = input().lower()   
            if self.get_move in self.weapons:
                self.player_move = self.get_move         
            else:
                print('invalid choice!') 
                continue
            #checking who wins the round
            if self.player_move == 'rock' and self.cpu_move == 'paper':
                print('The machine uses paper, you lose')
                self.cpu_score += 1
                print('Your score is: ', self.player_score)
                print('The machine\'s score is: ', self.cpu_score)
            if self.player_move == 'paper' and self.cpu_move == 'rock':
                print('The machine uses rock , you win')
                self.player_score += 1
                print('Your score is: ', self.player_score)
                print('The machine\'s score is: ', self.cpu_score)
            if self.player_move == 'rock' and self.cpu_move == 'rock':
                print('The machine uses rock, it is a tie')
                print('Your score is: ', self.player_score)
                print('The machine\'s score is: ', self.cpu_score)
            if self.player_move == 'paper' and self.cpu_move == 'paper':
                print('The machine uses paper, it is a tie')
                print('Your score is: ', self.player_score)
                print('The machine\'s score is: ', self.cpu_score)
            if self.player_move == 'scissors' and self.cpu_move == 'scissors':
                print('The machine uses scissors, it is a tie')
                print('Your score is: ', self.player_score)
                print('The machine\'s score is: ', self.cpu_score)
            if self.player_move == 'paper' and self.cpu_move == 'scissors':
                print('The machine uses scissors , you lose')
                self.cpu_score += 1
                print('Your score is: ', self.player_score)
                print('The machine\'s score is: ', self.cpu_score)
            if self.player_move == 'scissors' and self.cpu_move == 'paper':
                print('The machine uses paper , you win')
                self.player_score += 1
                print('Your score is: ', self.player_score)
                print('The machine\'s score is: ', self.cpu_score)
            if self.player_move == 'scissors' and self.cpu_move == 'rock':
                print('The machine uses rock , you lose')
                self.cpu_score += 1
                print('Your score is: ', self.player_score)
                print('The machine\'s score is: ', self.cpu_score)
            if self.player_move == 'rock' and self.cpu_move == 'scissors':
                print('The machine uses scissors , you win')
                self.player_score += 1
                print('Your score is: ', self.player_score)
                print('The machine\'s score is: ', self.cpu_score)
            
            #Checking who wins and if the player wants to play again
            again = None
            if self.player_score == 3:
                print('Congratulations, you have beaten the machine!')
                again = self.play_again()
                if again == False:
                    running = False
                    return False
                else:
                    self.player_score = 0
                    self.cpu_score = 0
                    continue
            elif self.cpu_score == 3:
                print('You ran out of attemps, the machine wins!')
                again = self.play_again()
                if again == False:
                    running = False
                    return False
                else:
                    self.player_score = 0
                    self.cpu_score = 0
                    continue

    
    def play_again(self):
        print('do you want to play again? (yes or no)')
        r = input()
        if r.lower().startswith('y'):
            return True
        else:
            print('Ok, thank you for playing!')
            return False
    
   
            

main_game = Game()         



def main():
    print('Hi, Welcome to Rock, Paper and scissors, do you want to play? (yes or no)')
    answer = input()
    if answer.lower().startswith('y'):
        run = main_game.run()
        if run == False:
            return False
    else:
        print('ok, see you soon')
        return False

while True:
    game = main()
    if game == False:
        break