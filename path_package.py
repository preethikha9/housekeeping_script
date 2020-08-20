import os
for root in os.walk("./path_check", topdown=False):
   print(root)


''''
Structure:

path_check
    |__check1
    |     |______subcheck1
    |     |______subcheck2
    |__check2
    |     |______subcheck3
    |__check3
'''

''' Output1:
('./path_check/check1/subcheck1', [], [])
('./path_check/check1/subcheck2', [], [])
('./path_check/check1', ['subcheck1', 'subcheck2'], [])
('./path_check/check2/subcheck3', [], [])
('./path_check/check2', ['subcheck3'], [])
('./path_check/check3', [], [])
('./path_check', ['check1', 'check2', 'check3'], []) '''


for root,dirs,files in os.walk("./path_check", topdown=False):
   print(root)
   for names in dirs:
       print(names)


''' Output2:
./path_check/check1/subcheck1
./path_check/check1/subcheck2
./path_check/check1
subcheck1
subcheck2
./path_check/check2/subcheck3
./path_check/check2
subcheck3
./path_check/check3
./path_check
check1
check2
check3
'''