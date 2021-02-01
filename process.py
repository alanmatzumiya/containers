import os, subprocess

branches = ['music_' + str(j) for j in range(1, 11)]
sentence_1 = "git init"
sentence_2 = " && git add ."
sentence_3 = " && git commit -m 'auto'"
sentence_4 = " && git push origin " 
sentence = sentence_1 + sentence_2 + sentence_3 + sentence_4

for branch in branches:
    f = open("./" + branch + "/gitpush.py", "w")
    f.write('import os\nos.system("' + sentence + branch + '")')
    f.close()
    os.system("python3 ./" + branch + "/gitpush.py")
