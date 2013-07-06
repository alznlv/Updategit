1import subprocess

def getoutput():
    change_file_list=[]
    p = subprocess.Popen('git pull',stdout=subprocess.PIPE,shell=True)
    while p.poll() is None:
        out=''
        out=p.stdout.readline().strip('\n')
        print out
        if len(out.split('|'))>1:
            change_file_list.append(out.split("|")[0])
            print change_file_list
        else:
            print len(out.split('|'))
            print out.split('|')
        
    print p.returncode

getoutput()