from ddos import Ddos
from settings import *

if __name__ == '__main__':
	dos = Ddos(url=URL, methodId=METHOD, maxThread=MAX_THREAD)
	dos.start()

	import os
	os.system("pause")