from os import system
class MyData:        #we will use a class with proper characteristics for each element
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status
    def show(self):
        print(f'    {self.name} {self.age} {self.status}')

data = []   #Here we will keep all the records

def input_check(var):   #the function will check if we are choosing something properly
    clear()             #and return the chosen position (if exists)
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
     
def add():      #The function is adding elements to the database
    clear()
    print(f'Add record {len(data)+1}')
    a = input('Name: ')
    b = input('Age: ')
    c = input('Status: ')
    d = MyData(a,b,c)
    data.append(d)
    clear()
    menu()

def view(t):    #This function will help us to view the elemnets of the database (use 22 to view all the elements)
    if t == 22:
        for i in range(0,len(data)):
            data[i].show()
        menu()    
    a = input_check('View')
    data[a-1].show() 
    menu()
    
def sort():     #Here we are changing positions between 2 elements of the database
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

def remove(t):     #Removing function of the elements (use 44 to remove everything)
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

def clear():    # Clears the display
   _ = system('clear') 

def menu():      #This will be the menu of our program
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
        
