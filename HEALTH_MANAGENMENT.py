
# FOR TIME
def gettime():
    import datetime
    return datetime.datetime.now()

# FOR ABDUL FOOD
def abdul_food():
    f=open('abdul_food.txt','a')
    food_1 = input('Enter Your Food : ')
    time_1 =str(gettime())
    f.write(time_1)
    f.write('\t')
    f.write(food_1)
    f.write('\n')
    f.close()

# FOR ABDUL EXCERCIES
def abdul_exe():
    f1=open('abdul_exe.txt','a')
    exe_1 = input('Enter Your Excercies : ')
    time_1 =str(gettime())
    f1.write(time_1)
    f1.write('\t')
    f1.write(exe_1)
    f1.write('\n')
    f1.close()

# FOR SAQUIB FOOD
def saquib_food():
    f2=open('saquib_food.txt','a')
    food_2 = input('Enter Your Food : ')
    time_1 =str(gettime())
    f2.write(time_1)
    f2.write('\t')
    f2.write(food_2)
    f2.write('\n')
    f2.close()

# FOR SQUIB EXCERCIES
def saquib_exe():
    f3=open('saquib_exe.txt','a')
    exe_2 = input('Enter Your Excercies : ')
    time_1 =str(gettime())
    f3.write(time_1)
    f3.write('\t')
    f3.write(exe_2)
    f3.write('\n')
    f3.close()

# FOR MALIK FOOD
def malik_food():
    f4=open('malik_food.txt','a')
    food_3 = input('Enter Your Food : ')
    time_1 =str(gettime())
    f4.write(time_1)
    f4.write('\t')
    f4.write(food_3)
    f4.write('\n')
    f4.close()

# FOR MALIK EXCERCIES
def malik_exe():
    f5=open('malik_exe.txt','a')
    exe_3 = input('Enter Your Excercies : ')
    time_1 =str(gettime())
    f5.write(time_1)
    f5.write('\t')
    f5.write(exe_3)
    f5.write('\n')
    f5.close()

# reading of text file. abdul, saquib, malik

# for abdul
def abdul_f():
    f6 = open('abdoul_food.txt')
    fr = f6.read()
    print(fr)
    f6.close()

def abdul_e():
    f7 = open('abdul_exe.txt')
    fr1 = f7.read()
    print(fr1)
    f7.close()

# for saquib

def saquib_f():
    f8 = open('saquib_food.txt')
    fs = f8.read()
    print(fs)
    f8.close()

def saquib_e():
    f9 = open('saquib_exe.txt')
    fs1 = f9.read()
    print(fs1)
    f9.close()

# for malik

def malik_f():
    f10 = open('malik_food.txt')
    ft = f10.read()
    print(ft)
    f10.close()

def malik_e():
    f11 = open('malik_exe.txt')
    ft1 = f11.read()
    print(ft1)
    f11.close()



while True:

    print('FOR WRITE OR READ , END THE PROGRAM. PRESS 1 OR 2 OR 3 RESPECTIVELY ')
    a = int(input('Enter Your Choice : '))

    if a == 1:
        # FOR WRITE
        print('FOR ABDUL , SAQUIB , MALIK , CHOSE 1,2,3 RESPECTIVELY')
        b = int(input('Enter Your choice : '))
    # FOR ABDUL
        if b == 1:
            print('FOR FOOD AND EXCERCIES , PRESS 1,2 RESPECTIVELY')
            c = int(input('Enter Your Choice : '))
            if c == 1:
                abdul_food()
            elif c == 2:
                abdul_exe()
            else:
                print('You are press wroung key so programwill start fro first'
                    ' positin')
    # FOR SAQUIB
        elif b == 2:
            print('FOR FOOD AND EXCERCIES , PRESS 1,2 RESPECTIVELY')
            c1 = int(input('Enter Your Choice : '))
            if c1 == 1:
                saquib_food()
            elif c1 == 2:
                saquib_exe()
            else:
                print('You are press wroung key so programwill start fro first'
                      ' positin')
    # FOR MALIK
        elif b == 3:
            print('FOR FOOD AND EXCERCIES , PRESS 1,2 RESPECTIVELY')
            c2 = int(input('Enter Your Choice : '))
            if c2 == 1:
                malik_food()
            elif c2 == 2:
                malik_exe()
            else:
                print('You are press wroung key so programwill start fro first'
                      ' positin')

    elif a == 2:
    # FOR READ
        print('FOR ABDUL , SAQUIB , MALIK , CHOSE 1,2,3 RESPECTIVELY')
        b1 = int(input('Enter Your choice : '))
    # FOR ABDUL
        if b1 == 1:
            print('FOR FOOD AND EXCERCIES , PRESS 1,2 RESPECTIVELY')
            c3 = int(input('Enter Your Choice : '))
            if c3 == 1:
                abdul_f()
            elif c3 == 2:
                abdul_e()
            else:
                print('You are press wroung key so programwill start fro first'
                      ' positin')
    # FOR SAQUIB
        elif b1 == 2:
            print('FOR FOOD AND EXCERCIES , PRESS 1,2 RESPECTIVELY')
            c4 = int(input('Enter Your Choice : '))
            if c4 == 1:
                saquib_f()
            elif c4 == 2:
                saquib_e()
            else:
                print('You are press wroung key so programwill start fro first'
                      ' positin')
    # FOR MALIK
        elif b1 == 3:
            print('FOR FOOD AND EXCERCIES , PRESS 1,2 RESPECTIVELY')
            c5 = int(input('Enter Your Choice : '))
            if c5 == 1:
                malik_f()
            elif c5 == 2:
                malik_e()
            else:
                print('You are press wroung key so programwill start fro first'
                      ' positin')

    elif a == 3:
        quit()

    else:
        print('YOU ARE CHOSE WROUNG INPUT')

