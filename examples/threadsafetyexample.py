#!/usr/bin/python

import threading

class limitedResource:
    def __init__(self, count):
        self.count = count
        self.lock = threading.Lock() # remove to show problem

    def aquire(self):
        with self.lock:  # remove to show problem
            if self.count > 0:
                self.count = self.count - 1
                return 1
            else:
                return 0


class resourceHog(threading.Thread):
    aquired = 0
    
    def __init__(self, resource):
        threading.Thread.__init__(self)
        self.res = resource

    def run(self):
        while self.res.aquire():
            self.aquired += 1


if __name__ == "__main__":
    resource = limitedResource(10000)
    hog1 = resourceHog(resource)
    hog2 = resourceHog(resource)    

    hog1.start()
    hog2.run()
    hog1.join()

    print "hog 1 aquired: ", hog1.aquired
    print "hog 2 aquired: ", hog2.aquired
    print "        total: ", hog1.aquired + hog2.aquired
