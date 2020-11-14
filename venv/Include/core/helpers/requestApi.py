import json
import requests
from config import *

#----------user--------------------------------#
def get_users():
    data = requests.get(req_url + "/user/").json()
    return data

def create_user(data):
    data = requests.post(req_url + "/user/",data=json.dumps(data)).json()
    return data

def get_user(id):
    data = requests.get(req_url + "/user/"+str(id)).json()
    return data

def edit_user(data,id):
    data = requests.post(req_url + "/user/"+str(id),data=json.dumps(data)).json()
    return data

def remove_user(id):
    data = requests.delete(req_url + "/user/"+str(id)).json()
    return data
#----------------------------------------------#


#------------------tasks-----------------------#
def get_tasks():
    data = requests.get(req_url + "/task/").json()
    return data
def get_task(id):
    data = requests.get(req_url + "/task/"+str(id)).json()
    return data
def init_tasks():
    data = requests.get(req_url + "/task/google_init_tasks/").json()
    return data
#---------------------------------------------#


#------------------Question--------------------#
def get_question(tgid):
    data = requests.get(req_url + "/question/question/"+str(tgid)).json()
    return data
def complete_question(id,answer):
    data = requests.get(req_url + "/question/complete?question_id="+str(id)+"&answer="+str(answer)).json()
    return data
def get_init_settings():
    data = requests.get(req_url + "/question/get_current_settings/").json()
    return data
def get_init_question():
    data = requests.get(req_url + "/question/get_current_settings/").json()
    return data
#---------------------------------------------#