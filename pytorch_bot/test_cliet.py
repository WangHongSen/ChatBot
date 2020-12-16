import os.path
import requests
import sys

SERVER_IP = '127.0.0.1'
PORT      = '8080'


A1        = '/simp'
A2        = '/derep'

APP       = [A1, A2]



SERVER_URL ='http://'+SERVER_IP+':'

if __name__ == "__main__":

    if len(sys.argv)!=2:
        print('Usage: python client.py app_no [0: simplify  1: dereplicate]')

    #step-1: build request URL
    srv = int(sys.argv[1])
    url = SERVER_URL+PORT+APP[srv]

    #f = open('./2010-0249.html','r')
    content = "what is your name"
    #f.close()
    
    
    #step-2: 
    #0. simplify
    if srv==0:
    
        payload = {'file_id':123456, 'file_content':content}
        

    #1. dereplicate
    if srv==1:
         payload = {'file_id':45678, 'file_content':content}

    r = requests.post(url, data=payload, stream=True)
    result = r.status_code
    if result == 200:
       print(r.content)
