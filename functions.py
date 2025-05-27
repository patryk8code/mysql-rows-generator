import os
# this is very first menu
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def Menu0():
    print("1: Start generating")
    print("2: More info")
    print("Q: Close program")

def MoreInfo():
    print(bcolors.HEADER + "This generator will generate fake/trash data\nIt will help you learn make operation in database in SQL :)" + bcolors.ENDC)

def InsertNames():
    print("0: Use random column names")
    print("Insert column name: ")

# These are the selectable data type options that can be generated.
def DataTypes():
    print("0: end")
    print("1: INT")
    print("2: STRING")
    print("3: BOOL")
    print("4: DECIMAL")
    print("5: DATE")
    print("6: DATETIME")
    print("7: TIME")
    print("8: YEAR")
    print("D: Delete Column")

def InsertDataTypes(file):
    ColumnTypes=[]
    DataTypes()
    ColumnName=open(file,'r')
    DATA=[]
    for i in ColumnName:
        DATA.append(i)
    for i in DATA:
        while(True):
            os.system("cls")
            DataTypes()
            a=input('Type for\'' + i[0:len(i)-1] + '\': ')
            if (a == '0'):
                # AFTER COLUM TYPES INSERT
                GenerateRows(ColumnName,ColumnTypes)
                break
            if (a == 'D' or a=='d'):
                ColumnTypes.append('0')
            elif (a == '1'):
                ColumnTypes.append('1')
            elif (a == '2'):
                ColumnTypes.append('2')
            elif (a == '3'):
                ColumnTypes.append('3')
            elif (a == '4'):
                ColumnTypes.append('4')
            elif (a == '5'):
                ColumnTypes.append('5')
            elif (a == '6'):
                ColumnTypes.append('6')
            elif (a == '7'):
                ColumnTypes.append('7')
            elif (a == '8'):
                ColumnTypes.append('8')
            else:
                print(bcolors.WARNING +"Something is wrong.."+ bcolors.ENDC)
                continue
            break
    ColumnName.close()
    column_write=open(file,'w')
    j=0
    for i in DATA:
        if(ColumnTypes[j]=='0'):
            j=j+1
            continue
        column_write.write(i[0:len(i)-1]+' '+ColumnTypes[j]+'\n')
        j=j+1

def GenerateRows(Names,Types):
    how_much_rows=input("Number of rows: ")
    ROWS="INSERT INTO COLUMN("
    try:
        how_much_rows=int(how_much_rows)
        if (how_much_rows>0 and how_much_rows<=1000000000):
            for i in Names:
                ROWS=ROWS+"\""+i+"\","
            ROWS=ROWS+") VALUES "
        else:
            print("Type number from 1 to 1 000 000 000") 
    except:
        print("Type NUMBERS !")
    a=input("asdaaa")

# additional opts
# like id starts from.. zakresy???? nah?

    #     if(how_much_rows.isnumeric()):
    #         how_much_rows=int(how_much_rows)
    #         if(how_much_rows>=0):
    #             break
    #         elif(how_much_rows==-1):
    #             insert_ColumnNames()
    #             break
    #     else:
    #         os.system("cls")
    #         print("Wrong!! type NUMBERS")

# save_to_file="INSERT INTO ___TABLE___ "
#     if(list_of_columns_names):
#         save_to_file="INSERT INTO ___TABLE___ ("
#         for i in list_of_columns_names:
#             save_to_file+=i+", "
#         save_to_file=save_to_file[:-2]
#         save_to_file+=") VALUES "
#     else:
#         save_to_file+="VALUES "
#     for i in range(how_much_rows):
#         save_to_file+=generate_row(i)
#     print("Now check file \"data.txt\"")
    
#     f = open("data.txt", "w")
#     f.write(save_to_file[:-2]+";")
#     f.close()

