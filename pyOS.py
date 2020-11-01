import os
import re
import shutil
import hashlib

sdir=os.path.split(os.path.realpath(__file__))[0]
rd='user'
rdir=sdir+'\\'+rd
wdir='\\'
ufile=sdir+'\\info.txt'

def register():
    print('你还未注册一个账户，请先注册！')
    un=input('username:')
    up=input('password:')
    unb=un.encode('UTF-8')
    upb=up.encode('UTF-8')
    md5=hashlib.md5(unb)
    unh=md5.hexdigest()
    md5=hashlib.md5(upb)
    uph=md5.hexdigest()
    with open(ufile,'w+') as u:
        u.write(unh+'\n'+uph+'\n')
    rdn=input('请指定根目录的名称（默认为“user”）：')
    rdn=rdn if rdn!='' else 'user'
    if not os.path.isdir(sdir+'\\'+rdn):
        os.mkdir(sdir+'\\'+rdn)
        rd=rdn
    else:
        while os.path.isdir(sdir+'\\'+rdn):
            aws=input('检测到工作目录下已经有一个名为“'+rdn+'”的目录，是否覆盖（Y/N）（此操作会清空指定的文件夹并不可恢复）:')
            if aws in ['Y','y','']:
                shutil.rmtree(sdir+'\\'+rdn)
                os.mkdir(sdir+'\\'+rdir)
                print('根目录已成功创建。')
                rd=rdn
                break
            elif aws in ['N','n']:
                rdn=input('已取消覆盖操作，请重新指定根目录的名称：')
                if not os.path.isdir(sdir+'\\'+rdn):
                    os.mkdir(sdir+'\\'+rdn)
                    rd=rdn
                    break
            else:
                print('出现了计划外的输入，请重新输入。\n')
    print('注册成功！')
#open(ufile,'r')
#-----------------------------------------------------------
#print(sdir)
if not os.path.isfile(ufile):
    register()
l=False
while not l:
    uf=open(ufile,'r')
    u=uf.readlines()
    #print(u)
    #print(u[0][:-1])
    #print(u[1][:-1])
    un=input('username:')
    if un!='root':
        up=input('password:')
        unb=un.encode('UTF-8')
        upb=up.encode('UTF-8')
        md5=hashlib.md5(unb)
        unh=md5.hexdigest()
        md5=hashlib.md5(upb)
        uph=md5.hexdigest()
        if unh==u[0][:-1] and uph==u[1][:-1]:
            break
        elif unh!=u[0][:-1]:
            print('用户名错误！')
        elif uph!=u[1][:-1]:
            print('密码错误！')
    else:
        up=input('password:')
        if up=='root':
            break
        else:
            print('密码错误！')
#-----------------------------------------------------------
while True:
    pattern=r'\\{1}[a-z0-9A-Z]{1,}[\\]{1}[\.]{2}'
    wdir=re.sub(pattern,'',wdir)
    o=un+'@pyLinux-'+wdir+'>'
    inp=input(o)
    igp=inp.split(' ')
    if igp[0] in ['exit','quit','e']:
        break
    #-----------------------------------------------------------
    elif igp[0]=='echo':
        if len(igp)==2 and igp[1]!='':
            print(igp[1])
        elif len(igp)!=2:
            print('参数错误！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='cd':
        if len(igp)==2 and os.path.isdir(rdir+wdir+igp[1]):
            wdir+=(igp[1] if igp[1][0]!='\\' else igp[1][1:])+'\\'
            #print(wdir)
            os.chdir(rdir+wdir)
        else:
            print('目录或参数错误！')
    #-----------------------------------------------------------
    elif igp[0]=='ls':
        if len(igp)==1:
            for filename in os.listdir(rdir+wdir):
                print(filename)
        else:
            print('输入错误！')
    #-----------------------------------------------------------
    elif igp[0]=='new':
        #创建文件
        if len(igp)==2 and not os.path.isfile(rdir+wdir+igp[1]):
            #文件路径必须为当前工作目录的相对路径
            file=open(rdir+wdir+igp[1],'w+')
            file.close()
            print('文件创建成功。')
        elif len(igp)!=2:
            print('参数错误！')
        elif len(igp)==2 and os.path.isfile(rdir+wdir+igp[1]):
            print('文件已存在！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='md':
        #创建一级目录
        if len(igp)==2 and not os.path.isdir(rdir+wdir+igp[1]):
            #目录必须是当前工作目录的相对路径
            os.mkdir(rdir+wdir+igp[1])
            print('文件夹创建成功。')
        elif len(igp)!=2:
            print('参数错误！')
        elif len(igp)==2 and os.path.isdir(rdir+wdir+igp[1]):
            print('目录已存在！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='cat':
        #查看文件内容
        if len(igp)==2 and os.path.isfile(rdir+wdir+igp[1]):
            #文件路径必须为当前工作目录的相对路径
            with open(rdir+wdir+igp[1],'r',encoding='utf-8') as file:
                otp=file.read()
                if otp=='':
                    print('文件为空。')
                else:
                    print('文件内容：\n\"'+otp+'\"')
        elif len(igp)==2 and not os.path.isfile(rdir+wdir+igp[1]):
            print('文件不存在！')
        elif len(igp)!=2:
            print('参数错误！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='edit':
        #编辑文件
        #文件路径必须为当前工作目录的相对路径
        if len(igp)==2 and os.path.isfile(rdir+wdir+igp[1]):
            os.system('start /B notepad '+rdir+wdir+igp[1])
        elif len(igp)==2 and not os.path.isfile(rdir+wdir+igp[1]):
            print('文件不存在！')
        elif len(igp)!=2:
            print('参数错误！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='cp':
        #复制
        if len(igp)==3 and os.path.isfile(rdir+wdir+igp[1]):
            #文件路径必须为当前工作目录的相对路径
            if os.path.isdir(rdir+wdir+igp[2]):
                shutil.copy(igp[1],igp[2])
                print('文件已成功复制。')
            elif os.path.isfile(rdir+wdir+igp[2]):
                while True:
                    aws=input('该路径是一个文件，是否确定要覆盖此文件的内容？[Y/N]:')
                    if aws in ['Y','y','']:
                        shutil.copy(rdir+wdir+igp[1],rdir+wdir+igp[2])
                        print('文件已成功复制。')
                        break
                    elif aws in ['N','n']:
                        print('已取消覆盖操作。')
                        break
                    else:
                        print('出现了计划外的输入，请重新输入。\n')
            else:
                print('目标目录/文件有误！')
        elif len(igp)!=3:
            print('参数错误！')
        elif len(igp)==3 and not os.path.isfile(rdir+wdir+igp[1]):
            print('源文件路径有误！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='cut':
        #剪切
        if len(igp)==3 and os.path.isfile(rdir+wdir+igp[1]):
            if os.path.isdir(rdir+wdir+igp[2]):
                file_n=igp[1].split('\\')[-1]
                if file_n in os.listdir(rdir+wdir+igp[2]):
                    while True:
                        aws=input('该位置已经存在一个同名文件，是否确定要覆盖此文件？[Y/N]:')
                        if aws in ['Y','y','']:
                            os.remove(rdir+wdir+igp[2]+file_n)
                            shutil.move(rdir+wdir+igp[1],rdir+wdir+igp[2])
                            print('文件已成功移动。')
                            break
                        elif aws in ['N','n']:
                            print('已取消覆盖操作。')
                            break
                        else:
                            print('出现了计划外的输入，请重新输入。\n')
                else:
                    shutil.move(rdir+wdir+igp[1],rdir+wdir+igp[2])
            elif os.path.isfile(rdir+wdir+igp[2]):
                print('第二个参数只能是路径！')
            else:
                print('目标目录/文件有误！')
        elif len(igp)!=3:
            print('参数错误！')
        elif len(igp)==3 and not os.path.isfile(rdir+wdir+igp[1]):
            print('源文件路径有误！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='rm':
        #删除
        if len(igp)==2 and os.path.isfile(rdir+wdir+igp[1]):
            #文件路径必须为当前工作目录的相对路径
            while True:
                aws=input('是否确定要删除此文件？[Y/N]:')
                if aws in ['Y','y','']:
                    os.remove(rdir+wdir+igp[1])
                    print('文件已成功删除。')
                    break
                elif aws in ['N','n']:
                    print('已取消删除操作。')
                    break
                else:
                    print('出现了计划外的输入，请重新输入。\n')
        elif len(igp)!=2:
            print('参数错误！')
        elif len(igp)==2 and not os.path.isfile(rdir+wdir+igp[1]):
            print('文件不存在！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='rmdir':
        #删除空目录
        if len(igp)==2 and os.path.isdir(rdir+wdir+igp[1]):
            #目录必须是当前工作目录的相对路径
            while True:
                aws=input('是否确定要删除此目录（只能删除空目录）？[Y/N]:')
                if aws in ['Y','y','']:
                    os.rmdir(rdir+wdir+igp[1])
                    print('目录已成功删除。')
                    break
                elif aws in ['N','n']:
                    print('已取消删除操作。')
                    break
                else:
                    print('出现了计划外的输入，请重新输入。')
        elif len(igp)!=2:
            print('参数错误！')
        elif len(igp)==2 and not os.path.isdir(rdir+wdir+igp[1]):
            print('目录不存在！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='rmtree':
        #删除不为空的目录/多级目录
        if len(igp)==2 and os.path.isdir(rdir+wdir+igp[1]):
            #目录必须是当前工作目录的相对路径
            while True:
                aws=input('是否确定要删除此目录（不为空的目录/多级目录）？[Y/N]:')
                if aws in ['Y','y','']:
                    shutil.rmtree(rdir+wdir+igp[1])
                    print('目录已成功删除。')
                    break
                elif aws in ['N','n']:
                    print('已取消删除操作。')
                    break
                else:
                    print('出现了计划外的输入，请重新输入。')
        elif len(igp)!=2:
            print('参数错误！')
        elif len(igp)==2 and not os.path.isdir(rdir+wdir+igp[1]):
            print('目录不存在！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='rename':
        #重命名
        if len(igp)==3 and os.path.exists(rdir+wdir+igp[1]):
            #文件/目录路径必须为当前工作目录的相对路径
            os.rename(rdir+wdir+igp[1],str(igp[2]))
            print('重命名成功。')
        elif len(igp)!=3:
            print('参数错误！')
        elif len(igp)==3 and not os.path.exists(rdir+wdir+igp[1]):
            print('文件/目录不存在！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='py':
        #调用pyhon解释器
        if len(igp)==1:
            while True:
                i=input('py>')
                try:
                    if i not in ['exit','quit','e']:
                        exec(i)
                    else:
                        break
                except:
                    print('输入错误！')
        elif len(igp)==2:
            print(igp[1])
            if os.path.isfile(igp[1]):
                print(igp[1][-3:])
                if igp[1][-3:] in ['.py','pyc','pyd','pyw']:
                    os.system('python '+igp[1])
                else:
                    print('不是有效的python程序！')
            else:
                print('不是有效的python程序！')
        else:
            print('参数错误！')
    #-----------------------------------------------------------
    elif igp[0]=='ipconfig':
        #显示当前网络配置
        if len(igp)==1:
            f=os.popen('ipconfig')
            d=f.read()
            print(d)
            f.close()
        else:
            print('参数错误！')
    #-----------------------------------------------------------
    elif igp[0]=='ping':
        #同cmd:ping XXX.XXX.XXX.XXX
        if len(igp)==2:
            f=os.popen(r'ping '+igp[1], 'r')
            d=f.read()
            print(d)
            f.close()
        else:
            print('参数错误！')
    #============下面的部分请根据自己的实际情况进行设置或更改==============
    elif igp[0]=='chrome':
        #调用chrome浏览器
        if len(igp)==2:
            if os.path.exists(rdir+wdir+igp[1]):
                os.system('start /B '+sdir+'\\Chrome '+rdir+wdir+igp[1])
            else:
                os.system('start /B '+sdir+'\\Chrome '+igp[1])
        elif len(igp)==1:
            os.system('start /B '+sdir+'\\Chrome')
        elif len(igp)>2:
            print('参数错误！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='word':
        #使用Office Word
        if len(igp)==2 and os.path.isfile(rdir+wdir+igp[1]):
            os.system('start /B '+sdir+'\\Word '+rdir+wdir+igp[1])
        elif len(igp)==2 and not os.path.isfile(rdir+wdir+igp[1]):
            print('这不是一个Word文档！')
        elif len(igp)==1:
            os.system('start /B '+sdir+'\\Word')
        elif len(igp)>2:
            print('参数错误！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='access':
        #使用Office Access
        if len(igp)==2 and os.path.isfile(rdir+wdir+igp[1]):
            os.system('start /B '+sdir+'\\Access '+rdir+wdir+igp[1])
        elif len(igp)==2 and not os.path.isfile(rdir+wdir+igp[1]):
            print('这不是一个Access数据库文件！')
        elif len(igp)==1:
            os.system('start /B '+sdir+'\\Access')
        elif len(igp)>2:
            print('参数错误！')
        else:
            pass
    #-----------------------------------------------------------
    elif igp[0]=='excel':
        #使用Office Excel
        if len(igp)==2 and os.path.isfile(rdir+wdir+igp[1]):
            os.system('start /B '+sdir+'\\Excel '+rdir+wdir+igp[1])
        elif len(igp)==2 and not os.path.isfile(rdir+wdir+igp[1]):
            print('这不是一个Excel表文件！')
        elif len(igp)==1:
            os.system('start /B '+sdir+'\\Excel')
        elif len(igp)>2:
            print('参数错误！')
        else:
            pass
    elif igp[0]=='mysql':
        #调用MySQL
        f=os.system('mysql -u root')
    #============上面的部分请根据自己的实际情况进行设置或更改==============
    else:
        print('\''+inp+'\''+'不是内部或外部命令，请重新输入。')
