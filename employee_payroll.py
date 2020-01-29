print('********************************EMPLOYEE PAYROLL*******************************************************')
main_list=[]
'''this is the main list that all the details are stored'''  
from _datetime import date
from _ast import Or
def entering_input(count):
    '''this is to enter new employee details'''
    for j in range(0,count):
        a=[]
        for i in range(0,4):
            
                if i==0:
                    b=input("Enter employee id")
                elif i==1:
                    b=input('Enter employee name')
                elif i==2:
                    print('Enter date of joining')
                    day = int(input('Enter a day'))
                    month = int(input('Enter a month'))
                    year = int(input('Enter a year'))
                    b=date(year,month,day)
                elif i==3:
                    b=input('enter the salary/annum(!Digits Only)')
                a.append(b)
        print('the given list is',a)
        main_list.append(a)
        print('----------------------------------------------')
    main_func()
def all_details():
    '''this function is to display all employee details'''
    print('You  have selected 2st operation \n---------------------------------')
    if len(main_list)==0:
        print('The list is empty,Enter values first \n------------------------------')
    else: 
        print('The list of employees \n----------------------------------')
        '''this function for displaying all employee details'''
        for x in range(len(main_list)): 
            print ('ID:',main_list[x][0])
            print ('Name:',main_list[x][1])
            print ('DoJ:',main_list[x][2]) 
            print ('Salary:',main_list[x][3])
            print('--------------------------------') 

    main_func()
def search():
    '''this function is to search with employee details'''
    if main_list==[]:
        print('FIRST ENTER THE DETAILS !')
        main_func()
    print('You  have selected 3st operation \n*******************************')
    ip=input('enter the key word to search(name,ID,salary) \n-----------------------------------')
    for k in range(0,len(main_list)):
        #name search
        if ip==main_list[k][1]:
            print('search done.\n+++++++++++++++++++')
            print ('ID:',main_list[k][0])
            print ('Name:',main_list[k][1])
            print ('DoG:',main_list[k][2]) 
            print ('Salary:',main_list[k][3])
            print('--------------------------------') 
            #ID search
        elif ip==main_list[k][0]:
            print('search done.\n+++++++++++++++++++')
            print ('ID:',main_list[k][0])
            print ('Name:',main_list[k][1])
            print ('DoG:',main_list[k][2]) 
            print ('Salary:',main_list[k][3])
            print('--------------------------------')
            #Salary search 
        elif ip==main_list[k][3]:
            print('search done.\n+++++++++++++++++++')
            print ('ID:',main_list[k][0])
            print ('Name:',main_list[k][1])
            print ('Salary:',main_list[k][3])
            print('--------------------------------')
        elif ip!=main_list[k][1] or ip!=main_list[k][0] or ip!=main_list[k][3]:
            print('no such employee or parameter') 
            break 
            
    main_func() 
def update():
    if main_list==[]:
        print('FIRST ENTER THE DETAILS !')
        main_func()
    '''this function is to update the existing list'''
    inp=input('enter the Id of employee you want to update \n-----------------------------------\n')
    for l in range(0,len(main_list)):
        if inp!=main_list[l][0]:
            print('No such employee !')
            main_func()
           
    for l in range(0,len(main_list)):
        if inp==main_list[l][0]:
            print ('ID:',main_list[l][0])
            print ('Name:',main_list[l][1])
            print ('DoG:',main_list[l][2]) 
            print ('Salary:',main_list[l][3])
            print('--------------------------------') 
    dchoose=input('press 0 for update the date else press1')
    '''this input will differentiate the date from other parameters'''
    if dchoose=='0':
        print('Enter date of joining')
        day = int(input('Enter a day'))
        month = int(input('Enter a month'))
        year = int(input('Enter a year'))
        b=date(year,month,day)
        main_list[l][2]=b
        print('Update Done..\n--------------------------------------------')
        print ('ID:',main_list[l][0])
        print ('Name:',main_list[l][1])
        print ('DoG:',main_list[l][2]) 
        print ('Salary:',main_list[l][3])
        print('--------------------------------') 
    elif dchoose=='1':
        up=input('enter the parameter to change:')
        for m in range(0,len(main_list)):
            for n in range(0,4):
                if up==main_list[m][n]:
                    new_value=input('enter new parameter:')
                    main_list[m][n]=new_value
                    print('Update Done..\n--------------------------------------------')
                    print ('ID:',main_list[m][0])
                    print ('Name:',main_list[m][1])
                    print ('DoG:',main_list[m][2]) 
                    print ('Salary:',main_list[m][3])
                    print('--------------------------------') 
    main_func()            
def main_func():
    '''this function calls all other functions'''
    b=int(input('  \t OPERATIONS \n --------------------------------------\n *enter new employee details,press:1 \n *To display list of employees,press:2 \n *To search employee details press:3 \n *To update any employee details press:4 \n*****************************************\n'))
    if b==1:
        print('You  have selected 1st operation \n________________________________________')
        entering_input(int(input('What is the count of new employees')))
    elif b==2:
        all_details()
    elif b==3:
        search()
    elif b==4:
        update()
    else:
        print('Invalid Input,Please Enter appropriate Input')
        main_func()
main_func()











 
