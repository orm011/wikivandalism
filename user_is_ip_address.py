from wkv_common import *

def user_is_ip_address(editinfo):
    username = editinfo['user']
    if username.count('.') != 3:
        return 0
    try:
        v = int(username.replace('.', ''))
    except:
        return 0
    return 1

