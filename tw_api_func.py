import json
import pandas as pd
from requests_oauthlib import OAuth1Session
from pprint import pprint
import config

CK = config.CK
CS = config.CS
AT = config.AT
ATS = config.ATS


twitter = OAuth1Session(CK, CS, AT, ATS)

url_update = "https://api.twitter.com/1.1/statuses/update.json"
url_destroy = "https://api.twitter.com/1.1/statuses/destroy/:id.json"
url_retweets = "https://api.twitter.com/1.1/statuses/retweets/:id.json"
url_user_timeline = "https://api.twitter.com/1.1/statuses/user_timeline.json"
url_search = "https://api.twitter.com/1.1/search/tweets.json"
url_favorite = "https://api.twitter.com/1.1/favorites/create.json"
url_friend = "https://api.twitter.com/1.1/friendships/create.json"
url_getfriend = "https://api.twitter.com/1.1/friends/ids.json"


#params_post = {"status": "hello", "in_reply_to_status_id":"1125737072193445888"}
params_get = {"count":3}
params_destroy = {}


myid = 917958153383366656

#req = twitter.post(url_update, params = params_post)
#req = twitter.get(url_user_timeline, params = params_get)

def search_tweet():
    keyword = input('>>')
    params_search = {'q':keyword, 'count':5}
    req = twitter.get(url_search, params=params_search)

    print('test')
    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline['statuses']:
            print('-'*50)
            print(tweet['user']['name'] + '   :::   ' + tweet['text'])
            print(tweet['created_at'])
            print(tweet['id'])
            print('-'*50)
    else:
        print('ERROR; %d'% req.status_code)

def post_tweet_frominput():
    tweet = input('>>')
    params_post = {'status':tweet}
    req = twitter.post(url_update, params=params_post)

def post_tweet(tweet):
    params_post = {'status':tweet}
    req = twitter.post(url_update, params=params_post)
    if req.status_code == 200:
        result_str = 'successfully posted'
    else:
        # print('ERROR; %d' % req.status_code)
        result_str = 'error'
    return result_str

def delete_all():
    params = {'count':100}
    req = twitter.get(url_user_timeline, params=params)
    timeline = json.loads(req.text)
    for tweet in timeline:
        del_req = twitter.post("https://api.twitter.com/1.1/statuses/destroy/{}.json".format(tweet['id']))

def show_owntweet():
    params = {'count':100}
    req = twitter.get(url_user_timeline, params=params)
    timeline = json.loads(req.text)
    for tweet in timeline:
        print(tweet['text'], tweet['id'])

    pprint(timeline)

def favorite():
    id = input('>>')
    param_fav = {'id':id}
    req = twitter.post(url_favorite, params = param_fav)

def search_fav():
    keyword = input('>>')
    params_search = {'q':keyword, 'count':3}
    req_search = twitter.get(url_search, params = params_search)

    timeline = json.loads(req_search.text)
    for tweet in timeline['statuses']:
        req_fav = twitter.post(url_favorite, params = {'id':tweet['id']})
        print('successfully liked')


def checkdic():
    keyword = input('>>')
    params_search = {'q':keyword, 'count':1}
    req = twitter.get(url_search, params=params_search)
    timeline = json.loads(req.text)
    nya = type(timeline)
    pprint(timeline)


def search_getinfo():
    keyword = input('>>')
    params_search = {'q':keyword, 'count':5}
    req_search = twitter.get(url_search, params = params_search)
    timeline = json.loads(req_search.text)
    for tweet in timeline['statuses']:
        print(tweet['user']['name'], ' : follower is', tweet['user']['followers_count'])
        print(tweet['user']['name'], ' : friend is', tweet['user']['friends_count'])

def search_follow(keyword):
    params_search = {'q':keyword, 'count':7}
    req_search = twitter.get(url_search, params = params_search)
    timeline = json.loads(req_search.text)
    return_str = ''
    for tweet in timeline['statuses']:
        fo = tweet['user']['followers_count']
        fr = tweet['user']['friends_count']
        user_id = tweet['user']['id']
        if fo / fr < 1.1 and fo / fr > 0.9:
            req_follow = twitter.post(url_friend, params={'user_id':user_id})
            print('successfully followed')
            return_str += 'success:'+fo+'/'+fr+'\n'
            # return 'successfully followed'
        else:
            print('out of range')
            return_str += 'out of range\n'
            # return 'out of range'

    return return_str
def friend_fav():
    params_friend = {'user_id':myid}
    req = twitter.get(url_getfriend, params=params_friend)
    friends = json.loads(req.text)
    return_str = ''
    for id in friends['ids']:
        req_timeline = twitter.get(url_user_timeline, params={'user_id':id, 'count':7})
        timeline = json.loads(req_timeline.text)
        if timeline[0]['in_reply_to_screen_name'] == None:
            req_fav = twitter.post(url_favorite, params = {'id':timeline[0]['id']})
            print('successfully liked')
            return_str += 'success'+'\n'
        else:
            print('tweet is reply')
            return_str += 'out of target'+'\n'

    return return_str

def search_tweet_bycountry():
    keyword = input('keyword >>')
    lang = input('language >>')
    params_search = {'q':keyword, 'lang':lang, 'count':10}
    req = twitter.get(url_search, params=params_search)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline['statuses']:
            print('-'*50)
            print("username : ", tweet['user']['name'])
            print("screenname : ", tweet['user']['screen_name'])
            print("tweet : ", tweet['text'])
            print("created at : ", tweet['created_at'])
            print("id : ", tweet['id'])
            print("favorite count : ", tweet['favorite_count'])
            print("retweet count : ", tweet['retweet_count'])
            print("url : ", "https://twitter.com/"+tweet['user']['screen_name']+ "/status/" + str(tweet['id']))
            print('-'*50)
    else:
        print('ERROR; %d'% req.status_code)
