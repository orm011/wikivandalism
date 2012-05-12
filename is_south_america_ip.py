from wkv_common import *
from user_is_ip_address import *
from ip_continent import *

def is_south_america_ip(editinfo):
  if not user_is_ip_address(editinfo):
    return 0
  username = editinfo['user']
  if get_continent(username) == 'SA':
    return 1
  return 0
