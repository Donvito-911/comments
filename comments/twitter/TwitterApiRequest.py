from ..tokens import import_token
from .decorators import manage_response, require_token
import requests

class TwitterApiRequest:
    def _get_data(self, tweet_id: str, kwargs: dict):
        json = self.__get_request(tweet_id, kwargs)
        replies, users = json["data"], json["includes"]["users"]
        users_dict = {user["id"]: user for user in users}
        return replies, users, users_dict
    
    @require_token
    @manage_response
    def __get_request(self, tweet_id, kwargs: dict):
        academic_mode, max_replies, bearer_token = kwargs.get("academic_mode", False), kwargs.get("max_replies",10), import_token("twitter")
                                                    
        url = self.__create_url(tweet_id, max_replies, academic_mode)
        request = requests.get(url, headers = self.__create_headers(bearer_token))
        return request
    
    @staticmethod
    def __create_url(tweet_id, max_replies, academic_mode):
        url = "https://api.twitter.com/2/tweets/search/"
        url += "all" if academic_mode else "recent"
        url += f"?query=conversation_id:{tweet_id}&tweet.fields=conversation_id,referenced_tweets&expansions=author_id&user.fields=description,location&max_results={max_replies}"
        return url
    
    @staticmethod
    def __create_headers(bearer_token: str):
        return {"Authorization": f"Bearer {bearer_token}"}
    