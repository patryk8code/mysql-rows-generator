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
def menu0():
    print("1: Start generating")
    print("2: More info")
    print("Q: Close program")

def more_info():
    print(bcolors.HEADER + "This generator will generate fake/trash data\nIt will help you learn make operation in database in SQL :)" + bcolors.ENDC)

def insert_names():
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
    print("9: Delete last one")
    print("Q: back")
