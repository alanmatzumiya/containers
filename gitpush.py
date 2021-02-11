import os

os.system("git init && git add . && git commit -m 'auto' && git push origin music_6" + os.environ.get('USERNAME') + " " + os.environ.get('PASSWORD'))
