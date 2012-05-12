from wkv_common import *

def username_has_capitals(editinfo):
    username = editinfo['user']
    if username.lower() != username:
        return 1
    else:
        return 0
