import os
from random import randint

print("hey guys")

for i in range(1,5):
    for j in range(1,randint(1,3)):
        d = str(i) + ' days ago'
        with open('file.txt','a') as f:
            f.write(d)
        os.system('git add .')
        os.system('git commit --date="'+d+'" -m "update commit"')


