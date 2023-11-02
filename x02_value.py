#!python3
'''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg:
  '''

def value(hand):
  total = 0
  total2 = 0
  for i in range(hand):
   if "A" in hand:
    total = total + 11
    return (total - 10)
   elif "J" in hand: 
     total = total + 10
   elif "Q" in hand: 
     total = total + 10
   elif "K" in hand: 
     total = total + 10
     n = 1
     #1
   elif n in hand: 
     total = total + 10
   else:
    n = n+1
    for i in range(8):
     n = i + 1
     if n in hand: 
      total = total + n
     else:
      continue
    


def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__name__":
  main()
