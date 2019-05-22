import numpy as np
import random as rnd

class PriorityQ:
    __lasttoken: int
    __internalqueue = {}

    def __init__(self):
        self.__lasttoken = rnd.randint(1000,1999)
    
    def put(self, priority: int, queue_item):
        self.__internalqueue[self.__lasttoken] = [priority, queue_item]
        self.__lasttoken += 1
    
    def peek(self):
        if(len(self.__internalqueue) > 0):
            #return self.__internalqueue
            for messagetoken in sorted(self.__internalqueue, key = lambda seq: self.__internalqueue[seq][0]):
                return messagetoken, self.__internalqueue[messagetoken]
        return None
    
    def receive_delete(self):
        if(len(self.__internalqueue) > 0):
            #return self.__internalqueue
            for messagetoken in sorted(self.__internalqueue, key = lambda seq: self.__internalqueue[seq][0]):
                value = self.__internalqueue[messagetoken]
                self.__internalqueue.pop(messagetoken)
                return messagetoken, value
        return None

    def get_depth(self):
        return len(self.__internalqueue)

    def complete(self, messagetoken: int):
        if (messagetoken in self.__internalqueue):
            self.__internalqueue.pop(messagetoken)