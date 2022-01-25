from functools import wraps
from ..tokens import import_token

def manage_response(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        request = fn(*args,**kwargs)
        json = request.json()
        if request.status_code == 200:
            if json["meta"]["result_count"] == 0:
                class NoRepliesFound(Exception): pass
                raise NoRepliesFound(f"Make sure the tweet has replies. If the tweet was posted more than 7 days ago, make sure you have academic_mode activated (Permissions of Research Academic required).\n Rectify these 2 possible cases, but it could be other case that led to 0 replies. \n\n Twitter API Response: {json}")
            return json
        elif request.status_code == 401:
            class Unauthorized(Exception): pass
            raise Unauthorized(f"Your Bearer token didnt connect into Twitter API. \n\n Twitter API Response: {json}")

        elif request.status_code == 403:
            class AuthorizationError(Exception): pass
            raise AuthorizationError(f"You may not have the proper access level (i.e. Research Academic) or you haven't setup your Twitter API project/app properly. \n\n Twitter API Response: {json}")
            
        else:
            raise BaseException(f"An error occured: Twitter API response: {json}")
    return wrapper

def require_token(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        BEARER_TOKEN = import_token("twitter")
        if not BEARER_TOKEN:
            class BearerToken(Exception): pass
            raise BearerToken("You haven't set up your bearer token, you must import set_tokens or set_token and set a bearer token in order to interact with the Twitter API")
        else:
            return fn(*args,**kwargs)
    return wrapper