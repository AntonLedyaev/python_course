import shutil
import os
import os

with open('result.txt', 'a') as result:
    for current_dir, dirs, files in os.walk('main'):
        if list(filter(lambda x: x.endswith('.py'), files)):
            result.write('{}\n'.format(current_dir))
