'''
https://docs.langchain.com/oss/python/langchain/overview

https://docs.langchain.com/oss/python/langgraph/overview

https://docs.langchain.com/oss/python/integrations/providers/overview

'''


import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://docs.langchain.com/oss/python/langchain/overview',
    'https://docs.langchain.com/oss/python/langgraph/overview',
    'https://docs.langchain.com/oss/python/integrations/providers/overview'
]

def fetch_content(url):
    response=requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread= threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")        

## This program uses Python threading to fetch multiple web pages simultaneously. Each URL is processed in a 
# separate thread to improve performance. The join() method ensures that the main program waits until all
#  threads finish execution