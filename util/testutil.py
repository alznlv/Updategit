import subprocess

def getoutput():
    change_file_list=[]
    p = subprocess.Popen('git pull',stdout=subprocess.PIPE,shell=True)
    while p.poll() is None:
        out=''
        out=p.stdout.readline().strip('\n')
        print out
        if out.find('Already up-to-date.')>=0:
            break;
        outlist=out.split('|')
        if len(outlist)>1 and outlist[0].find('dmengine/')>=0:
            change_file_list.append(outlist[0].strip())
            print change_file_list
    if p.poll() is None:
        p.kill()    
    print p.returncode

getoutput()