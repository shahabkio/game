#libraris
import math 
from random import randint
#get_data_path
def get_db_path():
    li = __file__.split('/')
    del li[-1]
    li = '/'.join(li)
    db_path = li + '/database.txt'
    return db_path

#decoding and loading  data
file = open(get_db_path())
txt = file.read()
code = 'x = ' + txt 
exec(code)
data = x.decode('utf-32')
exec(data)


#data_base_update 
def db_update():
    file = open(get_db_path() , mode = 'w')
    #erase the old contents
    file.truncate()
    txt = 'db = {}'.format(str(db))
    txt = txt.encode('utf-32')
    file.write(str(txt))
    


#main menu page 
def main_menu():
    
    print("="*40 ,  "welcome to guessing game" , "="*40)

    print("to create account press 1")
    print("to log into existing account press 2")


    while True:
        choice  = input("> ")

        if choice == "1":
            sign_up()
            break
        elif choice == "2":
            log_in()
            break
        else:
            continue

#sign_up page
def sign_up():
    print("="*40 ,  "sign_up page" , "="*40)

    #user_name section
    while True :
        User_Name = input("user_name :")
        
        if User_Name in db.keys() or not(User_Name.isalnum()) :
            print("user_name already exists")
            continue
        else:
            break
    
    #fullname section
    first_name = input("first name : ")
    last_name = input("last name : ")

     

    #password section 
    while True : 
        Password = input("password: ")
        Confirm_password = input("confirm_password: ")
        
        if Password == Confirm_password:
            break 
        else:
            continue 

    
    db[User_Name] = {'password' : Password , 'fullname' : first_name + ' ' + last_name , 'score' : 0}
    db_update()


#log_in system
def log_in():

    while True :
        user_name_check = input('user_name : ')
        password_check = input('password : ')

        if(user_name_check in db.keys()):
            if(password_check == db[user_name_check]['password']):
                if user_name_check == 'admin' :
                    admin_page()
                    break
                else:
                    print("log in successfuly")
                    account(user_name_check)
                    break
            else:
                print('user_name and password doesn\'t match')
                print('try again')
                continue


        else:
            print('user_name and password doesn\'t match')
            print('try again')
            continue

#admin page 
def admin_page():
    print("="*40 ,  "welcome mr shehab" , "="*40)
    print('options :- ')
    print('\tpress 1 to view database information')
    print('\tpress 2 to view source code')
    print('\tpress 3 to exit')
    admin_choice = input('> ')

    while True:

        if admin_choice == '1':

            for key in db.keys():

                print(key ,':-')
                for b_key in db[key].keys():
                    print(b_key , ':' , db[key][b_key] , sep=" ")
            break
        
        elif admin_choice == '2':

            src_code_path = __file__
            src_code = open(src_code_path , mode = 'r')
            print(src_code.read())
            break

        elif admin_choice == '3':
            exit()

        elif admin_choice == '4':
            start_game('admin')
            break

        else:
            continue



def number_gen(a,b):

    number = randint(a,b)
    return number

def account(user_name):

    player = user_name

    print(f'welcome {player}')
    #options
    

    while True:
        print('\tto start game press 1')
        print('\tto show your current score press 2') 
        print('\tto delete your account press 3')
        print('\tto exit press 4 ')
    

        choice = int(input('> '))

        if choice == 1:
            start_game(user_name)
            break
            

        if choice == 2:
            print('your current score {}'.format(db[player]['score']))
            continue

        if choice == 4:
            exit()
            
    

def start_game(user_name):
    score = db[user_name]['score']
    print(f' your score is {score}')

    #introduction
    print('-'*85)
    print('i have in my mind a number between 1 and 10')
    print('can you guess it')
    
    #number generator
    number = number_gen(1,10)
    guess = int(input('your guess: '))

    
    #checking answers 
    if guess == number :
        db[user_name]['score'] += 5 
        db_update()
        print('WOW , you are right')
        print('you are good at this')

    elif abs(guess-number) == 1 :
        print('too close') 
        print(f'my number was {number}')
        try_again(user_name)

    elif abs(abs(guess-number)) == 2 :

        print('close enough')
        print(f'my number was {number}')
        try_again(user_name)

    else:

        print('not even close')
        print(f'my number was {number}')
        try_again(user_name)

        
def try_again(user_name):

    print('do you want to try again (Y or N) ? ')
    choice = input('> ')

    if choice == 'y' or choice == 'Y':
        start_game(user_name)

    elif choice == 'N' or choice == 'n':
        print('going back to main menu ....')
        account(user_name)



main_menu()