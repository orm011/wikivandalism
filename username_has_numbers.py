from wkv_common import *

def username_has_numbers(editinfo):
    username = editinfo['user']
    origusername = username
    numbers = [0,1,2,3,4,5,6,7,8,9]
    numbers = [str(x) for x in numbers]
    for x in numbers:
        username = username.replace(x, '')
    if origusername != username:
        return 1
    else:
        return 0
