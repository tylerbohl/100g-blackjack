#!python3

"""
Create a list of cards
the cards should be denoted with a number or A, J, Q, K, T (for ace, jack, queen, king or ten)
as well as a suit
"""
import random

def createDeck():
  ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['C','D','H','S']
  deck = []
  for i in range(52):
    r = random.uniform(0, 12)
    s = random.uniform(0, 3)
    r = round(r)
    s = round(s)
    r = ranks[r]
    s = suits[s]
    card = r + s
    deck.append(card)
  
  return deck
print(createDeck())
'''
  use the two lists to create a new list "deck" 
  return the deck list to your calling function
'''

def main():
  deck = createDeck()
  assert "JH" in deck 
  assert "AC" in deck 
  assert "TD" in deck 
  assert len(deck) == 52
  
if __name__ == "__main__":
  main()
