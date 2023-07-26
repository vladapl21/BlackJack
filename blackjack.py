import math
import random
import time

d = [2,3,4,5,6,7,8,9,10,10,10,10,11]
Hand = []
DHand = []
i = 1
Cards = 0
j=0
aces = 0
buss = False
DCards = 0


#Append two random cards to the Hand array
for i in range(2):
  Hand.append(random.choice(d))
  i = i+1
  Cards = Cards + 1
  if Hand[Cards-1] == 11:
    aces = aces + 1

#Small check in case I got two aces
if 11 in Hand and sum(Hand) > 21:
    Hand.remove(11)
    Hand.append(1)

#Output the two cards I got
print(f'Your current hand is {Hand}  Total = {sum(Hand)}')
print('')

#If you get blackjack straight away, you only receive 1.5x (not 2x)
if sum(Hand) == 21:
  print('Blackjack - You Win 1.5x your bet!')
  exit()

#Ask user if they want to hit or stick
Choice = input(f'Do you want to hit "h" or stay "s":  ')

#If they didnt choose stick
while Choice != 's':

#----If they choose to hit, another card is added
  if Choice == 'h':
    Hand.append(random.choice(d))
    Cards = Cards + 1
    print('You got a', Hand[Cards-1])
    if Hand[Cards-1] == 11: #We check if the user has received an ace
      aces = aces + 1
    i=0
    
    #Check to determine your total
    CheckValue = 0
    for j in range(Cards):
      CheckValue = CheckValue + int(Hand[j])
      j = j+1
    j = 0

    #11 changes to 1 only if there is an Ace and hand is over 21
    if 11 in Hand and sum(Hand) > 21:
      if CheckValue > 21:
        Hand.remove(11)
        Hand.append(1)

    #Need to check new value of hand
    CheckValue = 0
    for j in range(Cards):
      CheckValue = CheckValue + int(Hand[j])
      j = j+1
    j = 0

    print(f'Your current hand is {Hand}  Total = {CheckValue}')
    
    #Early check to see if you went bust
    if CheckValue > 21:
      print(f'The {Hand[Cards-1]} sent you over the limit of 21...')
      buss = True
      break
      
  Choice = input(f'Do you want to hit "h" or stay "s":  ')
#----

#If user has gone bust, program quits
if buss == True:
  exit()

print('')
time.sleep(1)

#Made a nice recap of which cards you got
for j in range(Cards):
  if j+1 == 1:
    m = 'st'
  elif j+1 == 2:
    m = 'nd'
  elif j+1 == 3:
    m = 'rd'
  else:
    m = 'th'
  print(f'Your {j+1}{m} card is {int(Hand[j])}')
  time.sleep(0.8)
  j = j+1
  

print(f'Total = {sum(Hand)}')
print('')
#--------------NOW THE DEALER DRAWS CARDS - this is the mid-point--#
time.sleep(2)
print(f'It is now the Dealers turn to draw cards.')

#Draw dealers first two cards
DCard1 = random.choice(d)
DCard2 = random.choice(d)
DHand.append(int(DCard1))
DHand.append(int(DCard2))
Dealer = sum(DHand)
if 11 in DHand and Dealer > 21:
    DHand.remove(11)
    DHand.append(1)
print(f'Dealer got {DCard1} and {DCard2}. This adds up to {sum(DHand)}.')
time.sleep(2.5)

#Dealer always draws until they get a minimum of 17
while sum(DHand) < 17:
  print('The dealer draws another card')
  time.sleep(1)
  DHand.append(random.choice(d))
  DCards = len(DHand)
  print(f'Dealer got a {int(DHand[DCards-1])}')
  Dealer = 0
  Dealer = sum(DHand)
  #If they go over 21, we need to check whether we can make any of the aces a 1
  if 11 in DHand and Dealer > 21:
    DHand.remove(11)
    DHand.append(1)
  print(f'Dealers hand: {DHand}  Total = {sum(DHand)}')
  time.sleep(2)

#If it is actually over 21, user wins
if Dealer > 21:
  print('Dealer went bust - You Win 2x your bet!')
  exit()


#Double check to see if you went bust    
if sum(Hand) <= 21:
  #You have to have more than the dealer to win
  if sum(Hand) > Dealer:
    print('You got more than the dealer - You Win 2x your bet!')
  else: 
    print('You got same or less than the dealer - You lost what you bet!')
