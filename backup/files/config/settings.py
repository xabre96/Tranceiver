import os
# pwd = os.getcwd()
f=open("config.txt","r")
s=f.readlines()
f.close()
host = s[1].strip('\n')
user = s[3].strip('\n')
password = s[5].strip('\n')
s[1] = '192.168.1.1\n'
s[3] = 'pi\n'
s[5] = 'raspberry\n'
f=open("config.txt","w")
f.writelines(s)
f.close()
print host+" "+user+" "+password
# print s[0].strip('ip=\n')
# print s[1].strip('hostname=\n')
# print s[2].strip('password=\n')
# for x in s:
    # ip = x.rstrip('\n')
    # ip = x.rstrip('ip=')
    # print ip