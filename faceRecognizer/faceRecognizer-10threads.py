from threading import Thread
import time
def BigBox():
    while True:
        print('Big Box is Open')
        time.sleep(5)
        print('Big Bix is Closed')
        time.sleep(5)
def SmallBox():
    while True:
        print('Small Box is Open')
        time.sleep(5)
        print('Small Box is Closed')
        time.sleep(1)
bigBoxThread=Thread(target=BigBox)
smallBoxThread=Thread(target=SmallBox)
bigBoxThread.daemon=True
smallBoxThread.daemon=True
bigBoxThread.start()
smallBoxThread.start()
while True:
    pass