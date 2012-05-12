from wkv_common import *
from user_is_ip_address import *

def user_num_groups(editinfo):
    if user_is_ip_address(editinfo):
        return 0
    username = editinfo['user']
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=users&ususers=' + username + '&format=json&usprop=blockinfo|groups|editcount|registration|emailable|gender'
    try:
        jsonobj = make_wikipedia_request_json(query)
        data = jsonobj[u'query'][u'users'][0]
        group_num = len(data[u'groups'])
        return group_num
    except:
        return 0
