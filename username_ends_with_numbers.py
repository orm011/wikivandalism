from wkv_common import *

def username_ends_with_numbers(editinfo):
    username = editinfo['user']
    numbers = [0,1,2,3,4,5,6,7,8,9]
    numbers = [str(x) for x in numbers]
    for x in numbers:
        if username[-1:] == x:
            return 1
    return 0
