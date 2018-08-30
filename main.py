from ddos import Ddos
from settings import *

if __name__ == '__main__':
    dos = Ddos(url=URL, methodId=METHOD_ID,
               maxThread=MAX_THREAD, headers=HEADERS)
    dos.start()

    import os
    os.system("pause")
