from wkv_common import *
from user_total_num_edits import *

def user_at_least_200_edits(editinfo):
    numedits = user_total_num_edits_real(editinfo)
    if numedits >= 200:
        return 1
    else:
        return 0

