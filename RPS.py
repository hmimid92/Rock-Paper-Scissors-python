# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
# import numpy as np

def player(prev_play, opponent_history=[]):
     opponent_history.append(prev_play)
     choices = {0: "R", 1: "P", 2: "S"}

     guess = 'R'
     gg = random.gauss(0, 8)

     if len(opponent_history) > 2:
       if gg < -1:
          if prev_play == 'R':
               guess = 'P'
          elif prev_play == 'P':
               guess = 'S'
          elif prev_play == 'S':
               guess = "S"
          else:
               guess = ''
       elif gg < 0:
           if prev_play == 'R':
               guess = "P"
           elif prev_play == 'P':
               guess = 'S'
           elif prev_play == 'S':
               guess = 'R'
           else:
               guess = ""
       elif gg < 1:
           if prev_play == 'R':
               guess = "R"
           elif prev_play == 'P':
               guess = choices[random.randint(0,2)]
           elif prev_play == 'S':
               guess = 'R'
           else:
               guess = ""
       elif gg < 2:
           if prev_play == 'R':
               guess = ''
           elif prev_play == 'P':
               guess = choices[random.randint(0,2)]
           elif prev_play == 'S':
               guess = 'S'
           else:
               guess = ""
       else:
           return ''
     
     return guess