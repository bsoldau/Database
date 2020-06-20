from os import system
class MyData:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status
    def show(self):
        print(f'    {self.name} {self.age} {self.status}')

data = []

def input_check(var):
    clear()
    print(f'''    {var} function \n
    You have {len(data)} records''') 
    if len(data) == 0:
        menu()
    try: 
        a = int(input('    Choose a record: ')) 
        if a < 1 or a > len(data):
            a/0  
    except:    
        print('Incorect input. Returning to main menu!')
        menu()  
    return a
     
def add():
    clear()
    print(f'Add record {len(data)+1}')
    a = input('Name: ')
    b = input('Age: ')
    c = input('Status: ')
    d = MyData(a,b,c)
    data.append(d)
    clear()
    menu()

def view(t):
    if t == 22:
        for i in range(0,len(data)):
            data[i].show()
        menu()    
    a = input_check('View')
    data[a-1].show() 
    menu()
    
def sort(): #ready
    a = input_check('Sort')
    b = input(' Select the target record: ')
    if str.isdigit(b) == False or int(b) > len(data) or int(b) < 1:
        print('Incorect input. Returning to main menu!')
        menu()
    c = data[a-1]
    data[a-1] = data[int(b)-1]
    data[int(b)-1] = c    
    print('Sort complete!')
    clear()
    menu()

def remove(t):
    if t == 44:
        print('Secret menu')
        y = input('You surely want to wipe all? y/n : ')
        if y == 'y' or y == 'Y':
            data.clear()
            print('Wipe complete!')
            menu()
    a = input_check('Remove')
    data.pop(a-1)
    print(f'Record {a} deleted!')
    menu()

def clear():  #ready
   _ = system('clear') 

def menu():
    print(f'''    ****************{len(data)}*******
    || 1. ADD    -> press 1
    || 2. VIEW   -> press 2
    || 3. SORT   -> press 3
    || 4. REMOVE -> press 4
    || 5. EXIT   -> press 5''')
    a = input ('    ||     Make a choise: ')
    clear()
    if a == '1':
        add()
    elif a == '2':
        view(2) 
    elif a == '22':
        view(22)        
    elif a == '3':
        sort()
    elif a == '4':
        remove(4) 
    elif a == '44':
        remove(44)    
    elif a == '5':
        exit(0)
    else:
        print('Wrong input...')
        menu()         

menu()
        
