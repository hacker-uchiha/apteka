# from main import Main
import os
import random
os.system('cls')
import json
import colorama as c
from time import sleep
def reset():
    print(c.Style.RESET_ALL,end="")
class Regist:
    def reg(self):
        self.name = input("Name:  ")
        if self.exit(self,self.name):
            pass
        self.surname = input("Surname:  ")
        self.tell = input("Tell:  ")
        print(c.Fore.GREEN+"Register has done ~ ( Name , Surname , Tell)")
        reset()
        with open(f"{self.tell}.json","a+") as f1:
            json.dump(int(self.tell),f1)
        sleep(5)
        self.regi()
     
    def regi(self):
        x = input("Login(Y/n):  ")
        if x.upper() == 'Y':
            self.nomer = input("nomeringizni kiriting: ")
            self.checking()
            if os.path.isfile(f"{self.nomer}.json"):
                x = random.randint(1000,10000)
                print(x)
                sleep(3)
                self.clsx()
                self.kod = input("yuborilgan kodni kiriting: ")
                self.checking()
                with open(f'{self.nomer}.json') as f1:  
                    if self.kod == str(x):
                        tel = json.load(f1)
                        print("Muvaffaqiyatli kirdingiz:  ")
                            # Main().mainOfMain()
                    else:
                        print("Registratsiyadan oting( exit() kiritilsa Logingga otib ketadi: ):  ")
                        self.regi()
            else:
                print("Registratsiyadan oting( exit() kiritilsa Logingga otib ketadi: ):  ")
                self.regi()
        else:
            self.reg()
    def clsx(self):
        import os    
        os.system('cls')
        
    def exit(self,x):
        if x == "exit()":
            self.regi()
        else:
            return  False
        
    def checking(self):
        for i in range(3):
            for j in range(1,4):
                print(f"Cheking{'.'*j}")
                sleep(1)
                self.clsx()
Regist().regi()


# class information:
#   def gymHall(self):
#     print("""     -about-
# Name of Hall - Fitrium
# Name Coach - Aakhad
# Price hall - 450000
# Addres - Beruniy""")
#     self.buy()
    
    
#   def buy(self):
#     print("[1]. Buy cours\n[2]. Buy with Discount\n[3]. Exit\n")
#     choice = int(input("Choose: "))
#     match choice:
#       case 1:
#         pass
#       case 2:
#         pass
#       case 3:
#         exit()
#       case _:
#         print("Inviled number! Try again")
        
#         self.buy()
