import tweepy

# Substitua pelas suas chaves de acesso
api_key = 'API_KEY'
api_secret_key = 'API_SECRET_KEY'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

# Autenticação com o Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Substitua 'python' pela hashtag de seu interesse
hashtag = 'python'
for tweet in tweepy.Cursor(api.search, q='#' + hashtag).items(10): # Busca os últimos 10 tweets contendo a hashtag
    print(tweet.text)
