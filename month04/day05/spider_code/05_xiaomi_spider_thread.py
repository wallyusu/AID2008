import requests
import time
from threading import Thread,Lock
from queue import Queue
from fake_useragent import UserAgent

class XiaoMiSpider:
    def __init__(self):
        self.url = 'https://app.mi.com/allHotList?page={}'
