import os
import sys

basepath = '.'

entries = os.listdir(basepath)
 
if not 'counter.txt' in entries:
    with open('counter.txt', 'w') as f:
        os.chmod('counter.txt', 0o777)
        f.write('1')
        sys.exit(0)
else:
    with open('counter.txt', 'r+') as f:
        content = f.read()      
        try:
            cnt = int(content) 
            f.seek(0)
            f.truncate()        
            cnt+=1
            os.chmod('counter.txt', 0o777)
            f.write(str(cnt))
            sys.exit(10)
        except:
            sys.exit(1)
        sys.exit(0)
