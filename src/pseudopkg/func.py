
def take_input():
    a = input('Enter anything: ') # cannot be run by pytest
    return a

def to_uppercase(a):
    print(a.upper()) # gets printed out in tests, too
    return a.upper()

def run_all():
    a = take_input() # breaks pytest, check inlince function comment of this
    return write_out_uppercase(a)
