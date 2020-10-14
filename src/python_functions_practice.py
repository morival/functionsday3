def return_10():
    return 10 


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y 

def multiply(x,y):
    return x*y 

def divide(x,y):
    return x/y

def length_of_string(string_length):
    return len(string_length)

def join_string( string_1, string_2 ):
    return add(string_1, string_2)

def add_string_as_number(x,y):
    # return int(x) + int(y)
    return add(int(x),int(y))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def number_to_full_month_name(num):
    return months[num-1]

months_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def number_to_short_month_name(num):
    return months_short[num-1]

def volume_of_cube(length):
    return length**3 

def reverse_string(rev):
    return rev[::-1]

def fahrenheit_to_celsius(far):
    return (far - 32)*(5.0/9.0)