from wkv_common import *

def user_is_bot(editinfo):
    username = editinfo['user']
    if 'bot' in username.lower():
        return 1
    else:
        return 0
