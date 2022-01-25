import pandas as pd
from .Tweet import Tweet

def generate_twitter_db(tweets: list, **kwargs):
    """**kwargs: max_replies, academic_mode, filename, save"""
    list_dfs = [Tweet(tweet["id"], username = tweet["username"], **kwargs).get_dataframe() for tweet in tweets]
    database = pd.concat(list_dfs, ignore_index = True)
    if kwargs.get("save", False):
        database.to_csv(kwargs.get("filename", "replies") + ".csv", index = False)
    return database