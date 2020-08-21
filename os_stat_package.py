import os
import time
path = "./test.py"
status = os.stat(path)
print(status)
print("status.st_mode "+ str(status.st_mode))       #file type and filemode bits
print("status.st_ino "+ str(status.st_ino))         #represent the inode number of Unix
print("status.st_dev "+ str(status.st_dev))         #identifier of the device on which file resides
print("status.st_nlink "+ str(status.st_nlink))     #number of hard links
print("status.st_uid "+ str(status.st_uid))         #user identifier of the file owner
print("status.st_gid "+ str(status.st_gid))         #group identifier of the file owner
print("status.st_size "+ str(status.st_size))       #sizes of the files in bytes
print("status.st_atime "+ str(status.st_atime))     #time of recent access.
print("status.st_mtime "+ str(status.st_mtime))     #time last modified 
print("status.st_ctime "+ str(status.st_ctime))     #time of most recent meta data change

time_in_secs = time.time() - (60)   
print("t" + str(time_in_secs))
print("t" + str(time.time())) #time() The time() function returns the number of seconds passed since epoch. For Unix system, January 1, 1970, 00:00:00 at UTC is epoch

''' Output:
posix.stat_result(st_mode=33188, st_ino=23761034, st_dev=16777220, st_nlink=1, st_uid=502, st_gid=20, st_size=17, st_atime=1597990385, st_mtime=1597990383, st_ctime=1597990383)
status.st_mode 33188
status.st_ino 23761034
status.st_dev 16777220
status.st_nlink 1
status.st_uid 502
status.st_gid 20
status.st_size 17
status.st_atime 1597990385.11
status.st_mtime 1597990383.75
status.st_ctime 1597990383.75
t1597992841.24
t1597992901.24 
'''