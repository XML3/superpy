from datetime import date, timedelta

#Global variable to store current date
current_date = date.today()

def get_current_date():
    return current_date

def set_current_date(new_date): 
    global current_date
    current_date = new_date
    
    #advances the global variable by specified nnumber of days.
def advance_current_date(days):
    global current_date
    current_date += timedelta(days=days)