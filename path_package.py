import os
for root in os.walk("./path_check", topdown=False):
   print(root)