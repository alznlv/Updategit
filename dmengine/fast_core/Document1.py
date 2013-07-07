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
        if out.find('create mode')>=0:
            print 'file be created'
            print out.split(' ')[-1]
        if out.find('delete mode')>=0:
            print 'file be deleted'
            print out.split(' ')[-1]
        if out.find('rename')>=0:
            print 'file be renamed'
            s1=out.split(' ')[-1]
            pre=s1[0:s1.find('{')]
            oldname=s1[s1.find('{'):s1.find('}')].split('=>')[0]
            newname=s1[s1.find('{'):s1.find('}')].split('=>')[1]
            print pre
            print oldname
            print newname
            print pre+oldname
            print pre+newname
        outlist=out.split('|')
        if len(outlist)>1 and outlist[0].find('dmengine/')>=0:
            change_file_list.append(outlist[0].strip())
            print change_file_list
    if p.poll() is None:
        p.kill()    
    print p.returncode

getoutput()