from wkv_common import *

def username_has_capitals(username):
    if username.lower() != username:
        return 1
    else:
        return 0
