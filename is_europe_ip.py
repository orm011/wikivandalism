from wkv_common import *
from user_is_ip_address import *
from ip_continent import *

def is_europe_ip(editinfo):
  if not user_is_ip_address(editinfo):
    return 0
  username = editinfo['user']
  return int(ip_is_europe(username))
