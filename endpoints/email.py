from flask import request,make_response
import json
from dbhelpers import conn_exe_close
from apihelpers import verify_endpoints_info

#this file is for email storing endpoints
#function for posting email
def post():
    #will check if an email is sent or not
    args = verify_endpoints_info(request.json,['email'])
    if (args != None):
        return make_response(json.dumps(args,default=str),400)
    #will check if email already exists or not
    results = conn_exe_close('call email_get(?)',[request.json['email']])
    #if email exists then it will not send a post request to the db
    if(type(results) == list and results[0]['email_count'] == 1): 
        return make_response(json.dumps('Email already exists',default=str),200)
    #if email does not exists then it will send requests
    elif(type(results) == list and results[0]['email_count'] == 0):
        email_post = conn_exe_close('call email_post(?)',[request.json['email']])
        #after successfull posting of an email to the db it will show the message
        if(type(email_post) == list and email_post[0]['email_count'] == 1):
            return make_response(json.dumps('Email added successfully',default=str),200)
        elif(type(email_post) == list and email_post[0]['email_count'] == 0):
            return make_response(json.dumps('Email not added',default=str),400)
        elif(type(email_post) == str):
            return make_response(json.dumps(email_post,default=str),400)
    elif(type(results)==str):
        return make_response(json.dumps(results,default=str),400)
