from wkv_common import *

def editor_started_article(editinfo):
    if editinfo['creator'] == editinfo['user']:
        return 1
    else:
        return 0
