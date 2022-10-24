from random import choices

class Slot:
    results = ['', '', '']

    def __init__(self):
        self.roll()

    def __str__(self):
        return f"| {self.results[0]} | {self.results[1]} | {self.results[2]} |"
    
    def roll(self):
        self.results = ['', '', '']
        symbols = ['*', 'F', '<', '#', '&', '=', '$']
        chances = [50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156]
        for i in range(0,3):
            result = choices(symbols, chances)
            self.results[i] += str(result[0])

    def lucky_roll(self):
        if self.results[0] == self.results[1] == self.results[2]:
            return self.results[0]
        return False

class User:
    money = 0

    def __init__(self, amount):
        self.money += amount

    def __str__(self):
        return f"You have {self.money} credits."

    def add_money(self, amount):
        self.money += amount

    def remove_money(self, amount):
        self.money -= amount

    def enough_money(self, amount):
        self.remove_money(amount)
        if self.money < 0:
            self.add_money(amount)
            return False
        return True

    def win_multiplier(self, symbol):
        symbols = ['*', 'F', '<', '#', '&', '=', '$']
        multiplier = [5, 10, 20, 70, 200, 1000, 100000]
        x = 7
        for i in range(0, 7):
            if symbol == symbols[i]:
                x = i
                break
            x = 7
        return multiplier[x]

def game():
    print("Welcome to the Slot Machine!")
    money = int(input('How many credits do you wish to deposit?\n'))
    user = User(money)
    while money > 0:
        print(user)
        continue_game = input('Do you wish to stop playing? Answer "Yes" to stop.\n')
        if continue_game != 'Yes':
            creds = int(input('How many credits do you want to spend this round? Be sure to enter an integer!\n'))
            if user.enough_money(creds):
                slot = Slot()
                print(slot)
                if slot.lucky_roll() != False:
                    amount = user.win_multiplier(slot.lucky_roll())*creds
                    print('You have won ' + str(amount) + ' credits!\n')
                    user.add_money(amount)
                else:
                    print('No luck, oops\n')
            else:
                print("You dont have enough credits for that.")
                print(user)
        else:
            money = 0
    print("Game over, see ya soon.\n")

game()