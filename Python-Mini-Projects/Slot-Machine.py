MAX_LINES=3
MIN_BET=1
MAX_BET=100

def deposit ():
   while True:
     amount=input('what would you like to deposit? £')
     if amount.isdigit():
       amount1=int(amount)
     if amount1 > 0:
         break
     else:
          print('amount must be greater than zero')
   else:
       print('please enter a number')
   return amount1



def lines():
  while True:
     balance=input(f'How many lines would you like to bet on (1-{MAX_LINES})? ')
     if balance.isdigt():
       lines= int(balance)
       if 1 <= lines <= MAX_LINES :
         break
       else:
         print('Enter a valid number of lines ')
     else:
       print('please enter a number')
  return lines


def get_bet ():
  while True:
     bet=input('how much would you like to bet? £')
     if bet.isdigt():
       amount= int(bet)
       if MIN_BET <=amount<= MAX_BET > 0:
         break
       else:
         print(f'Amount bet must be between{MIN_BET}-{MAX_BET}')
     else:
       print('please enter a number')
  return amount


def main():
  balance=deposit()
  lin1= lines()
  while True :
    bet=get_bet()
    Total_bet= bet*lin1
    if Total_bet > balance:
      print(f'You do not have enough to bet that amount,your balance is {balance}')
    else:
      break
     

main()