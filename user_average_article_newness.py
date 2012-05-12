from wkv_common import *
import calendar
import time

def user_average_article_newness(editinfo):
    try:
        username = editinfo['user']
        query = 'http://en.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + username + '&uclimit=50&ucdir=older&format=json'
        jsonobj = make_wikipedia_request_json(query)
        data = jsonobj['query']['usercontribs']
        total = 0
        article_age = 0
        '''title1 = data[3]['title']
        query1 = 'http://en.wikipedia.org/w/api.php?action=query&titles=' + title1 + '&prop=info&inprop=protection&format=json'
        jsonobj2 = make_wikipedia_request_json(query1)
        return jsonobj2'''

        for article in data: 
	    title1 = article['title']
            query1 = 'http://en.wikipedia.org/w/api.php?action=query&titles=' + title1 + '&prop=info&inprop=protection&format=json'
            jsonobj2 = make_wikipedia_request_json(query1)
	    total += 1
            pages = jsonobj2['query']['pages'].keys()[0]
            touched_date = jsonobj2['query']['pages'][pages]['touched']
            max_days = 2012*12*30+6*30
            year1 = int(touched_date[:4])
            month1 = int(touched_date[5:7])
            day1 = int(touched_date[8:10])
            article_age = article_age + max_days - year1*12*30-month1*30-day1
        if total == 0:
            return 0
        else:
            return float(article_age)/total
    except:
        return 0
