import functions as f 

import os
import random
import time
from datetime import datetime
import msvcrt

MAX_COLUMNS=20

column_name =[]
column_types=[]

while True:
    # f.GenerateRows(["id","imie","nazwisko","wiek","c1","c2","c3"],[0,1,2,3,0,0,8])
    # continue
    f.Menu0()
    a=msvcrt.getwch()
    print(a)
    if(a=='1'):
        os.system("cls")
        f.InsertNames()
        a = input("Column name: ")
        if (a == '0'):
            os.system("cls")
            f.InsertDataTypes('data/ColumnNames.txt')     
        else:
            column_name.append(a)
            while(True):
                os.system("cls")
                print("0: END")
                print("1: Delete last one")
                print(column_name)
                a = input("Column name: ")

                if (a == '0'):
                    os.system("cls")
                    i=0
                    FileName=''
                    while(True):
                        if not (os.path.isfile('data/ColumnNames'+str(i)+'.txt')):
                            FileName='data/ColumnNames'+str(i)+'.txt'
                            ColumnNames=open(FileName,'w')
                            for q in column_name:
                                ColumnNames.write(q+'\n')
                            ColumnNames.close()
                            break
                        i=i+1
                    f.InsertDataTypes(FileName)
                    while(True):
                        os.system("cls")
                        print("Additional options:")
                        print("0: No.")
                        print("1: Set range")
                        print("2: Use costum files with names")
                        # todo
                    break

                elif (a == '1'):
                    if column_name:
                        column_name.pop()
                    else:
                        print(f.bcolors.WARNING +"It's empty!!"+ f.bcolors.ENDC)
                elif a:
                    column_name.append(a)
                else:
                    os.system("cls")
                    print(f.bcolors.WARNING +"Something is wrong.."+ f.bcolors.ENDC)

            
    if (a == '2'):
        os.system("cls")
        f.MoreInfo()
        continue
    if (a == 'q' or a == 'Q'):
        os.system("cls")
        exit(0)
    else:
        os.system('cls')
        print(f.bcolors.WARNING + 'Please choose one option'+ f.bcolors.ENDC)
