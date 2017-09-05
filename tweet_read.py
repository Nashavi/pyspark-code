
# coding: utf-8

# In[ ]:

import tweepy

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener


# In[ ]:

import socket
import json


# In[ ]:

consumer_key = '0nylmq4q4mkeDl0JdE02b2h2f'
consumer_secret = '9kpsyX5pZh2IWhaRdzJpocAgdvJAuibCXErLlr4ev5VxxUrRIx'
access_token = '435092753-jd5rFG3YmpCBMkJ0Igjwh03LwPW0TB7UO2ONKGdy'
access_secret ='YXUVdubwV1nev9moThUvGC3OBxQDAMUSpghLhZpjb1q6Z'


# In[ ]:

class TweetsListener(StreamListener):
    
    def __init__(self,csocket):
        self.client_socket = csocket
        
    def on_data(self,data):
        
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].ecode('utf-8'))
            return True
        
        except BaseException as e:
            print("ERROR",e)
        
        return True
    
    def on_error(self,status):
        print(status)
        return True


# In[ ]:

def SendData(c_socket):
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    
    twitter_stream = Stream(auth,TweetsListener(c_socket))
    twitter_stream.filter(track = ['chelsea'])


# In[ ]:

if __name__ == '__main__':
    s = socket.socket()
    host = '127.0.0.1'
    port = 2225
    s.bind((host,port))

    print('Listening on port ',port)
    
    s.listen(5)
    c,addr = s.accept()
    
    SendData(c)


# In[ ]:



