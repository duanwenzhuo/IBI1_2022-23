def buy_house(value,salary) :
    '''input: value, a postive int
              salary, a postive int
        returns yes if value is smaller than five times salary
    '''
    if value <= 5*salary:
        print('yes')
    else:
        print('no')

#example        
buy_house(90900,10000)