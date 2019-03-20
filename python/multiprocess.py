import threading
import time

def thread_job():
    print('T1 start\n')
    time.sleep(0.5)
    print('T1 finish\n')
def T2_job():
	print('T2 start\n')
	time.sleep(0.2)
	print('T2 finish\n')

def main():
    added_thread = threading.Thread(target=thread_job, name="T1")
    thread2 = threading.Thread(target=T2_job,name='T2')
    added_thread.start()
    added_thread.join()
    thread2.start()
    thread2.join()
    time.sleep(0.1)
    print('all done\n')

if __name__ == '__main__':
    main()
