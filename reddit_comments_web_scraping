# Retriv reddit data with provided Reddit API

#pip install praw
import praw
reddit = praw.Reddit(client_id='cu5G838LAXfh2A', 
                              client_secret='UsPOUQKhde79g1zdGKaB_A0hWyw', 
                              user_agent='E4523Project129')
#econ_subreddit = reddit.subreddit('Economics')
#results = econ_subreddit.controversial(time_filter='year',limit=1000)

#google_subreddit = reddit.subreddit('Google')
#results = google_subreddit.controversial(time_filter='year',limit=1000)

#amazon_subreddit = reddit.subreddit('Amazon')
#results = amazon_subreddit.controversial(time_filter='year',limit=1000)

#netflix_subreddit = reddit.subreddit('Netflix')
#results = netflix_subreddit.controversial(time_filter='year',limit=1000)

fb_subreddit = reddit.subreddit('Facebook')
results = fb_subreddit.controversial(time_filter='year',limit=1000)
#list(results)

topics_dict = { 'author':[],
               "text_link":[],
               "upvote_ratio":[],
               "title":[], 
                "score":[], 
                "id":[], 
               'comm':[],
               "url":[], 
                "comms_num": [],
               'comm_content':[], 
                "created": [], 
                "body":[]}

for submission in results:
    topics_dict["author"].append(submission.author)
    topics_dict["text_link"].append(submission.link_flair_text)
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["upvote_ratio"].append(submission.upvote_ratio)
    topics_dict["id"].append(submission.id)
    topics_dict["comm"].append(submission.comments)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    submission.comments.replace_more(limit=0)
    comm_list = []
    for comment in submission.comments.list():
        comm_list.append(comment.body)
    topics_dict["comm_content"].append(comm_list)



import pandas as pd
topics_data = pd.DataFrame(topics_dict)

topics_data.sort_values('created',inplace=True)

import datetime as dt
def get_date(created):
    return dt.datetime.fromtimestamp(created)
time_stamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = time_stamp)

#topics_data

#topics_data.to_csv('reddit_econ.csv', index=False) 
#topics_data.to_csv('reddit_google.csv', index=False) 
#topics_data.to_csv('reddit_amazon.csv', index=False) 
#topics_data.to_csv('reddit_netflix.csv', index=False) 
topics_data.to_csv('reddit_fb.csv', index=False) 
