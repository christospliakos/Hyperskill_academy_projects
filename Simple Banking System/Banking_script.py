import random
import sqlite3
 
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS card (
                    id INTEGER,
                    number TEXT,
                    pin TEXT,
                    balance INTEGER DEFAULT 0);""")
account_id = 1
 
 
class Bank:
    
    def __init__(self):
        last_digits = random.randint(100000000, 999999999)
        self.card_number = int("400000" + str(last_digits))
        self.last_digit = self.luhn_algorithm()
        self.card_number = int("400000" + str(last_digits) + str(self.last_digit))
        self.pin = random.randint(1000, 9999)
        self.balance = 0
        print("Your card has been created")
        print(f"Your card number:\n{self.card_number}")
        print(f"Your card PIN:\n{self.pin}\n")
    
    def luhn_algorithm(self):
        card_number_2 = str(self.card_number)
        digits_list = []
        for i in range(0, len(card_number_2)):
            digits_list.append(int(card_number_2[i]))
            if i == 0 or i % 2 == 0:
                digits_list[i] = 2 * digits_list[i]
            if digits_list[i] > 9:
                digits_list[i] = digits_list[i] - 9
        sum_digit = 0
        for i in range(0, 10):
            if (sum(digits_list) + i) % 10 == 0:
                sum_digit = i
                break
        return sum_digit
    
    def store_data(self, counter_id):
        cur.execute(
            f"INSERT INTO card VALUES ({counter_id}, {str(self.card_number)}, {str(self.pin)}, {self.balance});")
        conn.commit()
    
    @staticmethod
    def check_pin(card_num, pin_num):
        state = False
        cur.execute(f"SELECT * FROM card WHERE (number = {card_num} AND pin = {pin_num});")
        card_check = cur.fetchone()
        if card_check is None:
            print("Wrong card number or PIN!")
        else:
            print("You have successfully logged in!")
            state = True
        return state
    
    @staticmethod
    def balance(card_num, pin_num):
        cur.execute(f"SELECT balance FROM card WHERE (number = {card_num} AND pin = {pin_num});")
        balance_amount = cur.fetchone()
        print(f"\nBalance:{int(balance_amount[0])}")
    
    @staticmethod
    def deposit_money(income, card_num):  # Updating the balance from the accounts
        cur.execute(f"UPDATE card SET balance = balance + {income} WHERE (number = {card_num});")
        conn.commit()
    
    @staticmethod
    def transfer_money_card_check(transfer_card_, card_num, pin_num):  # Checking if the transfer card is legit
        if transfer_card_ == card_num:
            print("You cant transfer money to the same account!")
        else:
            cur.execute(f"SELECT * FROM card WHERE (number = {transfer_card_});")
            card_check = cur.fetchone()
            state_luhn = Bank.check_luhn_algorithm(transfer_card_)
            if state_luhn:
                if card_check is None:
                    print("Such card does not exist.")
                else:
                    Bank.transfer_money_check(card_num, pin_num, transfer_card_)  # If passes the tests, it transfers
                    # the money
            else:
                print("Probably you made mistake in the card number. Please try again!")
    
    @staticmethod
    def transfer_money_check(card_num, pin_num, transfer_card_):  # Checking if there is enough money
        transfer_amount = float(input("Enter how much money you want to transfer:\n>"))
        cur.execute(f"SELECT balance FROM card WHERE (number = {card_num} AND pin = {pin_num});")
        balance_amount = float(cur.fetchone()[0])
        if transfer_amount > balance_amount:
            print("Not enough money!")
        else:  # Doing the transfer
            Bank.deposit_money(transfer_amount, transfer_card_)  # transferring money to other card
            Bank.deposit_money((-transfer_amount), card_num)  # subtracting money from the account which transfers
            print("Success!")
    
    @staticmethod
    def check_luhn_algorithm(transfer_c):  # Checking if the transfer card passes the Luhn algorithm
        card_number_2 = str(transfer_c)
        digits_list = []
        for i in range(0, len(card_number_2) - 1):
            digits_list.append(int(card_number_2[i]))
            if i == 0 or i % 2 == 0:
                digits_list[i] = 2 * digits_list[i]
            if digits_list[i] > 9:
                digits_list[i] = digits_list[i] - 9
        sum_digit = 0
        for i in range(0, 10):
            if (sum(digits_list) + i) % 10 == 0:
                sum_digit = i
                break
        if sum_digit == int(transfer_c[-1]):
            return True
        else:
            return False
    
    @staticmethod
    def remove_entry(card_num):
        cur.execute(f"DELETE FROM card WHERE number ={card_num}")
        conn.commit()
        print("\nThe account has been closed!")
 
 
counter = 0
while True:
    print("""1. Create an account
    2. Log into account
    0. Exit""")
    action = int(input())
    if action == 1:
        counter += 1
        new_account = Bank()
        new_account.store_data(counter)
        continue
    elif action == 2:
        card_no = (input("Enter your card number:\n"))
        pin_no = (input("Enter your PIN:\n"))
        state_pin = Bank.check_pin(card_no, pin_no)
        if state_pin:  # True
            while True:
                action2 = int(
                    input("\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n>"))
                if action2 == 1:
                    Bank.balance(card_no, pin_no)
                    continue
                elif action2 == 2:
                    income_amount = float(input("Enter income:\n>"))
                    Bank.deposit_money(income_amount, card_no)
                    print("Income was added!")
                elif action2 == 3:
                    transfer_card = input("Transfer\nEnter card number:\n>")
                    Bank.transfer_money_card_check(transfer_card, card_no, pin_no)
                elif action2 == 4:
                    Bank.remove_entry(card_no)
                    break
                elif action2 == 5:
                    print("You have successfully logged out!")
                    break
                elif action2 == 0:
                    print("Bye!")
                    break
            if action2 == 0:
                break
        else:  # False
            continue
    elif action == 0:
        print("Bye!")
        break
