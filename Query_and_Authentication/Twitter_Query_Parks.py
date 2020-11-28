import Tokens_keys
import pandas as pd
import numpy as np
import json
import re
from TwitterAPI import TwitterAPI,TwitterPager

'''This file Integrates with Twitter API with below defined query and saves the response as a JSON-file. '''





def Authentification():
    '''Function authentificate application with twitter credentials.
    returns: autentification variable(api)'''
    Api= TwitterAPI(Tokens_keys.Consumer_apikey, Tokens_keys.Consumer_secret_apikey, Tokens_keys.Access_token, Tokens_keys.Access_token_secret)
    return Api


def Request_Tofile(Api,file_name):
    ''' Function using TwitterPager module to paginate of response from Twitter REST API and write it to a json-file.
    IN: file_name represent the name and format of file from which we save all the tweets which are in JSON format
    OUT: file_name of the saved Json data.'''
    temp_list=[]
    
    Request= TwitterPager(Api,'tweets/search/fullarchive/:Fullarchive',{'query':'(Rålambshovsparken OR #Rålambshovsparken) -RT lang:sv','maxResults':'100','fromDate':'201501010000','toDate':'201912310000'})

    for item in Request.get_iterator():
        
            temp_list.append(item)
        

    temp_dict={'statuses':temp_list}

    
    with open(file_name,'w') as file:
        json.dump(temp_dict,file,indent=2) #easier to read

    return file_name

    
      



























