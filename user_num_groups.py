from wkv_common import *

def user_num_groups(username):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=users&ususers=' + username + '&format=json&usprop=blockinfo|groups|editcount|registration|emailable|gender'
    jsonobj = make_wikipedia_request_json(query)
    data = jsonobj[u'query'][u'users'][0]
    group_num = len(data[u'groups'])


    return group_num
