wikivandalism
=============

6.857 project about vandalism in wikipedia

## Prereqs
sudo apt-get install redis-server
sudo pip install redis requests

## To add a feature
Create a file feature_name.py, containing a function which returns a numeric value (ex: see user_empty_comment_ratio.py)

    def feature_name(username):

Or if you need more than just username, start the name with 'edit' and you'll get a dictionary (ex: see edited_article_user_num_edits.py)

    def edit_feature_name(editinfo):

At top of wikipedia_requests.py, add:

    from feature_name import *

## To generate data for a feature

    ./featuredata.py feature_name

Will make a file feature_name.csv containing the data. First run will take a while because all the data from Wikipedia will have to be fetched; subsequent runs will be faster because the data will be cached.

Or manually:

    python
    >>> from wikipedia_request import *
    >>> feature_to_text(feature_name)

## To run the octave script for plotting a feature

    octave --silent plot_feature.m user_revision_count.csv

If you want to add a cutoff for making the feature a binary 1-0 value, add it as the last argument, ex:

    octave --silent plot_feature.m user_revision_count.csv 50

