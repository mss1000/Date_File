'''
Created on Mar 16, 2015

@author: mike
'''

if __name__ == '__main__':
    pass

import time

while True:
    f = open( time.strftime("%d%b%Y") + '-danni.txt','a')
    s=str(time.strftime("%c"))
    f.write(s + "\n")
    print(s)
    time.sleep(5)
    f.close()


