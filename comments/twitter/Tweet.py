from .TwitterApiRequest import TwitterApiRequest
import pandas as pd

class Tweet(TwitterApiRequest):
    def __init__(self, tweet_id, **kwargs):
        """**kwargs: max_replies, bearer_token, username, academic_mode"""
        self.id = str(tweet_id)
        self.username = kwargs.get("username")
        self.replies, self.users, self.__users_dict = self._get_data(tweet_id, kwargs)
        
    def get_dataframe(self):
        columns = ["original_tweet_id","original_tweet_username","id","username","name","text","location","description"]
        data = []
        for reply in self.replies:
            if reply["referenced_tweets"][0]["id"] == self.id: # filter replies to the original tweet (i.e., no replies to a reply)
                user_info = self.__users_dict[reply["author_id"]]
                observation = [self.id, self.username, user_info["id"], user_info["username"], user_info["name"],
                               reply["text"],user_info.get("location", ""), user_info["description"]]
                data.append(observation)
                
        return pd.DataFrame(data, columns = columns)
    