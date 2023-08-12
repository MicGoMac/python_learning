import os.path

# avoid using __file__ as the cases may vary in diff situation
#see https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do

import os
curr_dir = os.path.abspath(os.getcwd())
print(curr_dir)

