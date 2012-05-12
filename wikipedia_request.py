import requests
import simplejson
import csv

""" for the example only"""
import trial_file_reader


from user_talk_vandal_vocab_count import *
from user_talk_vandal_vocab_ratio import *
from user_revision_count import *
from user_talk_revision_count import *
from user_article_to_edit_ratio import *
from user_empty_comment_ratio import *
from user_comment_avg_length import *
from user_edit_to_reversion_ratio import *

#from user_external_link_ratio import *

from edited_article_user_num_edits import *
from user_has_edited_talk_page import *

from user_is_ip_address import *
from user_is_bot import *
from user_uses_editing_tool import *
from username_has_capitals import *
from username_has_numbers import *
from username_ends_with_numbers import *
from editor_started_article import *

from article_is_biography import *
from article_is_protected import *

from is_asia_ip import *
from is_europe_ip import *
from is_north_america_ip import *
from is_australia_ip import *
from is_africa_ip import *
from is_south_america_ip import *

def join_edits_with_feature_on_user(feature_function, edits):
    """edits are the output from parsing trial.xml"""
    result = []
    for edit in edits:
        try:
            featureval = 0
            featureval = feature_function(edit)
            result.append((featureval, 
                           int(edit['isVandalism'] == 'true')))
        except:
            print 'error requesting for: ', edit['user'], 'moving on...'
            
    return result

def join_editid_with_feature(feature_function, edits):
    """edits are the output from parsing trial.xml"""
    result = []
    for edit in edits:
        try:
            featureval = 0
            featureval = feature_function(edit)
            result.append((edit['EditID'], featureval))
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

def feature_to_text(feature_function, number_of_examples=10, trialxmlpath = "../workspace/cluebotng/editsets/D/trial.xml"):
    """use this to get a new feature for the dataset stored into a file"""
    print 'reading training set from ' + trialxmlpath
    trainingset = trial_file_reader.parse_trial_file(trialxmlpath)
    print 'done reading training set'
    if number_of_examples <= 0:
        exampleset = trainingset[:]
    else:
        exampleset = trainingset[0:number_of_examples]
    x = join_edits_with_feature_on_user(feature_function, exampleset)
    filename = feature_function.__name__ + '.csv'
    dump_to_csv(x, filename)

def editid_to_featurevalues(feature_function, trialxmlpath = "../workspace/cluebotng/editsets/D/trial.xml"):
    """use this to get a new feature for the dataset stored into a file"""
    print 'reading training set from ' + trialxmlpath
    exampleset = trial_file_reader.parse_trial_file(trialxmlpath)
    print 'done reading training set'
    x = join_editid_with_feature(feature_function, exampleset)
    filename = feature_function.__name__ + '.dat'
    dump_to_csv(x, filename)



