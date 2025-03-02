# data enty added functionality we get from User

from datetime import datetime

dateFormat = "%d-%m-%Y"
CATEGORIES = {'I':'Income' ,'E':'Expense'}
def get_date(prompt, allow_default= False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(dateFormat) #if nothing pressed and entered it will take todays date
    try:
        valid_date = datetime.strptime(date_str,dateFormat)  # validated 
        return valid_date.strftime(dateFormat)
    except ValueError:
        print("Invalid Date Format. Enter {dd-mm-yyyy} format")
        return get_date(prompt,allow_default) #recurcive function

def get_amount():
    try:
        amount =float(input("Enter your amount: "))
        if amount<= 0:
            print("Amount should be a non-negative non-zero value")
        else:
            return amount
    except ValueError as e:
        print(e)
        return get_amount() # recurcise till we land on try            

def get_category():
    category = input("Enter you Category 'I' for 'Income' & 'E' for 'Expense' ").upper()
    if category in  CATEGORIES:
        return CATEGORIES[category]
    else:
        print("Invalid Category, Please Select Between 'I' for 'Income' & 'E' for 'Expense'") 
        return get_category()     

def get_description():
    return input("Enter Description (optional)")        