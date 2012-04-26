import requests
import simplejson
import csv

""" for the example only"""
import trial_file_reader


__wikipedia_query="http://en.wikipedia.org/w/api.php?action=query"

def construct_user_page_edits_request(username, limit):
    """constructs wikipedia query for user page edits"""
    return  __wikipedia_query + "&titles=User:" + username + "&prop=revisions" + "&format=json" + "&rvlimit="  + str(limit)

def construct_user_talk_page_edits_request(username, limit):
    return  __wikipedia_query + "&titles=User_talk:" + username + "&prop=revisions" + "&format=json" + "&rvlimit="  + str(limit)

def construct_user_talk_page_contents_request(username, limit):
    return  __wikipedia_query + "&titles=User_talk:" + username + "&prop=revisions&rvprop=comment|tags|content" + "&format=json" + "&rvlimit="  + str(limit)

class WikipediaError(Exception):
    pass


def make_wikipedia_request(req):
    """connects to wikipedia and collects answer"""
    try:
        res = requests.get(req)
        if not res.ok:
            raise  WikipediaError, res.error
    except:
            raise  WikipediaError
        
    return res.text

def make_wikipedia_request_json(req):
    jsontext = make_wikipedia_request(req)
    return simplejson.loads(jsontext)

def get_user_page_revisions(json_result):
    """returns a list of page edits"""
    parsed = simplejson.loads(json_result)
    try:
        return parsed.items()[0][1].items()[0][1].values()[0]['revisions']
    except:
        ##users without profile have no results in revisions
        return []

def user_revision_count(username):
    """actual feature, connects to wikpedia"""
    req = construct_user_page_edits_request(username,500)
    return len(get_user_page_revisions(make_wikipedia_request(req)))

def user_talk_revision_count(username):
    req = construct_user_talk_page_edits_request(username, 500)
    try:
        count = len(make_wikipedia_request_json(req)['query']['pages'].values()[0]['revisions'])
    except:
        count = 0

    return count

def join_edits_with_feature_on_user(feature_function, edits):
    """edits are the output from parsing trial.xml"""
    result = []
    for edit in edits:
        try:
            result.append((feature_function(edit['user']), 
                           int(edit['isVandalism'] == 'true')))
        except:
            print 'error requesting for: ', edit['user'], 'moving on...'
            
    return result

def dump_to_csv(tuple_list, file_name):
    f = open(file_name, "w")
    wr = csv.writer(f)
    for tup in tuple_list:
        wr.writerow(tup)
    f.close()
    
def example():
    """example of how you can use the functions in this file"""
    trialxmlpath = "../workspace/cluebotng/editsets/D/trial.xml"
    trainingset = trial_file_reader.parse_trial_file(trialxmlpath)
    exampleset = trainingset[0:10]
    examplefeature = user_talk_revision_count #user feature defined above
    x = join_edits_with_feature_on_user(examplefeature, exampleset)
    dump_to_csv(x, "examplefeature.csv")

def feature_to_text(feature_function, trialxmlpath, number_of_examples):
    """use this to get a new feature for the dataset stored into a file"""
    trainingset = trial_file_reader.parse_trial_file(trialxmlpath)
    exampleset = trainingset[0:number_of_examples]
    x = join_edits_with_feature_on_user(feature_function, exampleset)
    filename = feature_function.__name__ + '.csv'
    dump_to_csv(x, filename)


def user_talk_vandal_vocab_count(username):
    req = construct_user_talk_page_contents_request(username, 500)
    jsontxt = make_wikipedia_request(req)
    vandalvocab = ['unconstructive', 'revert', 'vandal', 'block', 'warn']
    wordsInText = jsontxt.replace(',', ' ').split(' ')
    vandalwordcount = 0
    for vandalword in vandalvocab:
        for w in wordsInText:
            if vandalword in w:
                vandalwordcount += 1
    return vandalwordcount
