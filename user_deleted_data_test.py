from wkv_common import *

#This does not work because of permission denied
'''def user_deleted_data_test(username):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=deletedrevs&druser=' + username + '&drlimit=500&format=json'
    jsonobj = make_wikipedia_request_json(query)
    return jsonobj'''

