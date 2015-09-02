#!/usr/bin/env python3

#####################################
#CrawlsComments v0.1 by /u/9Ghillie #
#####################################


import praw
from datetime import datetime, timedelta
import time
import sys


#User agent
user_agent = "CrawlsComments v0.1 by /u/9Ghillie"
r = praw.Reddit(user_agent=user_agent)

#Login information
#Make a reddit account prior and inser login information below
r.login('INSERT USERNAME', 'INSERT PASSWORD', disable_warning=True)

#Fetch submission 
#Replace "submission_id='XXXXXX'" with post ID you want to crawl
#Submission ID can be found from the submission's URL: 
#http://www.reddit.com/r/SUBREDDIT/comments/SUBMIsSION_ID/SUBMISSION_TITLE
submission = r.get_submission(submission_id='XXXXXX')
forest_comments = submission.comments
submission.replace_more_comments(limit=None, threshold=0)
all_comments = submission.comments

def print_comment(comment, level=0):
    print('',comment.body.strip(), sep=4*level*' ')
    for reply in comment.replies:
        print_comment(reply, level=level+1)

for comment in all_comments:
    print_comment(comment)
