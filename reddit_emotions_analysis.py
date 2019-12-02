import pandas as pd
import csv
import re
import datetime
import numpy as np
import csv

#retrieving the web-scrapped reddit comment data
reddit_fb = pd.read_csv("/Users/wangzhidan/Desktop/data/reddit_fb.csv")
reddit_am = pd.read_csv("/Users/wangzhidan/Desktop/data/reddit_amazon.csv")
reddit_nf = pd.read_csv("/Users/wangzhidan/Desktop/data/reddit_netflix.csv")
reddit_gg = pd.read_csv("/Users/wangzhidan/Desktop/data/reddit_google.csv")
reddit_econ = pd.read_csv("/Users/wangzhidan/Desktop/data/reddit_econ.csv")

#emotions analysis with NRC emotion lexicon lists
def get_nrc_data():
    nrc = "/Users/wangzhidan/Desktop/Data_Analytics/data/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt"
    count = 0
    emotion_dict=dict()
    with open(nrc,'r') as f:
        all_lines = list()
        for line in f:
            if count < 46:
                count+=1
                continue
            line = line.strip().split('\t')
            if int(line[2]) == 1:
                if emotion_dict.get(line[0]):
                    emotion_dict[line[0]].append(line[1])
                else:
                    emotion_dict[line[0]] = [line[1]]
    return emotion_dict


def emotion_analyzer(text,emotion_dict=get_nrc_data()):
    #Set up the result dictionary
    emotions = {x for y in emotion_dict.values() for x in y}
    emotion_count = dict()
    for emotion in emotions:
        emotion_count[emotion] = 0

    #Analyze the text and normalize by total number of words
    if isinstance(text, float):
        return [emotion_count.values()]
    else:
        total_words = len(text.split())
        for word in text.split():
            if emotion_dict.get(word):
                for emotion in emotion_dict.get(word):
                    emotion_count[emotion] += 1/len(text.split())
    return [emotion_count.values()]

#return emotions with these emotion analysis
def return_emotions(reddit_df):
    count = 0
    
    columns = ['anticipation', 'sadness', 'joy', 'negative', 'trust', 'positive', 'surprise', 'disgust', 'anger', 'fear']
    title_emotions = pd.concat([pd.DataFrame(emotion_analyzer(i), columns=columns) 
                          for i in reddit_df['title']],
           ignore_index=True)
    comm_emotions = pd.concat([pd.DataFrame(emotion_analyzer(j), columns=columns) 
                          for j in reddit_df['comm_content']],
           ignore_index=True)
    
    body_emotions = pd.concat([pd.DataFrame(emotion_analyzer(k), columns=columns) 
                          for k in reddit_df['body']],ignore_index=True)
    total_emotions = title_emotions + comm_emotions + body_emotions
    return total_emotions
    
## Getting Facebook reddit emotions and write into a csv file
reddit_fb_emotions = pd.concat([reddit_fb, return_emotions(reddit_fb)], axis=1, sort=False)
reddit_fb_emotions.to_csv(r'fb_reddit_emotions.csv', index = None, header = True)

#Getting Amazon reddit emotions and write into a csv file
reddit_am_emotions = pd.concat([reddit_am, return_emotions(reddit_am)], axis=1, sort=False)
reddit_am_emotions.to_csv(r'am_reddit_emotions.csv', index = None, header = True)

## Getting Netflix reddit emotions and write into a csv file
reddit_nf_emotions = pd.concat([reddit_nf, return_emotions(reddit_nf)], axis=1, sort=False)
reddit_nf_emotions.to_csv(r'nf_reddit_emotions.csv', index = None, header = True)

## Getting Google reddit emotions and write into a csv file
reddit_gg_emotions = pd.concat([reddit_gg, return_emotions(reddit_gg)], axis=1, sort=False)
reddit_gg_emotions.to_csv(r'gg_reddit_emotions.csv', index = None, header = True)

## Getting Economy reddit emotions and write into a csv file
reddit_econ_emotions = pd.concat([reddit_econ, return_emotions(reddit_econ)], axis=1, sort=False)
reddit_econ_emotions = pd.concat([reddit_econ, return_emotions(reddit_econ)], axis=1, sort=False)
    
    
