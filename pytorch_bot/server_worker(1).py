import web
import os
import time
import random
import io
import requests
import traceback
import base64

import tensorflow as tf

from config import Config
from model import CaptionGenerator
from dataset import prepare_train_data, prepare_eval_data, prepare_test_data
from mttkinter import mtTkinter as tk

urls = (
    '/', 'SimplifiyService',
    '/simp', 'SimplifiyService',
    '/derep', 'DereplicateService'
    
)

SERVER_IP = '127.0.0.1'
PORT      = '5000'


A1        = '/simp'
A2        = '/derep'

APP       = [A1, A2]



SERVER_URL ='http://'+SERVER_IP+':'
url = SERVER_URL+PORT

class SimplifiyService:
      def POST(self):
          upload_data = web.input()
          print (upload_data)
          if 'file_id' in upload_data:
              data1 = upload_data['file_id']              
              data2 = upload_data['file_content']
              print ('data2 success, start change')
              
              img = base64.b64decode(data2)
              print ('change success')
              
              f = open('./test/images/pic.jpg', 'wb')
              f.write(img)
              f.close()
              print ('save success')
              
              #deal()
              os.system('python main.py')
              print ('caption success')
              
              fcap = open('./test/results/res.txt','r')
              imgres = fcap.read()
              fcap.close()
              
              asktxt = {'file_id':45678, 'file_content':imgres}
              txtres = requests.post('http://127.0.0.1:8000/', data=asktxt, stream=True)
              resultcode = txtres.status_code
              #if result == 200:
              os.remove('./test/results/res.txt')
              os.remove('./test/images/pic.jpg')
              return txtres.content
              #return 'Simplify File: File: %s \t File Content: %s\n'%(data1, data2)
          else:
              return 'Invalid Request'
              
              
class DereplicateService:
      def POST(self):
          upload_data = web.input()
          print (upload_data)
          if 'file_id' in upload_data:
              data1 = upload_data['file_id']
              data2 = upload_data['file_content']
              f = open('new_html', 'w')
              f.write(data2)
              f.close()
              #return 1
              return 'Dereplicate File: %s \t File Content: %s\n'%(data1, data2)
              
          else:
              return 'Invalid Request'              


if __name__ == '__main__':
    #open_http(download_port)
    app = web.application(urls, globals())
    app.run()
