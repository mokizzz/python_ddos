from ddos import Ddos
from settings import *

if __name__ == '__main__':
	dos = Ddos()
	
	dos.setUrl(URL)
	dos.setMethod(METHOD)
	dos.setMaxThread(MAX_THREAD)

	dos.start()

	import os
	os.system("pause")