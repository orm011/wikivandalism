from wkv_common import *
import calendar
import time

def user_wiki_age_dif(username):
    query = 'http://en.wikipedia.org/w/api.php?action=query&list=users&ususers=' + username + '&format=json&usprop=blockinfo|groups|editcount|registration|emailable|gender'
    jsonobj = make_wikipedia_request_json(query)
    data = jsonobj[u'query'][u'users'][0]
    reg_date = data[u'registration']
    max_days = 2012*12*30+6*30
    year1 = int(reg_date[:4])
    month1 = int(reg_date[5:7])
    reg_days = year1*12*30+month1*30
    return max_days - reg_days
    
 
