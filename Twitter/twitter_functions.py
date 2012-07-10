import twitter
import util

# city id for getting tweets by location
PHILA_WOEID = 2471217

# commenting 
def search(searchTerm):
    """
    Print recent tweets containing `searchTerm`.
    """
    api = twitter.Api()
    tweets = api.GetSearch(searchTerm)
    for tweet in tweets:
        util.safe_print(tweet.GetText())

def trendingTopics():
    """
    Print the currently trending topics.
    """
    api = twitter.Api()

    trending_topics = api.GetTrendsWoeid(PHILA_WOEID)
    for topic in trending_topics:
        util.safe_print(topic.name)

def userTweets(username):
    """
    Print recent tweets by `username`.
	pass #pass is a placeholder for where the code will go, so it doesn't break rest of code when run
    """
    api = twitter.Api()
    user_tweets = api.GetUserTimeline(username)
    for tweet in user_tweets:
        util.safe_print(tweet.GetText())
#    pass

def trendingTweets():
    """
    Print tweets for all the trending topics.
    """
    api = twitter.Api()
    trending_topics = api.GetTrendsWoeid(PHILA_WOEID)
    for topic in trending_topics:
        topicSearchTerm = topic.name
        trending_tweets = api.GetSearch(topicSearchTerm)
        for tweet in trending_tweets:
            util.safe_print(tweet.GetText())
    # pass
