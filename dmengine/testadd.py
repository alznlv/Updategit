import xml.dom.minidom
import os
import subprocess
import traceback
import platform


class SyncWithGitServer(object):
    _pathPrefix='dmengine/'
    _xml_file_path=None
    _file_update_list=[]
    _file_create_list=[]
    _file_delete_list=[]
    _file_rename_dict={}
    _xml_dom=None
    _xml_root=None
    
    def __init__(self,xmlpath):
        self._xml_file_path=xmlpath
        self._xml_dom = xml.dom.minidom.parse(self._xml_file_path)
        self._xml_root = self._xml_dom.documentElement
    def get_attrvalue(self,node, attrname):
        return node.getAttribute(attrname) if node else ''
    def set_attrvalue(self,node, attrname,value):
        return node.setAttribute(attrname,value) if node else ''
    def get_nodevalue(self,node, index = 0):
        return node.childNodes[index].nodeValue if node else ''
    def get_xmlnode(self,node,name):
        return node.getElementsByTagName(name) if node else []  
    def createXmlFileNodeByName(self,nodenamevalue,version=1.0):
        file=self._xml_dom.createElement("file")
        self._xml_root.appendChild(file)
        name = self._xml_dom.createElement("name")
        file.appendChild(name)
        namevalue = self._xml_dom.createTextNode(nodenamevalue)
        name.appendChild(namevalue)
        name.setAttribute('version', str(version))
    def deleteFileNodeByName(self,nodenamevalue):
        file_nodes = self.get_xmlnode(self._xml_root,'file')
        for fn in file_nodes:
            fn_node=self.get_xmlnode(fn,'name')
            for f in fn_node:
                name=self.get_nodevalue(f).encode('utf-8','ignore').strip('\n')
                if  name.replace(self._pathPrefix,'') == nodenamevalue:
                    self._xml_root.removeChild(fn)
    def renameFileNodeByName(self,oldname,newname):
        file_nodes = self.get_xmlnode(self._xml_root,'file')
        for fn in file_nodes:
            fn_node=self.get_xmlnode(fn,'name')
            for f in fn_node:
                fileversion=self.get_attrvalue(f,'version') 
                name=self.get_nodevalue(f).encode('utf-8','ignore').strip('\n')
                if name ==oldname:
                    self.deleteFileNodeByName(oldname)
                    self.createXmlFileNodeByName(newname,fileversion)
    def updateNodeAttriVersionByName(self,name):
        file_nodes = self.get_xmlnode(self._xml_root,'file')
        for fn in file_nodes:
            fn_node=self.get_xmlnode(fn,'name')
            for f in fn_node:
                nodename=self.get_nodevalue(f).encode('utf-8','ignore').strip('\n')
                if nodename == name:
                    try:
                        value=float(self.get_attrvalue(f,'version'))
                        value+=0.1
                    except Exception as e:
                        print e
                    self.set_attrvalue(f,'version',str(value))
    def createFileInDom(self):
        if self._file_create_list not in [None,'']:
            for f in self._file_create_list:
                create_xmlFileNodeByName(f.replace(self._pathPrefix+'\\',''))
    def deleteFileInDom(self):
        if self._file_delete_list not in [None,'']:
            for f in self._file_delete_list:
                deleteFileNodeByName(f.replace(self._pathPrefix+'/',''))
    def renameFileInDom(self):
        if self._file_rename_dict not in [None,'']:
            for oldname,newname in self._file_rename_dict:
                renameFileNodeByName(oldname.replace(self._pathPrefix+'/',''),newname.replace(self._pathPrefix+'/',''))
    def updateFileInDom(self):
        if self._file_update_list not in [None,'']:
            for f in self._file_update_list:
                updateNodeAttriVersionByName(f.replace(self._pathPrefix+'/',''))
    def executeCommand(self,command):
            return subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    def getGitPullOutput(self):
        p = executeCommand('git pull')
        while p.poll() is None:
            out=''
            out=p.stdout.readline().strip('\n').strip()
            print out
            if out.find('Already up-to-date.')>=0:
                break
            elif out.find('create mode')>=0:
                print 'file be created'
                createfilename=out.split(' ')[-1]
                if createfilename.find(self._pathPrefix)>=0:
                    self._file_create_list.append(createfilename)
            elif out.find('delete mode')>=0:
                print 'file be deleted'
                deletefinename=out.split(' ')[-1]
                if deletefinename.find(self._pathPrefix):
                    self._file_delete_list.append(deletefinename)
            elif out.find('rename')>=0 and out.find(self._pathPrefix)>=0:
                print 'file be renamed'
                s1=out.split(' ')[1]
                s2=out.split(' ')[3]
                pre=s1[0:s1.find('{')]
                print pre
                oldname=s1[s1.find('{'):].replace('{','')
                print oldname
                newname=s2.replace('}','')
                print newname
                print pre+oldname
                print pre+newname
                self._file_rename_dict[pre+oldname]=pre+newname
            else:
                outlist=out.split('|')
                if len(outlist)>1 and outlist[0].find(self._pathPrefix)>=0:
                    _file_update_List.append(outlist[0].strip())
                    print _file_update_List
        if p.poll() is None:
            p.kill()    
        print p.returncode
    def writeXmlToFile(self,xmlpath=self._xml_file_path):
        try:
            f = open(path, 'w')
            f.write(self._xml_dom.toprettyxml(indent=""))
        except Exception as e:
            print e
        finally:
            f.close()
            
    def sync(self):
        self.getGitPullOutput()
        self.createFileInDom()
        self.deleteFileInDom()
        self.renameFileInDom()
        self.updateFileInDom()
if __name__=='__main__':
    sync=SyncWithGitServer(os.path.join(os.getcwd(),'localdmengine.xml'))
#    sync.createXmlFileNodeByName('abc\\1.txt')
#    sync.deleteFileNodeByName('tools\\x86-win32\\lib\\vx_tips.db')
#    sync.renameFileNodeByName('tools\\x86-win32\\lib\\vx_tips.db', 'tools\\x86-win32\\lib\\vx_tips-new.db')
#    sync.updateNodeAttriVersionByName("tools\\x86-win32\\lib\\vx_tips.db")
#
#    sync.writeXmlToFile('new.xml')
