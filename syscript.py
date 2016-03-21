__author__ = 'Tao'

import subprocess
import queue
import threading


class MultiCommand:
    '''
    run several commands with process pool.
    '''

    def __init__(self,cmds,maxpool):
        '''
        initial function
        :param cmds: List of cmd. Every cmd is in form of subprocess.Popen()
        :param maxpool: the maximum amount of process running at the same time
        :return: None
        '''
        self.maxpool = maxpool
        self.cmd_queue = queue.Queue(0)
        for i,cmd in enumerate(cmds):
            self.cmd_queue.put({'idx':i,'cmd':cmd})
        self.index = 0

    def run(self):
        '''
        :return: List of command output in order of self.cmds
        '''

        class myThread(threading.Thread):
            def __init__(self,cmdq):
                threading.Thread.__init__(self)
                self.cmdq = cmdq

            def run(self):
                global result,mutex
                while True:
                    if self.cmdq.qsize()>0:
                        cmd_dict = self.cmdq.get()
                        print(cmd_dict)
                        res = subprocess.run(cmd_dict['cmd'],shell=False)
                        mutex.acquire()
                        result[cmd_dict['idx']] = res
                        mutex.release()
                    else:
                        break

        global result,mutex
        result = [None for i in range(self.cmd_queue.qsize())]
        mutex = threading.Lock()
        length = min(self.maxpool,self.cmd_queue.qsize())
        threadList = list()
        for i in range(length):
            threadList.append(myThread(self.cmd_queue))
        for i in range(length):
            threadList[i].start()
        for i in range(length):
            threadList[i].join()
        return [i.stdout.decode() if i.stdout else None for i in result]

if __name__ == '__main__':
    cmds = [
    ['dell3'],
    ['dell5'],
    ['dell'],
    ['dell2'],
    ['dell4']
    ]
    mc = MultiCommand(cmds,1)
    res = mc.run()
    for i in res:
        print(i)