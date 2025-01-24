# import necesary libraries
import random
import time
import sys
import os

# create the multiline ASCII logo
logo = """
  __  __ _                __  __                                   
 |  \/  (_)              |  \/  |                                  
 | \  / |_  ___ _ __ ___ | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 | |\/| | |/ __| '__/ _ \| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |  | | | (__| | | (_) | |  | | (_| | | | | (_| | (_| |  __/ |   
 |_|  |_|_|\___|_|_ \___/|_|__|_|\__,_|_| |_|\__,_|\__, |\___|_|   
         |__ \ / _ \__ \| ____|                     __/ |          
            ) | | | | ) | |__                      |___/           
           / /| | | |/ /|___ \                                     
          / /_| |_| / /_ ___) |                                    
         |____|\___/____|____/                                     
                 
"""

winLogo = """
 __     ______  _    _  __          _______ _   _   _ 
 \ \   / / __ \| |  | | \ \        / /_   _| \ | | | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | | |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | | |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  | |_|
    |_|  \____/ \____/      \/  \/   |_____|_| \_| (_)
                                                      
"""

loseLogo = """
 __     ______  _    _   _      ____   _____ _______      __
 \ \   / / __ \| |  | | | |    / __ \ / ____|__   __|  _ / /
  \ \_/ / |  | | |  | | | |   | |  | | (___    | |    (_) | 
   \   /| |  | | |  | | | |   | |  | |\___ \   | |      | | 
    | | | |__| | |__| | | |___| |__| |____) |  | |     _| | 
    |_|  \____/ \____/  |______\____/|_____/   |_|    (_) | 
                                                         \_\           
"""

# create global variables, initializing with "None" to assign value later
turnNumber = 1

totalMoney = 10000
expenses = 0
price = 50
customerCount = 0
customerSatisfaction = 0
inventory = 0
staffCapacity = 0
unitsSold = 0
profits = 0
score = 0

saveFile = None
save = None
keepGoing = True

currentWorkingDirectory = os.getcwd()
directory = None

print(logo)

def initialize():
    global saveFile, turnNumber, totalMoney, expenses, price, customerCount, customerSatisfaction, inventory, staffCapacity, unitsSold, profits, save, directory, score

    print()
    print("Welcome to MicroManager 2025. Current Save files:")
    print("1.  MicroManagerSave1.mm2025")
    print("2.  MicroManagerSave2.mm2025")
    print("3.  MicroManagerSave2.mm2025")
    print()
    print("Please select a save file: ")
    save = int(input())

    directory = currentWorkingDirectory+"/CSE Project A/Save"+str(save)+".txt"

    if save <= 3:
        with open(directory, "r") as saveFile:
            lines = saveFile.readlines()
            turnNumber, totalMoney, expenses, price, customerCount, customerSatisfaction, inventory, staffCapacity, unitsSold, profits, score = [int(line.strip()) for line in lines]

    else:
        print("No valid input entered, exiting the game...")
        sys.exit()


def turn():
    global turnNumber, score
    
    endTurn = False

    while endTurn == False:
        print()
        print("Turn #"+str(turnNumber))
        print("Current bank balance: "+str(totalMoney)+"$")
        print("Current score: "+str(score))
        print("Please select an action: ")
        print()
        print("1. Marketing - Spend money to attract more customers")
        print("2. Research - Spend money to increase customer satisfaction")
        print("3. Hire Staff - Spend money to increase efficiency")
        print("4. Price Adjustment - Change the price of the product, to inrease amount of \ncustomers and customer satisfaction")
        print("5. Inventory - Spend money to increase inventory of the product")

        choice = int(input())

        if choice == 1:
            marketing()
        elif choice == 2:
            research()
        elif choice == 3:
            hireStaff()
        elif choice == 4:
            priceAdjust()
        elif choice == 5:
            addInventory()
        else:
            print("No valid choice entered")

        # checks if user wants to end turn
        print("End Turn? (Y/N)")
        choice = input()
        choice = choice.upper()

        if choice == "Y":
            endTurn = True

            print()
            print("*"*80) # create a buffer to seperate the turns
        elif choice == "N":
            endTurn = False
        else:
            print("Please enter a valid input next time, ending turn")
            endTurn = True
            print()
            print("*"*80) # create a buffer to seperate the turns

    turnNumber += 1

    # calculate the overall score with weights
    score += int((
    (turnNumber * 0.1) +
    (totalMoney * 0.2) -
    (expenses * 0.15) +
    (price * 0.05) +
    (customerCount * 0.1) +
    (customerSatisfaction * 0.2) +
    (inventory * 0.05) +
    (staffCapacity * 0.05) +
    (unitsSold * 0.1) +
    (profits * 0.15)
))

    afterTurn()

def afterTurn():
    global unitsSold, customerCount, inventory, profits, price, staffCapacity, totalMoney, customerSatisfaction
    
    print("Processing events...")
    print()

    time.sleep(1)
    print(str(customerCount)+" customers came to the store")

    time.sleep(1)
    if inventory > 0:
      unitsSold = random.randint(1, inventory)
      inventory -= unitsSold
      print(str(unitsSold)+" units sold")
    else:
      print("No units sold")
      customerCount -= random.randint(1, customerCount)

      time.sleep(1)
      print(str(customerCount)+" customers were lost due to no inventory")

    time.sleep(1)
    profits += unitsSold*price
    print(str(profits)+"$ in profits")

    time.sleep(1)
    newCustomers = customerSatisfaction*random.randint(1, 6)
    print("We attracted "+str(newCustomers)+" new customers")
    customerCount += newCustomers

    event = random.randint(1, 10)

    if event == 1:
        if staffCapacity > 1:
          print("Our employees have decided to go on strike! Staff Capacity is redcued by 75%")
          staffCapacity = int(0.25*staffCapacity)
    elif event == 9:
        print("There has been an economic crash! We lost 20% of our money due to expenses")
        totalMoney = int(0.8*totalMoney)
    elif event == 3:
        print("The economy is headed in the right direction! We have 20% more money to spend due to reduced expenses!")
        totalMoney = int(1.2*totalMoney)
    elif event == 5:
        if customerCount > 2:
          print("There has been a shift in demand, the amount of loyal customers we have is cut in half!")
          customerCount = int(0.5*customerCount)
    elif event == 7:
        if customerCount > 1:
          print("There has been a shift in demand, and we have double the amount of loyal customers!")
          customerCount = 2*customerCount
    elif event == 2:
        if customerSatisfaction > 1 and customerCount > 3:
          print("A new competitor has entered the market! The amount of loyal customers we have is reduced by 25%, and our customer satisfaction is reduced!")
          customerCount = int(0.75*customerCount)
          customerSatisfaction -= random.randint(1, 2)
    

def marketing():
    # define global variables being modified
    global customerCount, totalMoney

    print()
    print("You have decided to launch a marketing campaign!")
    print("Please select a campaign:")
    print("1. Handing out Flyers - 100$")
    print("2. Radio Advertisment - 500$")
    print("3. YouTube Advertisment - 1000$")
    print()
    print("Your current bank balance is "+str(totalMoney)+"$")

    choice = input()

    print()
    if choice == "1":
        if totalMoney - 100 > 0:
            newCustomers = random.randint(1, 20)
            customerCount += newCustomers
            totalMoney -= 100 # one time

            print("Your flyer advertisment campaign attracted "+str(newCustomers)+" new customers!")
        else:
            print("You don't have enough money to complete this marketing campaign!")
    elif choice == "2":
        if totalMoney - 500 > 0:
            newCustomers = random.randint(1, 100)
            customerCount += newCustomers
            totalMoney -= 500 # one time

            print("Your radio advertisment campaign attracted "+str(newCustomers)+" new customers!")
        else:
          print("You don't have enough money to complete this marketing campaign!")
    elif choice == "3":
        if totalMoney - 1000 > 0:
            newCustomers = random.randint(1, 1000)
            customerCount += newCustomers
            totalMoney -= 1000 # one time

            print("Your YouTube advertisment campaign attracted "+str(newCustomers)+" new customers!")
        else:
          print("You don't have enough money to complete this marketing campaign!")
    
def research():
    global customerSatisfaction, totalMoney
    
    print()
    print("You have decided to launch a research campaign!")
    print("The campaign will cost 3000$, would you like to proceed (Y/N)")
    choice = input()

    choice = choice.upper()

    if choice == "Y":
        if totalMoney - 3000 > 0:
          previousSatisfaction = customerSatisfaction
          satisfactionAddition = random.randint(1, 3)
          customerSatisfaction += satisfactionAddition

          if customerSatisfaction >= 10:
              customerSatisfaction = 10

          totalMoney -= 3000 # one time

          print()
          print("Your customer satisfaction increased from "+str(previousSatisfaction)+" to "+str(customerSatisfaction))
    
def hireStaff():
    global staffCapacity, inventory, expenses, totalMoney
    
    print()
    print("You have decided to hire staff!")
    print("Please select which tier you would like to hire: ")
    print("1. Beginner - 20$/day")
    print("2. Experienced - 35$/day")
    print("3. Scholar - 40$/day")
    
    choice = int(input())

    print()
    print("How many would you like to hire?")
    amount = int(input())

    print()
    if amount > 10:
        print("You can't hire that many!")
    else:
        if choice == 1:
            if totalMoney - (amount*20) > 0:
                print("You have hired "+str(amount)+" of new staff members. The daily cost for these workers is "+str(amount*20)+"$")

                oldInventory = inventory
                newInventory = random.randint(1, 10*amount)
                inventory += newInventory

                print("The company's inventory has been increased from "+str(oldInventory)+" to "+str(inventory))

                expenses += 20*amount
                staffCapacity += amount

        elif choice == 2:
            if totalMoney - (amount*35) > 0:
                print("You have hired "+str(amount)+" of new staff members. The daily cost for these workers is "+str(amount*35)+"$")

                oldInventory = inventory
                newInventory = random.randint(1, 20*amount)
                inventory += newInventory

                print("The company's inventory has been increased from "+str(oldInventory)+" to "+str(inventory))

                expenses += 35*amount
                staffCapacity += 3*amount

        elif choice == 3:
            if totalMoney - (amount*40) > 0:
                print("You have hired "+str(amount)+" of new staff members. The daily cost for these workers is "+str(amount*40)+"$")

                oldInventory = inventory
                newInventory = random.randint(1, 30*amount)
                inventory += newInventory

                print("The company's inventory has been increased from "+str(oldInventory)+" to "+str(inventory))

                expenses += 40*amount
                staffCapacity += 5*amount
                

def priceAdjust():
    global price, customerSatisfaction
    
    print()
    print("You have decided to increase the price of the product!")
    print("The current price of the product is "+str(price)+"$")

    print("Please enter a new price for the product")
    newPrice = int(input())

    if newPrice > price:
        previousSatisfaction = customerSatisfaction
        customerSatisfaction -= random.randint(1, 2)

        print("Due to a price increase, customer satisfaction has decreased from "+str(previousSatisfaction)+" to "+str(customerSatisfaction))
    
    elif newPrice < price:
        previousSatisfaction = customerSatisfaction
        customerSatisfaction += random.randint(1, 2)

        if customerSatisfaction >= 10:
            customerSatisfaction = 10

        print("Due to a price decrease, customer satisfaction has increased from "+str(previousSatisfaction)+" to "+str(customerSatisfaction))

def addInventory():
    global staffCapacity, inventory
    
    print()
    print("You have decided to increase the inventory of your product")
    print("Your current staff capacity is "+str(staffCapacity))
    print("Please choose the amount of inventory you would like (10 Inventory = 1 Staff Capacity)")
    addedInventory = int(input())

    if addedInventory / 10 < staffCapacity:
        inventory += addedInventory

        print()
        print("Your new inventory is "+str(inventory))

def checkSave():
    print()
    print("Would you like to save your game at this point (Y/N)")
    choice = input()

    choice = choice.upper()

    if choice == "Y":
        keepGoing = False
        
        with open(directory, "w") as saveFile:
          saveFile.write(str(turnNumber)) # turn number
          saveFile.write("\n") # newline character
          saveFile.write(str(totalMoney)) # total money
          saveFile.write("\n") # newline character
          saveFile.write(str(expenses)) # expenses
          saveFile.write("\n") # newline character
          saveFile.write(str(price)) # product price
          saveFile.write("\n") # newline character
          saveFile.write(str(customerCount)) # customer count
          saveFile.write("\n") # newline character
          saveFile.write(str(customerSatisfaction)) # customer satisfaction
          saveFile.write("\n") # newline character
          saveFile.write(str(inventory)) # inventory
          saveFile.write("\n") # newline character
          saveFile.write(str(staffCapacity)) # staff capacity
          saveFile.write("\n") # newline character
          saveFile.write(str(unitsSold)) # units sold
          saveFile.write("\n") # newline character
          saveFile.write(str(profits)) # profits

          sys.exit()
    else:
        keepGoing = True
        turn()

def checkWin():
    global winLogo, loseLogo, score, turnNumber, totalMoney, expenses, price, customerCount, customerSatisfaction, inventory, staffCapacity, unitsSold, profits, score
    
    if profits >= 100000:
      print()
      print(winLogo)

      print()
      print("Congratulations on winning the game! You won a monetary victory! Here are your stats:")
      print("Your game eneded on turn #"+str(turnNumber)) # turn number
      print("Your total money was "+str(totalMoney)) # total money
      print("Your total daily expenses were "+str(expenses)) # expenses
      print("The final price of your product was "+str(price)) # product price
      print("You had "+str(customerCount)+" customers in the end") # customer count
      print("Your customer satisfaction was "+str(customerSatisfaction)+"out of 10") # customer satisfaction
      print("Your final inventory was "+str(inventory)) # inventory
      print("Your final staff capacity was "+str(staffCapacity)) # staff capacity
      print("You sold "+str(unitsSold)+" units") # units sold
      print("Your total profits were "+str(profits)) # profits
      print("Your total score was "+str(score))

      sys.exit()
    if score >= 20000:
        print()
        print(winLogo)
        print("Congratulatiosn on winning the game! You won a score victory! Here are your stats:")
        print("Your game eneded on turn #"+str(turnNumber)) # turn number
        print("Your total money was "+str(totalMoney)) # total money
        print("Your total daily expenses were "+str(expenses)) # expenses
        print("The final price of your product was "+str(price)) # product price
        print("You had "+str(customerCount)+" customers in the end") # customer count
        print("Your customer satisfaction was "+str(customerSatisfaction)+"out of 10") # customer satisfaction
        print("Your final inventory was "+str(inventory)) # inventory
        print("Your final staff capacity was "+str(staffCapacity)) # staff capacity
        print("You sold "+str(unitsSold)+" units") # units sold
        print("Your total profits were "+str(profits)) # profits
        print("Your total score was "+str(score))

    if profits <= 0:
      print()
      print(loseLogo)
      print()
      print("Your profits have gone below 0 and you are in debt, and the game will now be terminated")
      sys.exit()
    if customerSatisfaction <= -10:
      print()
      print(loseLogo)
      print()
      print("Due to loss in customer satisfaction, the game will now be terminated")
      sys.exit()
    if customerCount <= 0:
      print()
      print(loseLogo)
      print()
      print("Due to a lack of customers, the game will now be terminated")
      sys.exit()
    if staffCapacity <= 0:
      print()
      print(loseLogo)
      print()
      print("Due to a lack of staff, the game will now be terminated")
      sys.exit()
    


initialize()
while keepGoing == True:
  turn()
  totalMoney -= expenses
  checkWin()
  checkSave()