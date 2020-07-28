class CoffeeMachine:
    
    def __init__(self, water_machine, milk_machine, beans_machine, disp_cups, tot_money):
        self.water_machine = water_machine
        self.milk_machine = milk_machine
        self.beans_machine = beans_machine
        self.disp_cups = disp_cups
        self.tot_money = tot_money
        self.state = None
        self.input_comm = "0"
        self.input_fill = None
        self.input_com = "0"
        self.buy_input = None
        self.state_buy = "0"
        self.available_w = 0
        self.available_beans = 0
        self.available_milk = 0
        self.state_update = "0"
        self.state_buying = "0"
        self.water_input = 0
        self.milk_input = 0
        self.coffee_input = 0
        self.cups_input = 0
    
    def check_resources(self, state_buying):
        self.state_buying = state_buying
        if self.state_buying == "ESPRESSO":
            self.available_w = self.water_machine - 250
            self.available_beans = self.beans_machine - 16
        elif self.state_buying == "CAPPUCCINO":
            self.available_w = self.water_machine - 200
            self.available_beans = self.beans_machine - 12
            self.available_milk = self.milk_machine - 100
        elif self.state_buying == "LATTE":
            self.available_w = self.water_machine - 350
            self.available_beans = self.beans_machine - 20
            self.available_milk = self.milk_machine - 75
        if self.available_w < 0:
            print("Sorry, not enough water")
        elif self.available_beans < 0:
            print("Sorry, not enough coffee beans")
        elif self.available_milk < 0:
            print("Sorry, not enough milk")
        elif self.disp_cups == 0:
            print("Sorry, not enough cups")
        else:
            print("I have enough resources, making you a coffee!")
            self.update_resources(state_buying, "BUY")
        self.state = "DISPLAY"
        self.display()
    
    def update_resources(self, state_buying, state_update):
        self.state_update = state_update
        self.state_buying = state_buying
        if self.state_update == "BUY":
            if self.state_buying == "ESPRESSO":
                self.water_machine -= 250
                self.beans_machine -= 16
                self.tot_money += 4
            elif self.state_buying == "CAPPUCCINO":
                self.water_machine -= 200
                self.beans_machine -= 12
                self.milk_machine -= 100
                self.tot_money += 6
            elif self.state_buying == "LATTE":
                self.water_machine -= 350
                self.beans_machine -= 20
                self.milk_machine -= 75
                self.tot_money += 7
            self.disp_cups -= 1
        elif self.state_update == "FILL":
            self.water_machine += int(self.water_input)
            self.milk_machine += int(self.milk_input)
            self.beans_machine += int(self.coffee_input)
            self.disp_cups += int(self.cups_input)
            self.state = "DISPLAY"
            self.display()
        elif self.state_update == "TAKE":
            self.tot_money = 0
            self.state = "DISPLAY"
            self.display()
    
    def display_resources(self):
        print(f"""\n{self.water_machine} of water \n{self.milk_machine} of milk \n{self.beans_machine} of coffee beans
{self.disp_cups} of disposable cups \n{self.tot_money} of money""")
    
    def display(self):
        if self.state == "DISPLAY":
            print("\nWrite action (buy, fill, take, remaining, exit):")
        elif self.state == "BUY":
            print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif self.state == "FILL":
            print("\nWrite how many ml of water do you want to add:")
            self.water_input = input()
            print("Write how many ml of milk do you want to add:")
            self.milk_input = input()
            print("Write how many grams of coffee beans do you want to add:")
            self.coffee_input = input()
            print("Write how many disposable cups of coffee do you want to add:")
            self.cups_input = input()
            self.update_resources(None, "FILL")
        elif self.state == "REMAINING":
            self.display_resources()
            self.state = "DISPLAY"
            self.display()
        elif self.state == "TAKE":
            print(f"\nI gave you {self.tot_money}")
            self.update_resources(None, "TAKE")
    
    def inputs(self, input_com):
        self.input_com = input_com
        if self.input_com == "0":
            self.state = "DISPLAY"
            self.display()
            return True
        elif self.input_com == "buy":
            self.state = "BUY"
            self.display()
            self.buy_inputs()
            return True
        elif self.input_com == "remaining":
            self.state = "REMAINING"
            self.display()
            return True
        elif self.input_com == "fill":
            self.state = "FILL"
            self.display()
            return True
        elif self.input_com == "exit":
            self.state = "EXIT"
            return False
        elif self.input_com == "take":
            self.state = "TAKE"
            self.display()
            return True
    
    def buy_inputs(self):
        self.buy_input = input()
        if self.buy_input == "1":
            self.state_buy = "ESPRESSO"
            self.check_resources(self.state_buy)
        elif self.buy_input == "2":
            self.state_buy = "LATTE"
            self.check_resources(self.state_buy)
        elif self.buy_input == "3":
            self.state_buy = "CAPPUCCINO"
            self.check_resources(self.state_buy)
        elif self.buy_input == "back":
            self.state = "DISPLAY"
            self.display()


Machine = CoffeeMachine(400, 540, 120, 9, 550)

Machine.inputs("0")
flag = True
while flag == True:
    flag = Machine.inputs(input())

