#! C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python.exe
#test.py
# coding: utf-8
#!/usr/bin/env python
# In[ ]:
#print("Content-Type: text/html") 
  
#import cgitb 
import requests
#import json

while (True):
    base_url = 'http://amit.codemix.in/time_sedular.php'
    response = requests.get(base_url)
    response = response.text
    if(response!=""):
	    base_url = 'https://api.telegram.org/bot5413394611:AAFE_SLHcKs4orJrL3KrKBqOzlIdwEDI0nM/sendMessage?chat_id=-1001628930827&text={} '.format(response)
	    requests.get(base_url) 
    else:print(False)





  




  


