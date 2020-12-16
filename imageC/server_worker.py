import web
import os
import time
import random
import io
import requests
import traceback

urls = (
    '/simp', 'SimplifiyService',
    '/derep', 'DereplicateService'
    
)

app = web.application(urls, globals())

class SimplifiyService:
      def POST(self):
          upload_data = web.input()
          print (upload_data)
          if 'file_id' in upload_data:
              data1 = upload_data['file_id']              
              data2 = upload_data['file_content']
              f = open('new_html', 'w')
              f.write(data2)
              f.close()
              return 'Simplify File: File: %s \t File Content: %s\n'%(data1, data2)
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
              return 'Dereplicate File: %s \t File Content: %s\n'%(data1, data2)
              
          else:
              return 'Invalid Request'              

if __name__ == '__main__':
    #open_http(download_port)
    app.run()
