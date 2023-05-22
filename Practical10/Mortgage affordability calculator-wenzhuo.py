def buy_house(value, salary) :
    '''input: value (int): The total value of the house
              salary (int): The purchaser's annual salary.
        Returns:
    str: "Yes" if the value is smaller than five times the salary, "No" otherwise.
    '''
    # Compare the value and the salary
    if value <= 5 * salary:
        return "Yes"
    else:
        return "No"

#example        
result = buy_house(90900,10000)
print(result)