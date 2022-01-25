BEARER_TOKENS = {"facebook": False, "twitter": False}

def set_tokens(facebook = False, twitter = False):
    global BEARER_TOKENS
    BEARER_TOKENS.update(facebook = facebook, twitter = twitter)

def set_twitter_token(token: str):
    global BEARER_TOKENS
    BEARER_TOKENS.update(twitter = token)
    
def set_facebook_token(token: str):
    global BEARER_TOKENS
    BEARER_TOKENS.update(facebook = token)

def import_token(platform: str):
    return BEARER_TOKENS[platform]