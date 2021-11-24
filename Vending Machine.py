
name = [" Coca-Cola"," Fanta"," Ice-Tea"," RedBull"," Orange Juice"," Apple Juice"] #a list of which types of products to store
price = [5.5,5,5,10,6,6] # prices of products. In this case the same-indexed ones point to the same product exp. price[0] is the price of name[0]
stock = [5,5,5,5,5,5] # the number in stock of products, same index thing is still valid

YorN="y" #this variable holds "y" initally and that means repeat the processes of VendingMachineInputManager


cash=0 # this holds the cash you insert when you start this vending machine


    



def notEnoughMoney():
    global cash
    print("Your cash is ",cash ," and you don't have enough money to buy a new thing.\n Do you want to add the price or take the money back?  take/add")
    TorA = input()
    

    if TorA.upper() =="TAKE":
        print("you got " ,cash, "Turkish liras back")
        cash = 0
        
    elif TorA.upper() =="ADD":
        adder = eval(input("How much money do you want to add?"))
        cash = cash + adder
        print("Your cash = ",cash)
        
    




def VendingMachineInputManager():
 global stock
 global cash
 global YorN
 r=0 # holds the value of maximum tries when you don't have enough money. If you exceed 3 then machine automatically stops
 
 while YorN =="y": #this is our main loop
    
    index=eval(input("\n\nWhich one do you want to take?"))


    #check if the index is valid or not
    while not 0 <index or not index < 7:
        print("Wrong index try again :(")
        index = eval(input("Which one do you want to take?"))


        
        
    cash=eval(input("How much money do you have?"))
    


    #check if the inserted cash is enough to buy something in the vending machine
    if cash < price[index-1]:
        print("Not enough money :(")
        print("Your cash = ",cash)
        while cash<min(price) and r<3:
            notEnoughMoney()
            r=r+1 # increase the "how many times did i try" holder
            
        if 0<cash<min(price): #if r exceeds 3 then stop
            print("Too much process. Take your money back")
            print("you got " ,cash, "Turkish liras back")
            cash = 0
            break



    # if the cash inserted is exactly equal to this, then execute the following code 
    elif cash==price[index-1]:
        if stock[index-1]>0:
            cash = cash - price[index-1]
            print("You Have Bought" , name[index-1], sep="")
            stock[index-1]=stock[index-1]-1
            print("Your cash = ",cash)
            YorN= input("You want to take another thing ? y/n")
        else:
            print("We don't have" , name[index-1],"in stock" ,sep=" ")
            print("Your cash = ",cash)
            YorN= input("You want to take another thing ? y/n")






    elif cash > price[index-1]:

        #if is in stock
        if stock[index-1]>0:

            
           print("You Have Bought" , name[index-1], sep="" , end="\n")
           cash = cash - price[index-1]
           stock[index-1]=stock[index-1]-1
           print("Your cash = ",cash)

           #1) if the user still has some money even after buying something
           while cash > 0: 

               #2) but the money isn't enough to buy any more thing execute this code
               if 0<cash<min(price):
                   notEnoughMoney()
                   if cash<min(price):
                       break

               #2) and also has enough money to buy another product execute this code
               elif cash>min(price):    
                   YorN= input("You want to take another thing ? y/n") # check if the user wants to continue or stop

                   #if continue :
                   if YorN =="y":
                       
                      index=eval(input("\n\nWhich one do you want to take?"))
             
                      if cash > price[index-1]:
                          if stock[index-1]>0: #if in stock
                             cash = cash - price[index-1]
                             print("You Have Bought" , name[index-1], sep="")
                             stock[index-1]=stock[index-1]-1
                             print("Your cash = ",cash)
                          else :#if not in stock
                             print("We don't have" , name[index-1],"in stock" ,sep=" ")
                      else : #if money is not enough
                          notEnoughMoney()
                          break

                   #if stop :
                   else :
                       break



        else : #if not in stock
            print("We don't have" , name[index-1],"in stock" ,sep=" ")
            

 #the shutting message
 print("Thank you for using Ruzgar's Vending Machine")
    





def VendingMachineBuilder(): # this code primitevely renders a user interface. Again, very primitively
    
    repeater = 1

    #this code iterates 3 times and each line: renders name[1],name[2] "\n" name[3],name[4] "\n" name[5] name[6]
    for i in range(0,6,2):
       print("___________________________________________")
       print("|({0}) {1:<7s}={2:.1f} | ({3}){4:>7s}={5:.1f}|".format(repeater,name[i],price[i],repeater+1,name[i+1],price[i+1]))
       repeater=repeater+2







def main(): # main function calls the other functions
    VendingMachineBuilder()
    VendingMachineInputManager()
    







main()

