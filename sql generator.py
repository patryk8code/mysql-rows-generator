import os
import random
import msvcrt
import time
from datetime import datetime
import string

def insert_options():
    print("0: end")
    print("1: INT")
    print("2: STRING") 
    print("3: BOOL")
    print("4: DECIMAL")
    print("5: DATE")
    print("6: DATETIME")
    print("7: TIME")
    print("8: YEAR")
    print("9: Delete last one")

def save_to_list(a):
    global how_much_columns
    how_much_columns+=1
    list_of_columns_types.append(a)
    if a=='1':        
        show_list_of_columns_types.append("INT")
    elif a=='2':        
        show_list_of_columns_types.append("STRING")
    elif a=='3':        
        show_list_of_columns_types.append("BOOL")
    elif a=='4':        
        show_list_of_columns_types.append("DECIMAL")
    elif a=='5':        
        show_list_of_columns_types.append("DATE")
    elif a=='6':        
        show_list_of_columns_types.append("DATETIME")
    elif a=='7':        
        show_list_of_columns_types.append("TIME")
    elif a=='8':        
        show_list_of_columns_types.append("YEAR")
    elif a=='9':      
        if(show_list_of_columns_types):  
            show_list_of_columns_types.pop()
            how_much_columns-=2
        else:
            print("Not possible, array is empty!")
            time.sleep(1)
    else:
        print("Error u typed f{a}")

def insert_column_types():
    while True:
        os.system('cls')
        print(show_list_of_columns_types)    
        print("- - - - - - - - - - ")
        insert_options()
        a=msvcrt.getwch()
        if(a.isnumeric()):
            if(a=='0'):
                insert_column_names()
                break
            else:
                save_to_list(a)
        elif(ord(a)==13):
            insert_column_names()
        else:
            print("Press right number or press '0' to go to next step")
def add_column_names():
    os.system("cls")
    
    for i in show_list_of_columns_types:
        while True:
            print(i,end=": ")
            name=input()
            if(name=="" or name[0].isdigit()):
                print("wrong name")
            else:
                list_of_columns_names.append(name)
                break
    print("Done..")
    generate_mysql()

def insert_column_names():
    os.system("cls")
    while True:
        print("Do you want to add column names?")
        print("0: Return")
        print("1: Yes")
        print("2: No, generate only rows")
        a=msvcrt.getwch()
        if(a.isnumeric()):
            if(a=='0'):
                insert_column_types()
                break
            if(a=='1'):
                add_column_names()
                break
            if(a=='2'):
                generate_mysql() #todo
                # special_options()
                break
            else:
                save_to_list(a)
        else:
            os.system("cls")
            print("Press right number or press '0' to go to next step")

def special_options():
    # todo
    wanna_id=0

    random_int_from=0
    random_int_limit=100000

    random_float_from=0
    random_float_limit=100000
    random_float_after_comma=100

    random_date_start=0
    random_date_end=10000000000000
def generate_mysql():
    while True:
        print("how much rows do u need? ")
        how_much_rows=input()
        if(how_much_rows.isnumeric()):
            how_much_rows=int(how_much_rows)
            if(how_much_rows>=0):
                break
            elif(how_much_rows==-1):
                insert_column_names()
                break
        else:
            os.system("cls")
            print("Wrong!! type NUMBERS")

    save_to_file="INSERT INTO ___TABLE___ "
    if(list_of_columns_names):
        save_to_file="INSERT INTO ___TABLE___ ("
        for i in list_of_columns_names:
            save_to_file+=i+", "
        save_to_file=save_to_file[:-2]
        save_to_file+=") VALUES "
    else:
        save_to_file+="VALUES "
    for i in range(how_much_rows):
        save_to_file+=generate_row(i)
    print("Now check file \"data.txt\"")
    
    f = open("data.txt", "w")
    f.write(save_to_file[:-2]+";")
    f.close()

wanna_id=1

random_int_from=0
random_int_limit=100000

random_float_from=0
random_float_limit=100000
random_float_after_comma=100

random_date_start=0
random_date_end=10000000000000

arr=['apple', 'banana', 'cherry', 'pear', 'orange', 'grape', 'mango', 'kiwi', 'lemon', 'lime', 'grapefruit', 'strawberry', 'watermelon', 'peach', 'plum', 'olive', 'avocado', 'carrot', 'cucumber', 'garlic', 'onion', 'spinach', 'tomato', 'lettuce', 'celery', 'cucumber', 'pumpkin', 'broccoli', 'cauliflower']
def generate_row(id):
    id+=96001
    to_return="("
    if(wanna_id==1):
        to_return+=str(id)+","
    for i in list_of_columns_types:
        if(i=='1'):
            to_return+=str(random.randrange(random_int_from, random_int_limit))+','
        if(i=='2'):
            to_return+='\''
            to_return+=arr[random.randrange(0,len(arr))]
            to_return+='\','
        if(i=='3'):
            to_return+=str(random.randrange(0, 1))+','
        if(i=='4'):
            to_return+=str((random.randrange(random_float_from, random_float_limit)/random_float_after_comma))+','
        if(i=='5'):
            timestamp = random.randrange(random_date_start,random_date_end)
            random_datetime=datetime.fromtimestamp((timestamp)/1000).strftime("%Y-%m-%d")
            to_return+="'"
            to_return+=str(random_datetime)
            to_return+="',"
        if(i=='6'):
            timestamp = random.randrange(random_date_start,random_date_end)
            random_datetime=(datetime.fromtimestamp((timestamp)/1000)).strftime("%Y-%m-%d %H:%M:%S")
            to_return+="'"
            to_return+=str(random_datetime)
            to_return+="',"
        if(i=='7'):
            timestamp = random.randrange(random_date_start,random_date_end)
            random_datetime=(datetime.fromtimestamp((timestamp)/1000)).strftime("%H:%M:%S")
            to_return+="'"
            to_return+=str(random_datetime)
            to_return+="',"
        if(i=='8'): 
            timestamp = random.randrange(random_date_start,random_date_end)
            random_datetime=(datetime.fromtimestamp((timestamp)/1000)).strftime("%Y")
            to_return+="'"
            to_return+=str(random_datetime)
            to_return+="',"
    to_return=to_return[:-1]
    to_return+="),\n"
    return to_return
open("data.txt","w")

how_much_rows=0
how_much_columns=0
list_of_columns_types=[]
show_list_of_columns_types=[]
list_of_columns_names=[]

a='0'


# -----------------------------------------------------------------------------------------------------------------
while True:
    print("hello in mysql rows generator")
    print("1: Start generating")
    print("2: More info")
    print("Q: Close program")
    a=msvcrt.getwch()

    if(a=='1'):
        os.system("cls")
        while True:
            insert_column_types()

            # maybe in future :)

#             print("1: Insert column data types")
#             print("2: Insert column names")
#             print("0: Return")
#             a=msvcrt.getwch()
#             if(a=='1'):
#                 insert_column_types()
#                 break
# # -----------------------------------------------------------------------------------------------------------------
#             elif(a=='2'):
#                 print("Insert column names")
#                 # todo 
#             elif(a=='Q' or a=='q'):
#                 exit()
#             elif(a=='0'):
#                 os.system("cls")
#                 break
#             else:
#                 os.system("cls")
#                 print("Press right number to continue or Q to close!")

    elif(a=='2'):
        print("Maybe later :)")
    elif(a=='Q' or a=='q'):
        exit()
    else:
        os.system("cls")
        print("Press right number to continue or Q to close!")

