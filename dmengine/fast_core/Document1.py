import subprocess

def getoutput():
    p = subprocess.Popen('git pull',stdout=subprocess.PIPE,shell=True)
    while p.poll() is None:
        out=''
        out=p.stdout.readline().strip('\n')
        print out
    print p.returncode

getoutput()