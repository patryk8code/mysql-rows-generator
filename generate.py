import os
import random
import msvcrt
import time
from datetime import datetime
import functions as f 

RANDOM_COLUMN_NAMES=0

column_name =[]
column_types=[]

while True:
    f.menu0()
    a=msvcrt.getwch()
    print(a)
    if(a=='1'):
        os.system("cls")
        f.insert_names()
        a = input("Column name: ")
        if (a == '0'):
            RANDOM_COLUMN_NAMES=1
            os.system("cls")
            # TODO
        else:
            column_name.append(a)
            os.system("cls")
            while(True):
                print("0: END")
                print("1: Delete last one")
                print("2: Save to file")
                print(column_name)
                a = input("Column name: ")
                if (a == '0'):
                    f.DataTypes()
                    for i in column_name:
                        print(i, end=': ')
                        a=input()
                        if (a == '1'):
                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$if (a == '1'):
                            column_types.append(a)
                elif (a == '1'):
                    if column_name:
                        column_name.pop()
                    else:
                        print(f.bcolors.WARNING +"It's empty!!"+ f.bcolors.ENDC)
                elif (a == '2'):
                    # TODO
                    print("opt 2")
                elif a:
                    column_name.append(a)
                else:
                    os.system("cls")
                    print(f.bcolors.WARNING +"Something is wrong.."+ f.bcolors.ENDC)

            
    if (a == '2'):
        os.system("cls")
        f.more_info()
        continue
    if (a == 'q' or a == 'Q'):
        os.system("cls")
        exit(0)
    else:
        os.system('cls')
        print(f.bcolors.WARNING + 'Please choose one option'+ f.bcolors.ENDC)
