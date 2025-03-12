# import moudles that are needed
from random import choice
from time import sleep

#import lists
from F1Drivers import HistoricDriversList, CurrentDriversList
from F1Teams import HistoricalTeamsList, CurrentTeamsList

from FormulaGraphic import graphic

# set up dictionary
dictionary = CurrentDriversList + HistoricDriversList + CurrentTeamsList + HistoricalTeamsList
CurrentList = CurrentDriversList + CurrentTeamsList
HistoricList = HistoricDriversList + HistoricalTeamsList

# set up varables needed
player_score = 0
computer_score = 0
exit = False

# set up functions
def hedgeman(hangman):
  print(graphic[hangman])
  return
# end function

def start():
  print('Lets play a game of hangman')
  while game():
    pass
# end fuunction

# main game(not main code)
def game():
  word = choice(dictionary)
  word_length = len(word)
  clue = word_length * ['_']
  tries = len(graphic) - 1
  guesses_left = len(graphic) - 1
  letters_tried = ''
  x = 0
  letters_wrong = 0
  
  print(f'The word has {len(word)} letters')
  print(f'You have {guesses_left} guesses')
  
  global computer_score, player_score
  
  while letters_wrong != tries and ''.join(clue) != word:
    
    guess = guess_letter()
    x = 0
    
    if len(guess) == 1 and guess.isalpha():
      if guess in letters_tried:
        print(f'You have already picked this letter, the letter is {guess}')
        print(f'You have guessed: {letters_tried}')

      else:
        letters_tried = letters_tried + guess + ',' + ''
        first_index = word.find(guess)
        
        if first_index == -1:
          letters_wrong = letters_wrong + 1
          guesses_left = guesses_left -1
          print('Incorrect letter')
          print(f'You have guessed: {letters_tried}')
          hedgeman(letters_wrong)
          
          if guesses_left > 1:
            print(f'You have {guesses_left} guesses left')
            print(f'You have guessed: {letters_tried}')
            
          elif guesses_left == 1:
            print(f'You have {guesses_left} guesses left')
            print(f'You have guessed: {letters_tried}')
          
        else:
          print(f'The letter {guess} is correct')
          print(f'You have guessed {letters_tried}')
          for i in range(word_length):
            if guess == word[i]:
              clue[i] = guess
              x = x + 1
              
        # Display the partially guessed word
        display_word = ""
        for letter in word:
          if letter in letters_tried:
            display_word += letter
          else:
            display_word += "_"
        print(display_word)
        if x > 0:
          if guesses_left != 1:
            print(f'You have {guesses_left} guesses left')
  
            
          elif guesses_left == 1:
            print(f'You have {guesses_left} guess left')
        
    else:
      print('Please chose another and you can only guess one letter at a time')
      print(f'You have guessed: {letters_tried}')
      continue
      
  hedgeman(letters_wrong)
  print(''.join(clue))
  
  if letters_wrong == tries:
    print('Game over')
    sleep(2)
    print(f'The word was {word}')
    computer_score = computer_score + 1
    
  elif ''.join(clue) == word:
    print(f'You won. The word was {word}')
    player_score = player_score + 1
  play_again()
# end function

def guess_letter():
  print()
  letter = input('What letter do you want to guess?: ').lower()
  print()
  return letter
# end function

def play_again():
  answer = input('Would you like to play again(Y or N)?: ').lower()
  print()
  if answer == 'y' or answer == 'yes':
    return start()
    
  if answer == 'n'or answer == 'no':
    print('Thank you for playing')
    return end()
    
  else:
    print('That is not valid please enter yes or no.')
    print()
    return play_again()
# end function

def end():
    player_score, computer_score
    print('The Scores were: ')
    print(f'You scored: {player_score}')
    print(f'The computer scored: {computer_score}')
# end function

# main code/main game runs

game()
