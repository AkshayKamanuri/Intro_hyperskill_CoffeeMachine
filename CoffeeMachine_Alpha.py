class CoffeeMachine():
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    x = 0

    def BuyCoffee(self):
        x = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back -to main menu:\n")
        if self.cups > 1:
            if x == '1' and self.water >= 250 and self.beans >= 16:
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
                print("I have enough resources, making you a coffee!\n")
            elif x == '1' and self.water < 250:
                print("Sorry, not enough water!\n")
            elif x == '1' and self.beans < 16:
                print("Sorry, not enough beans!\n")
            if x == '2' and self.water >= 250 and self.milk >= 75 and self.beans >= 16:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
                print("I have enough resources, making you a coffee!\n")
            elif x == '2' and self.water < 250:
                print("Sorry, not enough water!\n")
            elif x == '2' and self.milk < 75:
                print("Sorry, not enough milk!\n")
            elif x == '2' and self.beans < 16:
                print("Sorry, not enough beans!\n")
            if x == '3' and self.water >= 200 and self.milk >= 100 and self.beans >= 12:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
                print("I have enough resources, making you a coffee!\n")
            elif x == '3' and self.water < 200:
                print("Sorry, not enough water!\n")
            elif x == '3' and self.milk < 100:
                print("Sorry, not enough milk!\n")
            elif x == '3' and self.beans < 12:
                print("Sorry, not enough beans!\n")
        elif self.cups < 1:
            print("Sorry, not enough cups!\n")
        elif x == 'back':
            return

    def Refill(self):
        t = input("Write how many ml of water do you want to add:")
        self.water += int(t)
        u = input("Write how many ml of milk do you want to add:")
        self.milk += int(u)
        v = input("Write how many grams of coffee beans do you want to add:")
        self.beans += int(v)
        w = input("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(w)

    def TakeMoney(self):
        print("I gave you", self.money)
        self.money = 0

    def Inventory(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def default(self):
        y = input("Write action (buy, fill, take, remaining, exit):\n")
        if y == "buy":
            self.BuyCoffee()
        elif y == "fill":
            self.Refill()
        elif y == "take":
            self.TakeMoney()
        elif y == "remaining":
            self.Inventory()
        elif y == "exit":
            return False

cm = CoffeeMachine()
while cm.x < 1:
    t = cm.default()
    if t == False:
        cm.x = 1
