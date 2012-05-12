from wkv_common import *
from user_is_ip_address import *
from ip_continent import *

def is_australia_ip(editinfo):
  if not user_is_ip_address(editinfo):
    return 0
  username = editinfo['user']
  if get_continent(username) == 'OC':
    return 1
  return 0
