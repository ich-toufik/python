num_of_tries = 0
while num_of_tries != 3:

    username = input('please insert your username or usereemail: ')
    password = input('please insert youre password: ')
    if username == 'toufik' and password == '123' :
        print('welcome home')
        num_of_tries = 0
        exit()
    else: 
        print('erorr login')
        num_of_tries +=1
        print('you have' + str (3 - num_of_tries) + " left ")
