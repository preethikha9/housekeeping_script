import os
import sys
import time
#----------------------------------------------------------------------
def remove(path):
    """
    Remove the file or directory
    """
    if os.path.isdir(path):
        try:
            os.rmdir(path)
        except OSError:
            print "Unable to remove folder: %s" % path
    else:
        try:
            if os.path.exists(path):
                os.remove(path)
        except OSError:
            print "Unable to remove file: %s" % path
#----------------------------------------------------------------------
def cleanup(path):
    """
    Removes files from the passed in path that are older than or equal 
    to the number_of_days
    """
    time_in_secs = time.time() - (60)                                   # (current time - the file alive duration) gives the time when the function got created.
    for root, dirs, files in os.walk(path, topdown=False):              # traverse from the inner most to the root - deleted the file which was creted x days ago and checks the root directory if it is empty deletes it . so it goes from bottom to top. Thats why topdown is set false. 
        for file_ in files:
            full_path = os.path.join(root, file_)                       # to delete file enter the path from root
            stat = os.stat(full_path)                                   # os.stat has the properties of a file . for more info check 
            
            if stat.st_mtime <= time_in_secs:
                remove(full_path)
            
        if not os.listdir(root):
            remove(root)
            
#----------------------------------------------------------------------
if __name__ == "__main__":                                              # start
    path = sys.argv[1]                                                  # input path eg: python code.py <path>
    cleanup(path)                                                       # goes to function cleanup() with path as input. Goes to line 21